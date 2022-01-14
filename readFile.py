import binascii
import codecs
import sys
from TLV import TLV
from docsisTlvs import DocsisTlvs
from MTATlvs import MTATlvs
from mib import mib
from mtaConfig import mtaConfig
from cmConfig import cmConfig

cm = cmConfig()
cm.generateStringFromFile(sys.argv[1])
if len(sys.argv) > 1:
    if sys.argv[2] == "MTA":
		cm.tags = MTATlvs
	#print(cm.tlv_string)
cm.tlvs = cm.parse(cm.tlv_string, cm.tags)
cm.encode()
print("########")
for t in cm.tlvs:
	if t.datatype in ["uchar", "uint", "ushort", "hexstr"]:
			bb = t.getValue()
			print(bb)

	else:
		if t.datatype not in  ["snmp_object", "aggregate"]:
			print("Write a decoder for " + t.datatype)