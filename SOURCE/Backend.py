import Speech
import NL2KR
import config
from PLAN_QUERY import PLAN_QUERY
from FOIL_GENERATOR import FOIL_GENERATOR

class Backend(object):
    def __init__(self, model):
        self.model = model
        self.asr = Speech.ASR()
        self.nl2kr_plan = NL2KR.NL2KR(config.NL2KR_EXE_PATH, config.NL2KR_CONFIG_PATH, config.NL2KR_OUTPUT_FILE)
        self.nl2kr_explain = NL2KR.NL2KR(config.NL2KR_EXE_PATH, config.NL2KR_CONFIG_PATH, config.NL2KR_OUTPUT_FILE)

    def recognizeVoice(self, gui_callback, query_type = "plan"):
        #text = self.asr.recognize()
        text = "How can player1 go to Delhi?"
        if text is None:
            text = "I'm sorry, could you please repeat that."
            gui_callback(text)
        else:
            ltl_representation = self.nl2kr_plan.getLTLRepresentation(text)
            print ("ltl",ltl_representation)
            predicates = self.model.getPredicates()
            if query_type == "plan":
               pq = PLAN_QUERY()
               gui_callback("I heard: " + str(text) + " :" + ltl_representation)
               plan = pq.query_goal(predicates, ltl_representation)
               gui_callback("PLAN:\n"+"\n".join(plan))
            elif query_type == "explanation":
               #"bajilsnsalklals"
               fg = FOIL_GENERATOR()
               gui_callback("I heard: " + str(text) + " :" + ltl_representation)
               foil = fg.query_goal(predicates, ltl_representation)
               if len(foil) != 0:
                  

#if __name__ == "__main__":
#   bb = Backend()
