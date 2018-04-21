import Speech
import NL2KR
import config
from PLAN_QUERY import PLAN_QUERY
from FOIL_GENERATOR import FOIL_GENERATOR
import Util
import os,sys
from Executor import PlanExecutor

__PROB_TMPL_SRC__ = "../src/EXPLANATION_QUERY_INTERFACE/mmp_foil/domains/prob_templ.pddl"
__PROB_DST__ = "/tmp/curr_problem.pddl"
__FOIL_DST__ = "/tmp/curr_foil.sol"
__PLAN_DST__ = "/tmp/curr_plan.sol"
__EXP_CMD__ = "./run_mmp_script.sh"
__EXP_FILE__ = "/tmp/exp.dat"
__VALIDATE_ACTION__ = "(validate_pieces)"

# DUMMY_GOAL = "atend(hasResearchStation(atlanta))"
# DUMMY_FOIL_FORMULA = "always(not(incity(player3,atlanta)))"
# DUMMY_PLAN = ['(fly_by_charter player3 arizona atlanta)', '(build_research_station_new player3 atlanta)']

class Backend(object):
    def __init__(self, model):
        self.model = model
        self.asr = Speech.ASR()
        self.planExecutor = PlanExecutor(self.model)
        self.nl2kr_plan = NL2KR.NL2KR(config.NL2KR_EXE_PATH, config.NL2KR_CONFIG_PATH, config.NL2KR_OUTPUT_FILE)
        self.nl2kr_explain = NL2KR.NL2KR(config.NL2KR_EXE_PATH, config.NL2KR_CONFIG_PATH, config.NL2KR_OUTPUT_FILE)

        self.storage = {}


    def recognizeVoice(self, gui_callback):
        text = self.asr.recognize()
        if text is None:
            response = "I'm sorry, could you please repeat that."
            gui_callback(response)
        else:
            response = "I heard: "+str(text)
            gui_callback(response)

        return text

    def store(self,key,value):
        self.storage[key] = value

    def retrieve(self, key):
        return self.storage[key]



    def get_assistance(self, query_type, onASROut, onPlanningDoneGUI, question_text = None):
        print ("Query Type: ",query_type)
        if question_text is not None:
            text = question_text
        else:
            text = self.recognizeVoice(onASROut)

        if text is not None:
            predicates = self.model.getPredicates()

            if query_type == "plan":
                ltl_representation = self.nl2kr_plan.getLTLRepresentation(text)
                print ("ltl", ltl_representation)
                print ("Processing Plan Query ")
                pq = PLAN_QUERY()
                plan = pq.query_goal(predicates, ltl_representation)
                self.store('last_computed_goal', ltl_representation)
                self.store('last_computed_plan', plan)
                actionListInNaturalLang = self.asr.decodeActionList(plan)
                s = Util.enumStringFromList(actionListInNaturalLang)
                onPlanningDoneGUI(s)

            elif query_type == "explain":
                print ("Processing Explain Query ")
                ltl_representation = self.nl2kr_plan.getLTLRepresentation(text)
                last_computed_goal = self.retrieve('last_computed_goal')
                last_computed_plan = self.retrieve('last_computed_plan')
                print "Explaination Goal :" + str(last_computed_goal)
                print "Explaination Plan :" + str(last_computed_plan)
                fg = FOIL_GENERATOR()
                foil = fg.query_goal(predicates, last_computed_goal, ltl_representation)

                if len(foil) != 0:
                    with open(__FOIL_DST__, 'w') as f_fd:
                         f_fd.write("\n".join(foil))
                    #TODO:create_problem_for_explanation(curr_state, goal, prob_dst)
                    self.create_problem_for_explanation(predicates, last_computed_goal, __PROB_DST__)

                    #TODO:write plan
                    with open(__PLAN_DST__, 'w') as p_fd:
                         p_fd.write("\n".join([__VALIDATE_ACTION__] + last_computed_plan))
                    self.bash_cmd_exec(__EXP_CMD__)

                    with open(__EXP_FILE__) as e_fd:
                         explanation = e_fd.read()
                    #TODO: Send the explanation to GUI
                    onPlanningDoneGUI("explanation"+explanation)

    def update_goal_str(self, curr_str):
        new_str = curr_str.replace("atend(", "(at end ")
        new_str = new_str.replace("always(", "(always ")
        new_str = new_str.replace("not(", "(not ")
        new_str = new_str.replace("incity(", "(in_city ")
        new_str = new_str.replace("hasResearchStation(", "(has_research_station ")
        new_str = new_str.replace(",", " ")
        return new_str

    def create_problem_for_explanation(self, curr_state, goal, prob_dst):
        with open(__PROB_TMPL_SRC__) as p_fd:
             prob_tmp_str = p_fd.read()
        prob_str = prob_tmp_str.format("\n".join(list(curr_state)), self.update_goal_str(goal))
        with open(prob_dst, 'w') as p_fd:
             p_fd.write(prob_str)

    def bash_cmd_exec(self, cmd):
        output = os.popen(cmd)
        return output

    def executePlan(self):
        self.planExecutor.execute(self.retrieve('last_computed_plan'))
