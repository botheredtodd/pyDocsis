# For aesthetic reasons, the user is encouraged to put this in a database or something

MTATlvs = {}

MTATlvs["00"] = {}
MTATlvs["00"]["description"] = "/* Pad */"
MTATlvs["00"]["hex"] = "00"
MTATlvs["00"]["datatype"] = "special"
MTATlvs["00"]["subTlvs"] = {}

MTATlvs["02"] = {}
MTATlvs["02"]["description"] = "/* Unknown */"
MTATlvs["02"]["hex"] = "02"
MTATlvs["02"]["datatype"] = "unknown"
MTATlvs["02"]["subTlvs"] = {}

MTATlvs["04"] = {}
MTATlvs["04"]["description"] = "/* Unknown */"
MTATlvs["04"]["hex"] = "04"
MTATlvs["04"]["datatype"] = "unknown"
MTATlvs["04"]["subTlvs"] = {}

MTATlvs["10"] = {}
MTATlvs["10"]["description"] = "/* Unknown */"
MTATlvs["10"]["hex"] = "0a"
MTATlvs["10"]["datatype"] = "unknown"
MTATlvs["10"]["subTlvs"] = {}

MTATlvs["11"] = {}
MTATlvs["11"]["description"] = "SnmpMibObject"
MTATlvs["11"]["hex"] = "0b"
MTATlvs["11"]["datatype"] = "snmp_object"
MTATlvs["11"]["subTlvs"] = {}

MTATlvs["13"] = {}
MTATlvs["13"]["description"] = "/* Unknown */"
MTATlvs["13"]["hex"] = "0d"
MTATlvs["13"]["datatype"] = "unknown"
MTATlvs["13"]["subTlvs"] = {}

MTATlvs["32"] = {}
MTATlvs["32"]["description"] = "/* Unknown */"
MTATlvs["32"]["hex"] = "20"
MTATlvs["32"]["datatype"] = "unknown"
MTATlvs["32"]["subTlvs"] = {}

MTATlvs["34"] = {}
MTATlvs["34"]["description"] = "/* Unknown */"
MTATlvs["34"]["hex"] = "22"
MTATlvs["34"]["datatype"] = "unknown"
MTATlvs["34"]["subTlvs"] = {}

MTATlvs["35"] = {}
MTATlvs["35"]["description"] = "/* Unknown */"
MTATlvs["35"]["hex"] = "23"
MTATlvs["35"]["datatype"] = "unknown"
MTATlvs["35"]["subTlvs"] = {}

MTATlvs["38"] = {}
MTATlvs["38"]["description"] = "SnmpV3TrapReceiver"
MTATlvs["38"]["hex"] = "26"
MTATlvs["38"]["datatype"] = "aggregate"
MTATlvs["38"]["subTlvs"] = {}

MTATlvs["38"]["subTlvs"]["01"] = {}
MTATlvs["38"]["subTlvs"]["01"]["description"] = "SnmpV3TrapRxIP"
MTATlvs["38"]["subTlvs"]["01"]["hex"] = "01"
MTATlvs["38"]["subTlvs"]["01"]["datatype"] = "(encode_ip)"
MTATlvs["38"]["subTlvs"]["01"]["subTlvs"] = {}

MTATlvs["38"]["subTlvs"]["02"] = {}
MTATlvs["38"]["subTlvs"]["02"]["description"] = "SnmpV3TrapRxPort"
MTATlvs["38"]["subTlvs"]["02"]["hex"] = "02"
MTATlvs["38"]["subTlvs"]["02"]["datatype"] = "ushort"
MTATlvs["38"]["subTlvs"]["02"]["subTlvs"] = {}

MTATlvs["38"]["subTlvs"]["03"] = {}
MTATlvs["38"]["subTlvs"]["03"]["description"] = "SnmpV3TrapRxType"
MTATlvs["38"]["subTlvs"]["03"]["hex"] = "03"
MTATlvs["38"]["subTlvs"]["03"]["datatype"] = "ushort"
MTATlvs["38"]["subTlvs"]["03"]["subTlvs"] = {}

MTATlvs["38"]["subTlvs"]["04"] = {}
MTATlvs["38"]["subTlvs"]["04"]["description"] = "SnmpV3TrapRxTimeout"
MTATlvs["38"]["subTlvs"]["04"]["hex"] = "04"
MTATlvs["38"]["subTlvs"]["04"]["datatype"] = "ushort"
MTATlvs["38"]["subTlvs"]["04"]["subTlvs"] = {}

