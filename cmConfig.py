from docsisTlvs import DocsisTlvs
import binascii

class cmConfig(object):
	def __init__(self ):
		self.tlvs = []
		self.configFilePath = ""
		self.tlv_string = ""
		self.tags = DocsisTlvs
	
	def generateStringFromFile(self, file = ""):
		if file != "":
			self.configFilePath = file
		if self.configFilePath != "":
			f = open(self.configFilePath, "rb")
			content = f.read()
			self.tlv_string = binascii.hexlify(content).decode('UTF-8')[:]
		else:
			raise ValueError("Cannot turn a file into a string if there is no file.")
	def parse(self, tlv_string = "", tags = {}):
		"""
		stolen from https://github.com/timgabets/pytlv and modified
		"""
		tlvs = []
		if len(tlv_string) == 0:
			tlv_string = self.tlv_string
			print(tlv_string)
		i = 0
		if len(tags.keys()) == 0:
			print("Loading keys form docsis file")
			tags = self.tags
		while i < len(tlv_string): 
			tag_found = False
			tag_length = 2
			for tag in tags.keys():
					hv = hex(int(tag)).replace('0x', '')
					if len(hv) == 1:
						hv = "0" + hv
					if tlv_string[i:i+tag_length] == hv:
						try:
							if tlv_string[i+tag_length:i+tag_length+2] != '':
								value_length = int(tlv_string[i+tag_length:i+tag_length+2], 16)
						except ValueError:
							raise ValueError('Parse error: tag ' + tag + ' has incorrect data length')
	
						value_start_position = i+tag_length+2
						value_end_position = i+tag_length+2+value_length*2
	
						if value_end_position > len(tlv_string) and hv != "ff" and tag != "00":
							raise ValueError('Parse error: tag ' + tag + ' declared data of length ' + str(value_length) + ', but actual data length is ' + str(int(len(tlv_string[value_start_position-1:-1])/2)))
						else:
							value = tlv_string[value_start_position:value_end_position]
							if len(tags[tag]["subTlvs"].keys()) > 0:
								# print("#################")
								# print(i)
								# print(tag)
								# print(tags[tag]["subTlvs"].keys())
								# print(value)
								# print("#################")
								# #print(tlvs)
								# print("down")
								subts = self.parse(value, tags[tag]["subTlvs"])
								# print("up")
								parsed_data = [tag, subts]
								tlvs.append(parsed_data)
							else:
								parsed_data = [tag, value]
								tlvs.append(parsed_data)
							i = value_end_position
						tag_found = True
			if not tag_found:
				print(i)
				print(tlvs)
				msg = 'Unknown tag found: ' + tlv_string[i:i+10]
				raise ValueError(msg)
		return tlvs
if __name__ == '__main__':
	cm = cmConfig()
	cm.generateStringFromFile("cm.cfg")
	cm.tlvs = cm.parse(cm.tlv_string, cm.tags)
	print("########")
	for t in cm.tlvs:
		print(t)
	
