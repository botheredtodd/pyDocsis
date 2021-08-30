
oidDataTypes = {}
oidDataTypes["64"] = "IPAddress"
oidDataTypes["4"] = "HexString"


class mib:
	def __init__(self):
		# storing these as strings
		self.oid = ""
		self.value = ""
		self.dataType = ""
	def decode(self, hexJunk):
		"""
		based on panda_inline4's comment at https://stackoverflow.com/questions/49653398/converting-oid-of-public-key-etc-in-hex-data-to-the-dot-format
		
		"""
		# decodes the mib stuff from the config file.
		hex_list = [] 
		OID_str = ''
		for char in range(0,len(hexJunk),2):
			hex_list.append(hexJunk[char]+hexJunk[char+1])
		
		for element in range(len(hex_list)):
			hex_list[element] = int(hex_list[element],16)
		if hex_list[0] == 48: #this has been 48 for all of the ones I tested
			OID_str += "" 
		del hex_list[0] # oid tag
		totalLength = hex_list[0]
		del hex_list[0] # -- length of oid
		noIdea = hex_list[0]
		del hex_list[0] 
		oidlength = hex_list[0]
		del hex_list[0] 
		
		x = int(hex_list[0] / 40)
		y = int(hex_list[0] % 40)
		if x > 2:
			y += (x-2)*40
			x = 2;
		OID_str += str(x)+'.'+str(y)
		del hex_list[0]
		oidlength -= 1
		val = 0
		while len(hex_list) > 0:
			oidlength -= 1
			val = ((val<<7) | ((hex_list[0] & 0x7F)))
			if (hex_list[0] & 0x80) != 0x80:
				OID_str += "."+str(val)
				val = 0
			self.oid = OID_str
			if oidlength == 0:
				del hex_list[0]
				datatype = hex_list[0]
				del hex_list[0]
				datalength = int(str(hex_list[0]), 16)
				del hex_list[0]
				snmpdata = ""
				strDataType = str(datatype)
				while len(hex_list) > 0:
					if str(datatype) in oidDataTypes.keys():
						strDataType = oidDataTypes[str(datatype)]
						if oidDataTypes[str(datatype)] == "IPAddress":
							snmpdata += str(hex_list[0])
							if len(hex_list) > 1:
								snmpdata += "."
						elif oidDataTypes[str(datatype)] == "HexString":
							snmpdata += hex(hex_list[0])[2:]
							if len(hex_list) == 1:
								snmpdata = "0x" + snmpdata
					else:
						print("What is the datatype for mibby thingie " + str(datatype))		
						snmpdata += str(hex_list[0])
					del hex_list[0]
				self.dataType = strDataType
				self.value = snmpdata
				OID_str += " Data Type: " + strDataType + " Length: " + str(datalength) + " Value: " + snmpdata
			else:
				del hex_list[0]
				
		# print the OID in dot notation.
		#print(OID_str)
	def encode(self):
		outBlob = ""
		