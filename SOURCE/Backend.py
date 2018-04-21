import Speech
import NL2KR
import config
from PLAN_QUERY import PLAN_QUERY
from FOIL_GENERATOR import FOIL_GENERATOR
import Util
__PROB_TMPL_SRC__ = "../src/EXPLANATION_QUERY_INTERFACE/mmp_foil/domains/prob_templ.pddl"
__PROB_DST__ = "/tmp/curr_problem.pddl"
__FOIL_DST__ = "/tmp/curr_foil.sol"
__PLAN_DST__ = "/tmp/curr_plan.sol"
__EXP_CMD__ = "./run_mmp_script.sh"
__EXP_FILE__ = "/tmp/exp.dat"

class Backend(object):
    def __init__(self, model):
        self.model = model
        self.asr = Speech.ASR()
        self.nl2kr_plan = NL2KR.NL2KR(config.NL2KR_EXE_PATH, config.NL2KR_CONFIG_PATH, config.NL2KR_OUTPUT_FILE)
        self.nl2kr_explain = NL2KR.NL2KR(config.NL2KR_EXE_PATH, config.NL2KR_CONFIG_PATH, config.NL2KR_OUTPUT_FILE)

    def recognizeVoice(self, gui_callback, query_type = "plan"):
        text = self.asr.recognize()
        # text = "How can player1 go to Delhi?"
        if text is None:
            response = "I'm sorry, could you please repeat that."
            gui_callback(response)
        else:
            response = "I heard: "+str(text)
            gui_callback(response)

        return text



    def get_assistance(self, query_type, onASROut, onPlanningDoneGUI):
        print ("Query Type: ",query_type)

        # text = self.recognizeVoice(onASROut)
        text = "How can player1 go to Delhi?"
        if text is not None:
            predicates = self.model.getPredicates()

            if query_type == "plan":
                ltl_representation = self.nl2kr_plan.getLTLRepresentation(text)
                print ("ltl", ltl_representation)
                print ("Processing Plan Query ")
                pq = PLAN_QUERY()
                plan = pq.query_goal(predicates, ltl_representation)
                actionListInNaturalLang = self.asr.decodeActionList(plan)
                s = Util.enumStringFromList(actionListInNaturalLang)
                onPlanningDoneGUI(s)

            elif query_type == "explain":
                print ("Processing Explain Query ")
                fg = FOIL_GENERATOR()
                foil = fg.query_goal(predicates, ltl_representation)
                if len(foil) != 0:
                    with open(__FOIL_DST__, 'w') as f_fd:
                         f_fd.write("\n".join(foil))
                    #TODO:create_problem_for_explanation(curr_state, goal, prob_dst)
                    #TODO:write plan
                    self.bash_cmd_exec(__EXP_CMD__)
                    with open(__EXP_FILE__) as e_fd:
                         explanation = e_fd.read()
                  #TODO: Send the explanation to GUI

    def create_problem_for_explanation(self, curr_state, goal, prob_dst):
        with open(__PROB_TMPL_SRC__) as p_fd:
             prob_tmp_str = p_fd.read()
        prob_str = prob_tmp_str.format(curr_state, goal)
        with open(prob_dst) as p_fd:
             p_fd.write(prob_str)

    def bash_cmd_exec(self, cmd):
        output = os.popen(cmd)
        return output

    def executePlan(self):
        pass
