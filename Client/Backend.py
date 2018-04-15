import speech
class Backend(object):
	def __init__(self):
		pass
		self.asr = speech.ASR()

	def recognize(self):
		self.asr.recognize()
