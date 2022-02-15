from docsisTlvs import DocsisTlvs
#from mtaConfig import mtaConfig as cmConfig
from cmConfig import cmConfig
import sys 
import binascii

cm = cmConfig()
newCM = cmConfig()
cm.generateStringFromFile(sys.argv[1])
cm.tlvs = cm.parse()
newCM.configFilePath = cm.configFilePath + ".new"
for tlv in cm.tlvs:
	if tlv.tag != "11":
		newCM.tlvs.append(tlv)
	else:
		thisMIb = tlv.getValue()
		#thisMIb.decode(thisMIb.value)
		thisMIb.index = thisMIb.oid.split(".")[-1]
		thisMIb.oid = ".".join(thisMIb.oid.split(".")[:-1])
		print(thisMIb.oid)
		print(thisMIb.index)
		print(thisMIb.value)
		print("##############")
	