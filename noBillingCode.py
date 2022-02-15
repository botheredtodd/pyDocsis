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
		#print("Figure out if this mib has info you need to steal, and then steal it")
		#print("If this mib needs to be in the new config, build it from scratch with the new info, otherwise just move along")
		thisMIb = tlv.getValue()
		#thisMIb.decode(thisMIb.value)
		thisMIb.index = thisMIb.oid.split(".")[-1]
		#thisMIb.oid = ".".join(thisMIb.oid.split(".")[:-1])
		print(thisMIb.oid)
		print(thisMIb.index)
		print(thisMIb.value)
		print("##############")
		if thisMIb.oid.startswith("1.3.6.1.2.1.69.1.6.4.1"):
			if thisMIb.index in ["1", "10", "30"]:
				newCM.tlvs.append(tlv)
		elif thisMIb.oid.startswith("1.3.6.1.2.1.69.1.2.1"):
			if thisMIb.index in ["1", "2", "3", "4", "15"]:
				newCM.tlvs.append(tlv)
		elif thisMIb.oid.startswith("1.3.6.1.4.1.2082.5.1.1.1"):
			if thisMIb.index in ["0"]:
				newCM.tlvs.append(tlv)
#newCM.encode()