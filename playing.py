import os
from TLV import *
import binascii
import codecs

tlvs = {}
#file = open("docsis_symtable.h","r")
# for line in file:
# 	if line.startswith("{"):
# 		if True: #int(line.split(" ")[1][:-1]) < 256:
# 			new = str(hex(int(line.split(" ")[1][:-1])))[2:]
# 			if len(new) == 1:
# 				new = "0" + new
# 			if len(new) == 3:
# 				new = "0" + new
# 			tlvs.append(new)

tlvs["0b"] = "TLV 11 SnmpMibObject"
tlvs["3c"] = "tlv 60 UpstreamDropPacketClassification"
tlvs["ca"] = "tlv 202 eRouter"
tlvs["1d"] = "tlv 29 GlobalPrivacyEnable"
tlvs["11"] = "tlv 17 BaselinePrivacy"
tlvs["2b"] = "tlv 43 VendorSpecific"
tlvs["03"] = "tlv 3 NetworkAccess"
tlvs["12"] = "tlv 18 MaxCPE"
tlvs["21"] = "tlv 33 CoSignerCVCData"
tlvs["18"] = "tlv 24 UsServiceFlow"
tlvs["19"] = "tlv 25 DsServiceFlow"
tlvs["16"] = "tlv 22 UsPacketClass"
tlvs["17"] = "tlv 23 DsPacketClass"
tlvs["06"] = "TLV 6 CmMic"
tlvs["07"] = "TLV 7 CmtsMic"
tlvs["ff"] = "TLV 255 EndOfDataMkr"
tlvs["1c"] = "tlv28 MaxClassifiers"
tlvs["00"] = "TLV 0 Spacer"

#file.close()

tlv = TLV(tlvs)
f = open("cm.cfg", "rb")
content = f.read()
n = 2
bobbert = [binascii.hexlify(content).decode('UTF-8')[i:i+n] for i in range(0, len(binascii.hexlify(content).decode('UTF-8')), n)]
#print(bobbert)
#print(binascii.hexlify(content).decode('UTF-8'))
t = tlv.parse(binascii.hexlify(content).decode('UTF-8')[:])
for tt in t.keys():
	print(tlvs[str(tt)] + " : " + str(t[tt]))
	