import Speech
class Backend(object):
	def __init__(self):
		pass
		self.asr = Speech.ASR()

	def recognize(self):
		self.asr.recognize()