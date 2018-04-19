import Speech
import NL2KR
import config


class Backend(object):
    def __init__(self):
        pass
        self.asr = Speech.ASR()
        self.nl2kr = NL2KR.NL2KR(config.NL2KR_EXE_PATH, config.NL2KR_CONFIG_PATH, config.NL2KR_OUTPUT_FILE)

    def recognizeVoice(self, gui_callback):
        text = self.asr.recognize()
        if text is None:
            text = "I'm sorry, could you please repeat that."
            gui_callback(text)
        else:
            ltl_representation = self.nl2kr.getLTLRepresentation(text)
            gui_callback("I heard: " + str(text) + " :" + ltl_representation)
