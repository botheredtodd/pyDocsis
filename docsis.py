import binascii
import codecs
import sys


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
		for st in self.subTLVs:
			tvalue += st.encode(tags[self.tag]["subTlvs"])
		if divmod(len(tvalue), 2)[1] == 1:
			print(htag)
			print(tvalue)
			print(divmod(len(tvalue), 2))
			raise ValueError('Invalid value length - the length must be even')

		tlv_string += tlv_string + htag.upper() + hexify(len(tvalue) / 2) +tvalue.upper()
		return tlv_string	
	def decode(self, tags):
		tvalue = self.value
		if "strzero" in tags[self.tag]["datatype"]:
			tvalue = tvalue[:-2]
		elif "encode_uint" in tags[self.tag]["datatype"]:
			return int(self.value, 16)
			return codecs.decode(tvalue, encoding='hex')
		elif "ushort" in tags[self.tag]["datatype"]:
			return int(self.value, 16)
			return codecs.decode(tvalue, encoding='hex')
		elif "snmp_object" in tags[self.tag]["datatype"]:
			return notation_OID(tvalue)
		else:
			return tvalue