#!/usr/bin/env python3
import binascii
import codecs
import sys
from TLV import TLV
from docsisTlvs import DocsisTlvs
from MTATlvs import MTATlvs
from mib import mib
import json
import hashlib

class cmConfig(object):
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
	
						if value_end_position > len(tlv_string) and hv != "ff" and tag != "00" and tag != "107" and tag != "61" and tag != "97" and tag != "101" and tag != "35" and tag != "10" and tag != "106" and tag != "116" and tag != "52" and tag != "48" and tag != "51" and tag != "54" and tag != "102"  and tag != "83" and tag != "118" and tag != "67" and tag != "80":
							raise ValueError('Parse error: tag ' + tag + ' declared data of length ' + str(value_length) + ', but actual data length is ' + str(int(len(tlv_string[value_start_position-1:-1])/2)))
						else:
							value = tlv_string[value_start_position:value_end_position]
							if len(tags[tag]["subTlvs"].keys()) > 0:
								#print(tag)
								#print("down")
								subts = self.parse(value, tags[tag]["subTlvs"])
								#print("up")
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
		oldTLV7 = TLV(tag="07", datatype = "md5", value = "")
		stuff = '' #'0x'
		lastTLV = TLV()
		for tag in self.tlvs:
			if tag.tag not in ["06","07","255"]:
				if tag.tag != "00":
					stuff += tag.encodeForFile()
			elif tag.tag in ["06","07"]:
				self.hashme.append(tag.tag)
				if tlv.tag == "07":
					oldTLV7.setValue(tlv.getValue())
			else:
				lastTLV = tag
		#stuff = stuff.encode('UTF-8')
		exts = ""
		if '06' in self.hashme:
			newval = hashlib.md5(binascii.unhexlify(stuff))
			print(newval.hexdigest())
			nextTLV = TLV(tag="06", datatype = "md5", value = newval.hexdigest())
			exts += nextTLV.encodeForFile()
		if '07' in self.hashme:
		#	newval = hashlib.md5(binascii.unhexlify(stuff))
		#	nextTLV = TLV(tag="07", datatype = "md5", value = newval.hexdigest())
		
			exts += oldTLV7.encodeForFile()
		
		stuff += exts	
		stuff += lastTLV.encodeForFile()
		
		#while (len(stuff)/2) % 4 == 0:
		#	stuff += "00"
		#print(stuff)
		if self.configFilePath != "":
			f = open(self.configFilePath, "wb")
			f.write(binascii.unhexlify(stuff))
			f.close
	
def jsonThis(tlvs):
	outs = {}
	for t in tlvs:
		if len(t.subTLVs) == 0:
			outs[t.tag] = str(t.getValue()) + " (" + t.datatype + ")"
		else:
			outs[t.tag] = jsonThis(t.subTLVs)
	return outs	
	
if __name__ == '__main__':
	cm = cmConfig()
	cm.generateStringFromFile(sys.argv[1])
	#print(cm.tlv_string)
	if len(sys.argv) > 2:
		if sys.argv[2] == "MTA":
			cm.tags = MTATlvs
	#print(cm.tlv_string)
	cm.tlvs = cm.parse(cm.tlv_string, cm.tags)
	#oots = jsonThis(cm.tlvs)
	#print(json.dumps(oots, indent = 4))
	cm.configFilePath += ".new"
	#newtlvs = []
	for tlv in cm.tlvs:
		if tlv.tag == "06":
			print(tlv.getValue())
		if tlv.tag == "07":
			print(tlv.getValue())	
		#else:
		#	print(tlv.tag)
		#	print(tlv.getValue())
		#if tlv.tag in ["24","25"]:
		#	for st in tlv.subTLVs:
		#		 if st.tag == "08":
		#			 st.setValue(1000000)
	# 	if tlv.tag == "11":
	# 		if "1.3.6.1.4.4413" in tlv.getValue():
	# 			print("found it")
	# 			print(tlv.getValue())
	# 			tlv.setValue(binascii.hexlify(tlv.getValue().split(" ")[3].encode("ascii")).decode(), tlv.getValue().split(" ")[0].replace("4.4413", "4.1.4413"))
	# 			print(tlv.getValue())
	# 			newtlvs.append(tlv)
	# 		else:
	# 			print(tlv.getValue().split(" ")[0])
	# 			newtlvs.append(tlv)
	# 	else:
	# 		newtlvs.append(tlv)
	#cm.tlvs = newtlvs
	#cm.encode()
	# 
