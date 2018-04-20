import Speech
import NL2KR
import config
from PLAN_QUERY import PLAN_QUERY
from FOIL_GENERATOR import FOIL_GENERATOR
import Util

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
            ltl_representation = self.nl2kr_plan.getLTLRepresentation(text)
            print ("ltl", ltl_representation)

            predicates = self.model.getPredicates()

            if query_type == "plan":
                print ("Processing Plan Query ")
                pq = PLAN_QUERY()
                plan = pq.query_goal(predicates, ltl_representation)
                actionListInNaturalLang = self.asr.decodeActionList(plan)
                s = Util.enumStringFromList(actionListInNaturalLang)
                onPlanningDoneGUI(s)

            elif query_type == "explanation":
                print ("Processing Explain Query ")
                fg = FOIL_GENERATOR()
                foil = fg.query_goal(predicates, ltl_representation)
                if len(foil) != 0:
                    pass

    def executePlan(self):
        pass

    def updateState(self):
        pass
