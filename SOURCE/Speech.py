import speech_recognition as sr
import PredicateUtils


class ASR(object):
    def __init__(self):
        #enter the name of usb microphone that you found using lsusb
        mic_name = 'HDA Intel PCH: ALC3266 Analog (hw:0,0)'
        #Sample rate is how often values are recorded
        self.sample_rate = 48000
        #Chunk is like a buffer. It stores 2048 samples (bytes of data), it is advisable to use powers of 2 such as 1024 or 2048
        self.chunk_size = 2048
        #Initialize the recognizer
        self.recognizer = sr.Recognizer()
         
        #generate a list of all audio cards/microphones
        mic_list = sr.Microphone.list_microphone_names()
         
        #the following loop aims to set the device ID of the mic thatwe specifically want to use to avoid ambiguity.
        for i, microphone_name in enumerate(mic_list):
            if microphone_name == mic_name:
                self.device_id = i

    def recognize(self):
        #use the microphone as source for input. Here, we also specify 
        #which device ID to specifically look for incase the microphone 
        #is not working, an error will pop up saying "device_id undefined"
        with sr.Microphone(device_index = self.device_id, sample_rate = self.sample_rate,chunk_size = self.chunk_size) as source:
            #wait for a second to let the recognizer adjust the 
            #energy threshold based on the surrounding noise level
            self.recognizer.adjust_for_ambient_noise(source)
            print "Tell me what you would like to do?"
            #listens for the user's input
            audio = self.recognizer.listen(source)
                 
            try:
                text = self.recognizer.recognize_google(audio)
                print "You said: " + text
                return text
             
            #error occurs when google could not understand what was said
             
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
             
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None

    def undefinedActionMethod(self,name):
        return "Cannot Execute:{} Action -> Undefined Method".format(name)

    def speak(self, natural_language_sentence_list):

        for sentence in natural_language_sentence_list:
            pass

    def decodeActionList(self,list_of_actions):
        print "Decoding : "+str(list_of_actions)
        if(len(list_of_actions) ==0):
            return ['No need to do anything']

        nl_texts = []
        for action in list_of_actions:
            action_name, action_params = PredicateUtils.extractNameAndParametersFromAction(action)
            func = getattr(self, action_name, self.undefinedActionMethod(action_name))
            nl_texts.append(func(action_params))

        return nl_texts

    def build_research_station_new(self, params):
        player = params[0]
        city = params[1]
        nl_text = '%(player)s should build a research station at %(city)s' % {'player':player, 'city':city}
        return nl_text

    def move_research_station(self,params):
        player = params[0]
        city1 = params[1]
        city2 = params[2]
        nl_text = '%(player)s should move the research station at %(city1)s to %(city2)s' % {'player':player, 'city1':city1, 'city2':city2}
        return nl_text

    def fly_directly(self, params):
        player = params[0]
        fromCity = params[1]
        toCity = params[2]
        nl_text = '%(player)s should surrender his %(toCity)s card and then relocate to %(toCity)s' % {'player':player, 'toCity':toCity}
        return nl_text


    def fly_by_charter(self,params):
        player = params[0]
        fromCity = params[1]
        toCity = params[2]
        nl_text = '%(player)s should charter from %(fromCity)s to %(toCity)s' % {'player':player,'fromCity':fromCity, 'toCity':toCity}
        return nl_text

    def fly_by_shuttle(self,params):
        player = params[0]
        fromCity = params[1]
        toCity = params[2]
        nl_text = '%(player)s should shuttle from %(fromCity)s to %(toCity)s' % {'player':player,'fromCity':fromCity, 'toCity':toCity}
        return nl_text


    def treat_disease(self,params):
        player = params[0]
        disease = params[1]
        nl_text = '%(player)s should treat %(disease)s' % {'player':player, 'disease':disease}
        return nl_text

    def treat_cured_disease_begin(self,params):
        pass

    def treat_cured_disease_end(self,params):
        pass

    def share_knowledge(self,params):
        player1 = params[0]
        player2 = params[1]
        city = params[2]
        nl_text = '%(player1)s should give %(city) card to %(player2)s to share knowledge' % {'player1':player1, 'player2':player2,'city':city}
        return nl_text

    def cure_disease(self,params):
        player = params[0]
        city1 = params[1]
        city2 = params[2]
        city3 = params[3]
        city4 = params[4]
        disease = params[5]

        nl_text = '%(player1)s should surrender %(city1) %(city2) %(city3) and %(city4) cards and mark %(disease) disease as cured' % \
                  {'player':player, 'city1':city1, 'city2':city2, 'city3':city3, 'city4':city4, 'disease':disease}

        return nl_text


if __name__ == "__main__":
    asr = ASR()
    asr.recognize()


