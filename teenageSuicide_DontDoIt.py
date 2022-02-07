from MTATlvs import MTATlvs
from mtaConfig import mtaConfig
import sys 
import binascii

cm = mtaConfig()
cm.generateStringFromFile(sys.argv[1])
cm.tags = MTATlvs
print(cm.tlv_string)
cm.tlvs = cm.parse(cm.tlv_string, cm.tags)

for t in cm.tlvs:
	t.getValue()
	#print(t.value)
	#oldvalue = ""
	if t.tag =="64":
		newstring = "0F"
		m = t.getValue()
		print(m.oid)
		print(m.dataType)
		oldvalue = m.value
		for line in m.value.split('\r\n'):
			print("##### " + line + " #####")
			newstring += binascii.hexlify(line.encode()).decode('UTF-8')#[:]
			newstring += "0D"
			newstring += "0A"
			#newstring + "\r\n"
			if line == '<10> "[2-8]11" : RETURN(#0)':
				newstring += '<10> "988" : RETURN'
				newstring += "0D"
				newstring += "0A"
			elif ')S" : MAKE-CALL("sip:" #1 =domain =dialPhone)' in line:
				newstring += '"(988)" : MAKE-CALL(sip: #1 =domain =dialPhone)'
				newstring += "0D"
				newstring += "0A"
		#m.value = ""
		print(newstring)
		m.value = newstring[:-2]
		#print("New Value")
		#print(m.value)
		#print("Old Value")
		#print(oldvalue)
		t.value = m.encode()
		m = t.getValue()
		#print(t.value)
cm.configFilePath += ".new"
#cm.encode()