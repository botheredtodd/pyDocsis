from MTATlvs import MTATlvs
from mtaConfig import mtaConfig
import sys 
import binascii

# The bats that load a config file:
cm = mtaConfig()
cm.generateStringFromFile(sys.argv[1])
cm.tags = MTATlvs
print(cm.tlv_string)
cm.tlvs = cm.parse(cm.tlv_string, cm.tags)

for t in cm.tlvs:
	#By default, the tlv value is left in hex as a string. getValue() decodes it.
	t.getValue()

	if t.tag =="64": #In addition to being stupid, dialmaps are fat. This means they end up in TLV64 rather than TLV11
		newstring = "0F" # this is the ASCII "shift in" character, which seems to start every dialmap
		m = t.getValue()
		print(m.oid)
		print(m.dataType)
		oldvalue = m.value
		for line in m.value.split('\r\n'): #CRLF is what I am forcing the line endings into
			#print("##### " + line + " #####")
			newstring += binascii.hexlify(line.encode()).decode('UTF-8')#[:]
			#The next two lines put the CRLF back on, but in the format the file uses.
			newstring += "0D"
			newstring += "0A"
			#newstring + "\r\n"
			if line == '<10> "[2-8]11" : RETURN(#0)':
				newstring += '”(988)” : RETURN(#0)''
				newstring += "0D"
				newstring += "0A"
			# elif ')S" : MAKE-CALL("sip:" #1 =domain =dialPhone)' in line:
			# 	newstring += '"(988)" : MAKE-CALL(sip: #1 =domain =dialPhone)'
			# 	newstring += "0D"
			# 	newstring += "0A"
		#m.value = ""
		#print(newstring)
		m.value = newstring[:-2] #drop the last two bytes, which are a CRLF.
		t.value = m.encode()
		#m = t.getValue()
		#print(t.value)
cm.configFilePath += ".new" #rename so you don't overwrite the original file
#cm.encode()