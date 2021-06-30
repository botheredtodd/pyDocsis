from docsisTlvs import DocsisTlvs

class cmConfig(object):
	def __init__(self ):
		self.tlvs = []
		self.configFilePath = ""
		self.tlv_string = ""
		self.tags = DocsisTlvs
		
	def parse(self):
		"""
		stolen from https://github.com/timgabets/pytlv and modified
		"""
		i = 0
		while i < len(self.tlv_string): 
			tag_found = False
			#for tag_length in self.tag_lengths:
				tag_length = 2
				for tag, tag_name in self.tags.items():
					if self.tlv_string[i:i+tag_length] == tag:
						try:
							#print(self.tlv_string[i+tag_length:i+tag_length+2])
							if self.tlv_string[i+tag_length:i+tag_length+2] != '':
								value_length = int(self.tlv_string[i+tag_length:i+tag_length+2], 16)
						except ValueError:
							#print(i)
							#for t in parsed_data.keys():
							#	print(str(t) + ": " + str(parsed_data[t]))
							raise ValueError('Parse error: tag ' + tag + ' has incorrect data length')

						value_start_position = i+tag_length+2
						value_end_position = i+tag_length+2+value_length*2

						if value_end_position > len(self.tlv_string) and tag != "ff" and tag != "00":
							#print(i)
							#for t in parsed_data.keys():
							#	print(str(t) + ": " + str(parsed_data[t]))
							raise ValueError('Parse error: tag ' + tag + ' declared data of length ' + str(value_length) + ', but actual data length is ' + str(int(len(self.tlv_string[value_start_position-1:-1])/2)))
						else:
							value = self.tlv_string[value_start_position:value_end_position]
							parsed_data = [tag, value]
							self.tlvs.apend(parsed_data)
							i = value_end_position
							tag_found = True
			if not tag_found:
				#print(i)
				#for t in parsed_data.keys():
				#	print(str(t) + ": " + str(parsed_data[t]))
				msg = 'Unknown tag found: ' + self.tlv_string[i:i+10]
				raise ValueError(msg)
		return parsed_data
