import Util
import config

class NL2KR(object):
    def __init__(self, nl2kr_exe_path, nl2kr_config_path, nl2kr_output_file):
        self.nl2kr_exe_path = nl2kr_exe_path
        self.nl2kr_config_path = nl2kr_config_path
        self.nl2kr_output_file = nl2kr_output_file

        with open(nl2kr_config_path, 'r') as f:
            self.config_file_lines_array = f.readlines()
        with open(config.NL2KR_DICT_WORDS) as d_fd:
            self.dict_words = [i.strip().lower() for i in d_fd.readlines()]

    def getInputFile(self):
        nl2kr_input_file = filter(lambda line: 'Tdata' in line, self.config_file_lines_array)[0].split("=")[1]
        return nl2kr_input_file

    def __execute(self):
        cmd = self.nl2kr_exe_path + " " + self.nl2kr_config_path
        return Util.executeCommand(cmd, self.nl2kr_output_file, config.NL2KR_DIR)
    def return_closest_words(self, word):
        '''
           TODO: Use the word2vec distance to find
                 the closest word from self.dict_words
        '''
        return word

    def update_with_dict_words(self, curr_words):
        new_words = []
        for w in curr_words:
            if w in self.dict_words:
                new_words.append(w)
            else:
                new_words.append(self.return_closest_words(w))
         return " ".join(new_words)

    def getLTLRepresentation(self, old_text_string):
        text_parts = text_string.split(" ")
        text_string = self.update_with_dict_words()
        with open(config.NL2KR_INPUT_FILE, 'w') as n_fd:
             n_fd.write(text_string+"\n")        
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