MTATlvs["38"]["subTlvs"]["05"] = {}
MTATlvs["38"]["subTlvs"]["05"]["description"] = "SnmpV3TrapRxRetries"
MTATlvs["38"]["subTlvs"]["05"]["hex"] = "05"
MTATlvs["38"]["subTlvs"]["05"]["datatype"] = "ushort"
MTATlvs["38"]["subTlvs"]["05"]["subTlvs"] = {}

MTATlvs["38"]["subTlvs"]["06"] = {}
MTATlvs["38"]["subTlvs"]["06"]["description"] = "SnmpV3TrapRxFilterOID"
MTATlvs["38"]["subTlvs"]["06"]["hex"] = "06"
MTATlvs["38"]["subTlvs"]["06"]["datatype"] = "(encode_oid)"
MTATlvs["38"]["subTlvs"]["06"]["subTlvs"] = {}

MTATlvs["38"]["subTlvs"]["07"] = {}
MTATlvs["38"]["subTlvs"]["07"]["description"] = "SnmpV3TrapRxSecurityName"
MTATlvs["38"]["subTlvs"]["07"]["hex"] = "07"
MTATlvs["38"]["subTlvs"]["07"]["datatype"] = "string"
MTATlvs["38"]["subTlvs"]["07"]["subTlvs"] = {}

MTATlvs["38"]["subTlvs"]["08"] = {}
MTATlvs["38"]["subTlvs"]["08"]["description"] = "SnmpV3TrapRxIP6"
MTATlvs["38"]["subTlvs"]["08"]["hex"] = "08"
MTATlvs["38"]["subTlvs"]["08"]["datatype"] = "(encode_ip6)"
MTATlvs["38"]["subTlvs"]["08"]["subTlvs"] = {}

MTATlvs["41"] = {}
MTATlvs["41"]["description"] = "/* Unknown */"
MTATlvs["41"]["hex"] = "29"
MTATlvs["41"]["datatype"] = "unknown"
MTATlvs["41"]["subTlvs"] = {}

MTATlvs["48"] = {}
MTATlvs["48"]["description"] = "/* Unknown */"
MTATlvs["48"]["hex"] = "30"
MTATlvs["48"]["datatype"] = "unknown"
MTATlvs["48"]["subTlvs"] = {}

MTATlvs["49"] = {}
MTATlvs["49"]["description"] = "/* Unknown */"
MTATlvs["49"]["hex"] = "31"
MTATlvs["49"]["datatype"] = "unknown"
MTATlvs["49"]["subTlvs"] = {}

MTATlvs["62"] = {}
MTATlvs["62"]["description"] = "/* Unknown */"
MTATlvs["62"]["hex"] = "38"
MTATlvs["62"]["datatype"] = "unknown"
MTATlvs["62"]["subTlvs"] = {}

MTATlvs["64"] = {}
MTATlvs["64"]["description"] = "CMTSStaticMulticastSessionEncodings"
MTATlvs["64"]["hex"] = "40"
MTATlvs["64"]["datatype"] = "aggregate"
MTATlvs["64"]["subTlvs"] = {}

MTATlvs["64"]["subTlvs"]["01"] = {}
MTATlvs["64"]["subTlvs"]["01"]["description"] = "CMTSStaticMulticastSessionGroup"
MTATlvs["64"]["subTlvs"]["01"]["hex"] = "01"
MTATlvs["64"]["subTlvs"]["01"]["datatype"] = "ip_ip6"
MTATlvs["64"]["subTlvs"]["01"]["subTlvs"] = {}

MTATlvs["64"]["subTlvs"]["02"] = {}
MTATlvs["64"]["subTlvs"]["02"]["description"] = "CMTSStaticMulticastSessionSource"
MTATlvs["64"]["subTlvs"]["02"]["hex"] = "02"
MTATlvs["64"]["subTlvs"]["02"]["datatype"] = "ip_ip6"
MTATlvs["64"]["subTlvs"]["02"]["subTlvs"] = {}

