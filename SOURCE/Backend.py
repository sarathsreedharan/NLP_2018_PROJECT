import Speech
import ConfigParser

class Backend(object):
	def __init__(self):
		pass
		self.asr = Speech.ASR()

	def recognize(self,callback):
		self.asr.recognize(callback)








	# b=Backend()
	# b.getLTLRepresentation("")