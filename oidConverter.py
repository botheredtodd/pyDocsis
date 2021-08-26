import mibs

def notation_OID(oidhex_string):
	"""
	copied from panda_inline4's comment at https://stackoverflow.com/questions/49653398/converting-oid-of-public-key-etc-in-hex-data-to-the-dot-format
	
	"""
	''' Input is a hex string and as one byte is 2 charecters i take an 
		empty list and insert 2 characters per element of the list.
		So for a string 'DEADBEEF' it would be ['DE','AD','BE,'EF']. '''
	hex_list = [] 
	OID_str = ''
	for char in range(0,len(oidhex_string),2):
		hex_list.append(oidhex_string[char]+oidhex_string[char+1])
	
	print(hex_list)
	''' I have deleted the first two element of the list as my hex string
		includes the standard OID tag '06' and the OID length '0D'. 
		These values are not required for the calculation as i've used 
		absolute OID and not using any ASN.1 modules. Can be removed if you
		have only the data part of the OID in hex string. '''
	
	for element in range(len(hex_list)):
		hex_list[element] = int(hex_list[element],16)
	if hex_list[0] == 48:
		OID_str += "" #"1.3"
	del hex_list[0] # oid tag
	totalLength = hex_list[0]
	del hex_list[0] # -- length of oid
	# The first two digits of the OID are calculated differently from the rest. 
	noIdea = hex_list[0]
	del hex_list[0] 
	oidlength = hex_list[0]
	print(oidlength)
	del hex_list[0] 
	
	x = int(hex_list[0] / 40)
	y = int(hex_list[0] % 40)
	if x > 2:
		y += (x-2)*40
		x = 2;
	OID_str += str(x)+'.'+str(y)
	del hex_list[0]
	# An empty string to append the value of the OID in standard notation after
	# processing each element of the list.
	

	# Convert the list with hex data in str format to int format for 
	# calculations.
	i = 0

	# Convert the OID to its standard notation. Sourced from code in other 
	# languages and adapted for python.

	# The first two digits of the OID are calculated differently from the rest. 
	#x = int(hex_list[0] / 40)
	#y = int(hex_list[0] % 40)
	#if x > 2:
	#	y += (x-2)*40
	#	x = 2;
	#elif x == 0:
	#	if oidType != "":
	#		x = oidType
	#OID_str += str(x)+'.'+str(y)
	#del hex_list[0]
	val = 0
	while len(hex_list) > 0:
		oidlength -= 1
		val = ((val<<7) | ((hex_list[0] & 0x7F)))
		if (hex_list[0] & 0x80) != 0x80:
			OID_str += "."+str(val)
			val = 0
		if oidlength == 0:
			del hex_list[0]
			datatype = hex_list[0]
			del hex_list[0]
			datalength = int(str(hex_list[0]), 16)
			del hex_list[0]
			snmpdata = ""
			while len(hex_list) > 0:
				snmpdata += str(hex_list[0])
				del hex_list[0]
			OID_str += " Data Type: " + str(datatype) + " Length: " + str(datalength) + " Value: " + snmpdata
		else:
			del hex_list[0]
			
	# print the OID in dot notation.
	return OID_str
def unnotation_OID(oidhex_string):
	"""
	copied from a few lines up, and mangled.
	
	"""
	''' Input is a hex string and as one byte is 2 charecters i take an 
		empty list and insert 2 characters per element of the list.
		So for a string 'DEADBEEF' it would be ['DE','AD','BE,'EF']. '''
	hex_list = oidhex_string.split(".")
	OID_str = ''
	for char in range(0,len(oidhex_string),2):
		hex_list.append(oidhex_string[char]+oidhex_string[char+1])

	''' I have deleted the first two element of the list as my hex string
		includes the standard OID tag '06' and the OID length '0D'. 
		These values are not required for the calculation as i've used 
		absolute OID and not using any ASN.1 modules. Can be removed if you
		have only the data part of the OID in hex string. '''
	if int(hex_list[0], 16) == 48:
		OID_str += "1.3"
	del hex_list[0] # oid tag
	oidLength = int(hex_list[0], 16)
	del hex_list[0] # -- length of oid

	# An empty string to append the value of the OID in standard notation after
	# processing each element of the list.
	

	# Convert the list with hex data in str format to int format for 
	# calculations.
	i = 0
	for element in range(len(hex_list)):
		hex_list[element] = int(hex_list[element],16)

	# Convert the OID to its standard notation. Sourced from code in other 
	# languages and adapted for python.

	# The first two digits of the OID are calculated differently from the rest. 
	#x = int(hex_list[0] / 40)
	#y = int(hex_list[0] % 40)
	#if x > 2:
	#	y += (x-2)*40
	#	x = 2;

	#OID_str += str(x)+'.'+str(y)

	val = 0
	for byte in range(0,len(hex_list)):
		val = ((val<<7) | ((hex_list[byte] & 0x7F)))
		if (hex_list[byte] & 0x80) != 0x80:
			OID_str += "."+str(val)
			val = 0

	# print the OID in dot notation.
	return (OID_str)

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
	oid.insert(0, 0x30) # Add a Type (0x06 for Object Identifier)
	return oid
 
 
#notation_OID('060D2B0621040BA946964812D10905')
#print(notation_OID('301b060f2b06010401a01301030101020305050408efe7e7480de64166'))

#print(unnotation_OID('1.3.6.15.43.6.1.4.1.4115.1.3.1.1.2.3.5.5.4.8.234484680.13.13121.102'))