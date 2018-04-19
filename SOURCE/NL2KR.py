import Util
import config
class NL2KR(object):
    def __init__(self, nl2kr_exe_path, nl2kr_config_path, nl2kr_output_file):
        self.nl2kr_exe_path = nl2kr_exe_path
        self.nl2kr_config_path = nl2kr_config_path
        self.nl2kr_output_file = nl2kr_output_file

        with open(nl2kr_config_path, 'r') as f:
            self.config_file_lines_array = f.readlines()

    def getInputFile(self):
        nl2kr_input_file = filter(lambda line: 'Tdata' in line, self.config_file_lines_array)[0].split("=")[1]
        return nl2kr_input_file

    def __execute(self):
        cmd = self.nl2kr_exe_path + " " + self.nl2kr_config_path
        return Util.executeCommand(cmd, self.nl2kr_output_file, config.NL2KR_DIR)

    def getLTLRepresentation(self, text_string):
        result =  self.__execute()
        for line in result:
            if "Predicted result #0" in line:
                return line.split(":")[1][1:]


#
# if __name__ == "__main__":
#     nl2kr_exe_path = "/home/midhun/Documents/NLP/NLP_2018_PROJECT/NL2KR/NL2KR-T.sh"
#     nl2kr_config_path = "/home/midhun/Documents/NLP/NLP_2018_PROJECT/NL2KR/config.txt"
#     nl2kr_output_file = "/home/midhun/Documents/NLP/NLP_2018_PROJECT/NL2KR/out.txt"
#
#     nl2kr = NL2KR(nl2kr_exe_path,nl2kr_config_path,nl2kr_output_file)
#     print nl2kr.getLTLRepresentation("how can i go to Delhi")
#
