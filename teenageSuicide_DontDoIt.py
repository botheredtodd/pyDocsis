from MTATlvs import MTATlvs
from mtaConfig import mtaConfig
import sys 

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
		for line in m.value.split('\n'):
			print("##### " + line + " #####")
			newstring.append(line + "\n")
			