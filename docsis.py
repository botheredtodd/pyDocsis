import binascii
import codecs
import sys
from TLV import TLV
from docsisTlvs import DocsisTlvs
from mib import mib

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
	
						if value_end_position > len(tlv_string) and hv != "ff" and tag != "00" and tag != "107" and tag != "61" and tag != "97" and tag != "101" and tag != "35" and tag != "10":
							raise ValueError('Parse error: tag ' + tag + ' declared data of length ' + str(value_length) + ', but actual data length is ' + str(int(len(tlv_string[value_start_position-1:-1])/2)))
						else:
							value = tlv_string[value_start_position:value_end_position]
							if len(tags[tag]["subTlvs"].keys()) > 0:
								subts = self.parse(value, tags[tag]["subTlvs"])
								parsed_data = [tag, subts]
								tlvs.append(TLV(tag = tag, subTLVs = subts, datatype = tags[tag]["datatype"]))
								#tlvs.append(parsed_data)
							else:
								#if "str" in tags[tag]["datatype"]:	
								#	if "encode_strzero" in tags[tag]["datatype"]:
								#		value = value[:-2]
								#	value = codecs.decode(value, "hex")
								#parsed_data = [tag,  tags[tag]["description"], tags[tag]["datatype"] , value]
								tlvs.append(TLV(tag = tag, value = value, datatype = tags[tag]["datatype"]))
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
	#print(cm.tlv_string)
	cm.tlvs = cm.parse(cm.tlv_string, cm.tags)
	#cm.configFilePath = "cm2.cfg"
	#print(cm.tlv_string.upper())
	#print()
	#cm.encode()
	#print("########")
	
	for t in cm.tlvs:
		#if t.datatype in ["uchar", "uint", "ushort", "hexstr"]:
			# bb = t.getValue()
			# print("before")
			# print(t.value)
			# t.setValue(bb)
			# print("after")
			# print(t.value)
		#print(t.tag)
		if t.tag == "11":
			print(t.value)
			m = t.getValue()
			print(m.value)
			print(m.encode())
		#if "datatype" in DocsisTlvs[t.tag].keys():
		#	print(DocsisTlvs[t.tag]["datatype"])
		#if DocsisTlvs[t.tag]["datatype"] == "(decode_snmp_object)":
		#print(t.datatype)
		# t.getValue()
		#print(t.getValue())
		#for tt in t.subTLVs:
			#print("  " + tt.tag)
			#print("  " + tt.datatype)
			#if tt.datatype in ["uchar", "uint", "ushort", "hexstr", "strzero"]:
				# bb = tt.getValue()
				# print("before")
				# print(tt.value)
				# tt.setValue(bb)
				# print("after")
				# print(tt.value)
			#if "datatype" in DocsisTlvs[t.tag]["subTlvs"][tt.tag].keys():
			#	print("  " + DocsisTlvs[t.tag]["subTlvs"][tt.tag]["datatype"])
			# print("  " + str(tt.getValue()))
			#tt.getValue()
		#	print("  " + tt.decodedValue(DocsisTlvs[t.tag]["subTlvs"]))
	