MTATlvs["64"]["subTlvs"]["03"] = {}
MTATlvs["64"]["subTlvs"]["03"]["description"] = "CMTSStaticMulticastSessionCMIM"
MTATlvs["64"]["subTlvs"]["03"]["hex"] = "03"
MTATlvs["64"]["subTlvs"]["03"]["datatype"] = "hexstr"
MTATlvs["64"]["subTlvs"]["03"]["subTlvs"] = {}

MTATlvs["64"]["subTlvs"]["107"] = {}
MTATlvs["64"]["subTlvs"]["107"]["description"] = "Technicolor thing"
MTATlvs["64"]["subTlvs"]["107"]["datatype"] = "unknown"
MTATlvs["64"]["subTlvs"]["107"]["subTlvs"] = {}
MTATlvs["64"]["subTlvs"]["107"]['hex'] = "6b"

MTATlvs["65"] = {}
MTATlvs["65"]["description"] = "/* Unknown */"
MTATlvs["65"]["hex"] = "41"
MTATlvs["65"]["datatype"] = "unknown"
MTATlvs["65"]["subTlvs"] = {}

MTATlvs["66"] = {}
MTATlvs["66"]["description"] = "/* Unknown */"
MTATlvs["66"]["hex"] = "42"
MTATlvs["66"]["datatype"] = "unknown"
MTATlvs["66"]["subTlvs"] = {}

MTATlvs["67"] = {}
MTATlvs["67"]["description"] = "/* Unknown */"
MTATlvs["67"]["hex"] = "43"
MTATlvs["67"]["datatype"] = "unknown"
MTATlvs["67"]["subTlvs"] = {}

MTATlvs["68"] = {}
MTATlvs["68"]["description"] = "/* Unknown */"
MTATlvs["68"]["hex"] = "44"
MTATlvs["68"]["datatype"] = "unknown"
MTATlvs["68"]["subTlvs"] = {}

MTATlvs["69"] = {}
MTATlvs["69"]["description"] = "/* Unknown */"
MTATlvs["69"]["hex"] = "45"
MTATlvs["69"]["datatype"] = "unknown"
MTATlvs["69"]["subTlvs"] = {}

MTATlvs["75"] = {}
MTATlvs["75"]["description"] = "/* Unknown */"
MTATlvs["75"]["hex"] = "4b"
MTATlvs["75"]["datatype"] = "unknown"
MTATlvs["75"]["subTlvs"] = {}

MTATlvs["82"] = {}
MTATlvs["82"]["description"] = "/* Unknown */"
MTATlvs["82"]["hex"] = "52"
MTATlvs["82"]["datatype"] = "unknown"
MTATlvs["82"]["subTlvs"] = {}

MTATlvs["93"] = {}
MTATlvs["93"]["description"] = "/* Unknown */"
MTATlvs["93"]["hex"] = "5d"
MTATlvs["93"]["datatype"] = "unknown"
MTATlvs["93"]["subTlvs"] = {}

MTATlvs["97"] = {}
MTATlvs["97"]["description"] = "/* Unknown */"
MTATlvs["97"]["hex"] = "61"
MTATlvs["97"]["datatype"] = "unknown"
MTATlvs["97"]["subTlvs"] = {}

MTATlvs["100"] = {}
MTATlvs["100"]["description"] = "/* Unknown */"
MTATlvs["100"]["hex"] = "64"
MTATlvs["100"]["datatype"] = "unknown"
MTATlvs["100"]["subTlvs"] = {}

MTATlvs["101"] = {}
MTATlvs["101"]["description"] = "/* Unknown */"
MTATlvs["101"]["hex"] = "65"
MTATlvs["101"]["datatype"] = "unknown"
MTATlvs["101"]["subTlvs"] = {}

MTATlvs["103"] = {}
MTATlvs["103"]["description"] = "/* Unknown */"
MTATlvs["103"]["hex"] = "67"
MTATlvs["103"]["datatype"] = "unknown"
MTATlvs["103"]["subTlvs"] = {}

MTATlvs["105"] = {}
MTATlvs["105"]["description"] = "/* Unknown */"
MTATlvs["105"]["hex"] = "69"
MTATlvs["105"]["datatype"] = "unknown"
MTATlvs["105"]["subTlvs"] = {}

MTATlvs["110"] = {}
MTATlvs["110"]["description"] = "/* Unknown */"
MTATlvs["110"]["hex"] = "6e"
MTATlvs["110"]["datatype"] = "unknown"
MTATlvs["110"]["subTlvs"] = {}

