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
		print("Figure out if this mib has info you need to steal, and then steal it")
		print("If this mib needs to be in the new config, build it from scratch with the new info, otherwise just move along")
		thisMIb = tlv.getValue()
		#thisMIb.decode(thisMIb.value)
		thisMIb.index = thisMIb.oid.split(".")[-1]
		thisMIb.oid = ".".join(thisMIb.oid.split(".")[:-1])
		print(thisMIb.oid)
		print(thisMIb.index)
		print(thisMIb.value)
		print("##############")
	