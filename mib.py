import codecs
oidDataTypes = {}
oidDataTypes["66"] = "UInt32"
oidDataTypes["64"] = "IPAddress"
oidDataTypes["6"] = "objectIdentifier"
oidDataTypes["5"] = "Null"
oidDataTypes["4"] = "HexString"
oidDataTypes["3"] = "BitString"
oidDataTypes["2"] = "Integer32"
oidDataTypes["1"] = "Boolean"


	
## The following two functions are stolen from https://github.com/AstralVX/oidhex_to_dot
def encode_variable_length_quantity(v:int) -> list:
	# Break it up in groups of 7 bits starting from the lowest significant bit
	# For all the other groups of 7 bits than lowest one, set the MSB to 1
	m = 0x00
	output = []
	while v >= 0x80:
		output.insert(0, (v & 0x7f) | m)
		v = v >> 7
		m = 0x80
	output.insert(0, v | m)
	return output
def encode_oid_string(oid_str:str) -> tuple:
	a = [int(x) for x in oid_str.split('.')]
	oid = [a[0]*40 + a[1]] # First two items are coded by a1*40+a2
	# A rest is Variable-length_quantity
	for n in a[2:]:
		oid.extend(encode_variable_length_quantity(n))
	oid.insert(0, len(oid)) # Add a Length
	
	# Yeah, we seem to be using pid type 0x30
	# oid.insert(0, 0x30) # Add a Type (0x06 for Object Identifier)
	return oid

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
						self.dataType = strDataType
						if oidDataTypes[str(datatype)] == "IPAddress":
							snmpdata += str(hex_list[0])
							if len(hex_list) > 1:
								snmpdata += "."
						elif oidDataTypes[str(datatype)] == "HexString":
							working = ""
							while len(hex_list) > 1:
								tmp = str(hex(hex_list[0]))[2:]
								if len(tmp) % 2 == 1:
									tmp = "0" + tmp
								working += tmp
								del hex_list[0]
							working += str(hex(hex_list[0]))[2:]
							if len(working) % 2 == 1:
								working = "0" + working
							snmpdata = "0x" + working
						elif oidDataTypes[str(datatype)] == "UInt32":
							working = ""
							while len(hex_list) > 1:
								working += hex(hex_list[0])
								del hex_list[0]
								print(working)
							working += hex(hex_list[0])
							#print("Is " + str(int(working, 16)) + " a number?")
							snmpdata = str(int(working, 16))
					else:
						print("OID is : " + self.oid)
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
		if self.dataType == "HexString":
			datalen = str(hex(int(len(self.value[2:]) / 2)))[2:]
			if len(datalen) == 1:
				datalen = "0" + datalen
			outBlob = outBlob + self.value[2:]
			outBlob = datalen + outBlob
			outBlob = "0" + str(hex(4))[2:] + outBlob 
		elif self.dataType == "IPAddress":
			datalen = "04"
			for s in self.value.split("."):
				# print(s)
				addr = str(hex(int(s)))[2:]
				if len(addr) % 2 == 1:
					addr = "0" + addr
				outBlob += addr
				# if len(outBlob) % 2 == 1:
					# outBlob = "0" + outBlob
			outBlob = datalen + outBlob
			outBlob = str(hex(64))[2:] + outBlob
		elif self.dataType == "UInt32":
			outBlob += str(hex(int(self.value)))
			if len(outBlob) % 2 == 1:
				outBlob = "0" + outBlob
			datalen = int(len(outBlob) / 2)
			outBlob = str(hex(datalen))[2:] + outBlob
			outBlob = str(hex(66))[2:] + outBlob	

			
			
			
		oidBlob = ""
		for by in encode_oid_string(self.oid):
			val = str(hex(int(by)))[2:]
			if len(val) == 1:
				val = "0" + val
			result = val.replace('0x', '').upper()
			if divmod(len(result), 2)[1] == 1:
				# Padding
				result = '0{}'.format(result)
			oidBlob += result
		outBlob = oidBlob + outBlob
		outBlob = "06" + outBlob #OBJECT IDENTIFIER data type
		outBlob = str(hex(int(len(outBlob) / 2)))[2:] + outBlob
		if divmod(len(outBlob), 2)[1] == 1:
			# Padding
			outBlob = '0{}'.format(outBlob)
		outBlob = "30" + outBlob #because reasons...
		
		return outBlob
			
		
		
		