MTATlvs["111"] = {}
MTATlvs["111"]["description"] = "/* Unknown */"
MTATlvs["111"]["hex"] = "6f"
MTATlvs["111"]["datatype"] = "unknown"
MTATlvs["111"]["subTlvs"] = {}

MTATlvs["114"] = {}
MTATlvs["114"]["description"] = "/* Unknown */"
MTATlvs["114"]["hex"] = "72"
MTATlvs["114"]["datatype"] = "unknown"
MTATlvs["114"]["subTlvs"] = {}

MTATlvs["116"] = {}
MTATlvs["116"]["description"] = "/* Unknown */"
MTATlvs["116"]["hex"] = "74"
MTATlvs["116"]["datatype"] = "unknown"
MTATlvs["116"]["subTlvs"] = {}

MTATlvs["117"] = {}
MTATlvs["117"]["description"] = "/* Unknown */"
MTATlvs["117"]["hex"] = "75"
MTATlvs["117"]["datatype"] = "unknown"
MTATlvs["117"]["subTlvs"] = {}

MTATlvs["118"] = {}
MTATlvs["118"]["description"] = "/* Unknown */"
MTATlvs["118"]["hex"] = "76"
MTATlvs["118"]["datatype"] = "unknown"
MTATlvs["118"]["subTlvs"] = {}

MTATlvs["120"] = {}
MTATlvs["120"]["description"] = "/* Unknown */"
MTATlvs["120"]["hex"] = "78"
MTATlvs["120"]["datatype"] = "unknown"
MTATlvs["120"]["subTlvs"] = {}

MTATlvs["121"] = {}
MTATlvs["121"]["description"] = "/* Unknown */"
MTATlvs["121"]["hex"] = "79"
MTATlvs["121"]["datatype"] = "unknown"
MTATlvs["121"]["subTlvs"] = {}

MTATlvs["163"] = {}
MTATlvs["163"]["description"] = "/* Unknown */"
MTATlvs["163"]["hex"] = "a3"
MTATlvs["163"]["datatype"] = "unknown"
MTATlvs["163"]["subTlvs"] = {}

MTATlvs["254"] = {}
MTATlvs["254"]["description"] = "MtaConfigDelimiter"
MTATlvs["254"]["hex"] = "fe"
MTATlvs["254"]["datatype"] = "uchar"
MTATlvs["254"]["subTlvs"] = {}

MTATlvs["255"] = {}
MTATlvs["255"]["description"] = "/*EndOfDataMkr*/"
MTATlvs["255"]["datatype"] = "special"
MTATlvs["255"]["subTlvs"] = {}
MTATlvs["255"]['hex'] = "ff"




if __name__ == '__main__':
	def printSubTLVS(tlv, parent):
		for key in tlv:
			if tlv[key]["datatype"] == "aggregate":
				print("var tlv" + parent + key + " = TLVDefinitions(tag: " + key + ", dataType: ." + tlv[key]["datatype"] + ", description: \"" + tlv[key]["description"] + "\")")
			else:
				print("let tlv" + parent + key + " = TLVDefinitions(tag: " + key + ", dataType: ." + tlv[key]["datatype"] + ", description: \"" + tlv[key]["description"] + "\")")
			printSubTLVS(tlv[key]["subTlvs"], parent + key)
			print("tlv" + parent + ".subTLVs.append(tlv" + parent + key  + ")")

	endbits = "let DOCSIS :[TLVDefinitions] = [\n"
	#fp = open("outs.json", 'w')
	#json.dump(MTATlvs, fp)
	for key in MTATlvs.keys():
		endbits += "tlv" + key + ",\n"
		if MTATlvs[key]["datatype"] == "aggregate":
			print("var tlv" + key + " = TLVDefinitions(tag: " + key + ", dataType: ." + MTATlvs[key]["datatype"] + ", description: \"" + MTATlvs[key]["description"] + "\")")
		else:
			print("let tlv"  + key + " = TLVDefinitions(tag: " + key + ", dataType: ." + MTATlvs[key]["datatype"] + ", description: \"" + MTATlvs[key]["description"] + "\")")
		printSubTLVS(MTATlvs[key]["subTlvs"], key)
	endbits += "]"
	print(endbits)