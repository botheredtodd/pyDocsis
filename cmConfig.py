from docsisTlvs import DocsisTlvs
import binascii
import codecs
from oidConverter import notation_OID
import sys

def hexify(number):
	"""
	Convert integer to hex string representation, e.g. 12 to '0C'
	"""
	if number < 0:
		raise ValueError('Invalid number to hexify - must be positive')

	result = hex(int(number)).replace('0x', '').upper()
	if divmod(len(result), 2)[1] == 1:
		# Padding
		result = '0{}'.format(result)
	return result



class TLV:
	def __init__(self, **args):
		if "tag" in args.keys():
			self.tag = args["tag"]
		else:
			self.tag= ""
		if "datatype" in args.keys():
			self.datatype = args["datatype"]
		else:
			self.datatype = ""
		if "value" in args.keys():
			self.value = args["value"]
		else:
			self.value = ""
		if "subTLVs" in args.keys():
			self.subTLVs = args["subTLVs"]
		else:
			self.subTLVs = []
	def encode(self, tags = {}):
		if tags == {}:
			tags = DocsisTlvs
		tlv_string = ''
		htag = tags[self.tag]["hex"]
		tvalue = self.value
		#print(htag)
		#print(tvalue)
		for st in self.subTLVs:
			tvalue += st.encode(tags[self.tag]["subTlvs"])
		if divmod(len(tvalue), 2)[1] == 1:
			print(htag)
			print(tvalue)
			print(divmod(len(tvalue), 2))
			raise ValueError('Invalid value length - the length must be even')

		tlv_string += tlv_string + htag.upper() + hexify(len(tvalue) / 2) +tvalue.upper()
		return tlv_string	
	def decodedValue(self, tags):
		tvalue = self.value
		if "encode_strzero" in tags[self.tag]["datatype"]:
			tvalue = tvalue[:-2]
		elif "encode_uint" in tags[self.tag]["datatype"]:
			return int(self.value, 16)
			return codecs.decode(tvalue, encoding='hex')
		elif "encode_ushort" in tags[self.tag]["datatype"]:
			return int(self.value, 16)
			return codecs.decode(tvalue, encoding='hex')
		elif "decode_snmp_object" in tags[self.tag]["datatype"]:
			return notation_OID(tvalue)
		else:
			return tvalue
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
			print("Loading keys from docsis file")
			tags = self.tags
		while i < len(tlv_string): 
			tag_found = False
			tag_length = 2
			for tag in tags.keys():
					hv = tags[tag]["hex"] #hex(int(tag)).replace('0x', '')
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
								#print(tag)
								# print(tags[tag]["subTlvs"].keys())
								# print(value)
								# print("#################")
								#print("down")
								subts = self.parse(value, tags[tag]["subTlvs"])
								#print("up")
								parsed_data = [tag, subts]
								tlvs.append(TLV(tag = tag, subTLVs = subts))
								#tlvs.append(parsed_data)
							else:
								#if "str" in tags[tag]["datatype"]:	
								#	if "encode_strzero" in tags[tag]["datatype"]:
								#		value = value[:-2]
								#	value = codecs.decode(value, "hex")
								#parsed_data = [tag,  tags[tag]["description"], tags[tag]["datatype"] , value]
								tlvs.append(TLV(tag = tag, value = value))
							i = value_end_position
						tag_found = True
			if not tag_found:
				#print(i)
				print(tlvs)
				msg = 'Unknown tag found: ' + tlv_string[i:i+10]
				raise ValueError(msg)
		return tlvs
	def encode(self):
		stuff = '' #'0x'
		for tag in self.tlvs:
			stuff += tag.encode()
		#stuff = stuff.encode('UTF-8')
		#print(stuff)
		if self.configFilePath != "":
			f = open(self.configFilePath, "wb")
			f.write(binascii.unhexlify(stuff))
			f.close
		
if __name__ == '__main__':
	cm = cmConfig()
	cm.generateStringFromFile(sys.argv[1])
	cm.tlvs = cm.parse(cm.tlv_string, cm.tags)
	#cm.configFilePath = "cm2.cfg"
	print(cm.tlv_string.upper())
	#print()
	#cm.encode()
	#print("########")
	#for t in cm.tlvs:
		#print(t.tag)
		#if "datatype" in DocsisTlvs[t.tag].keys():
			#print(DocsisTlvs[t.tag]["datatype"])
		#if DocsisTlvs[t.tag]["datatype"] == "(decode_snmp_object)":
			#print(t.value)
			#print(t.decodedValue(DocsisTlvs))
		#for tt in t.subTLVs:
		#	print(tt.tag)
		#	if "datatype" in DocsisTlvs[t.tag]["subTlvs"][tt.tag].keys():
		#		print(DocsisTlvs[t.tag]["subTlvs"][tt.tag]["datatype"])
		#	print(tt.value)
		#	print(tt.decodedValue(DocsisTlvs[t.tag]["subTlvs"]))
	
