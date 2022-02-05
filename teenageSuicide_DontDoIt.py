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
	if t.tag =="64":
		newstring = ""
		m = t.getValue()
		print(m.dataType)
		for line in m.value.split('\n'):
			print("##### " + line + " #####")
			newstring += line 
			newstring + "\n"
			#if line == '"[2-8]11" : RETURN(#0)':
			#	newstring += '"988" : RETURN\n'
			#elif ')S" : MAKE-CALL("sip:" #1 =domain =dialPhone)' in line:
			#	newstring += '"(988)" : MAKE-CALL(sip: #1 =domain =dialPhone)\n'
		
		m.value = binascii.hexlify(newstring.encode()).decode('UTF-8')[:]
		print(m.value)
		t.setValue(m.encode())
cm.configFilePath += ".new"
cm.encode()