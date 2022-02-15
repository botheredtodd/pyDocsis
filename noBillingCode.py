from docsisTlvs import DocsisTlvs
from cmConfig import cmConfig
import sys 
import binascii

cm = cmConfig()
cm.generateStringFromFile(sys.argv[1])
cm.tlvs = cm.parse(cm.tlv_string, cm.tags)
cm.configFilePath += ".new"
for tlv in cm.tlvs:
	if tlv.tag != "11":
		print(tlv.tag)
		print(tlv.value)
	#else:
		
	