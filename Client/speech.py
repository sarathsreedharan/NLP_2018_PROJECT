import speech_recognition as sr

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
             
            #error occurs when google could not understand what was said
             
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
             
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))


if __name__ == "__main__":
    asr = ASR()
    asr.recognize()


