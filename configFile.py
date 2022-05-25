from mtaConfig import mtaConfig
from pyDocsis.cmConfig import cmConfig
import binascii


class configFile(object):
	def __init__(self ):
		self.tlvs = []
		self.configFilePath = ""
		self.tlv_string = ""
		self.tags = DocsisTlvs
		self.hashme = []
	
	def generateStringFromFile(self, file = ""):
		if file != "":
			self.configFilePath = file
		if self.configFilePath != "":
			f = open(self.configFilePath, "rb")
			content = f.read()
			self.tlv_string = binascii.hexlify(content).decode('UTF-8')[:]
		else:
			raise ValueError("Cannot turn a file into a string if there is no file.")
	def getConfig(self):
		if self.tlv_string.startswith("fe0101"):
			bob = mtaConfig()
			bob.configFilePath = self.configFilePath
			bob.tlv_string = self.tlv_string
			return bob
		else:
			bob = cmConfig()
			bob.configFilePath = self.configFilePath
			bob.tlv_string = self.tlv_string
			return bob