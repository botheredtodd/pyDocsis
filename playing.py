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
f = open("sdcm.cfg", "rb")
content = f.read()
n = 2
bobbert = [binascii.hexlify(content).decode('UTF-8')[i:i+n] for i in range(0, len(binascii.hexlify(content).decode('UTF-8')), n)]
#print(bobbert)
#print(binascii.hexlify(content).decode('UTF-8'))
t = tlv.parse(binascii.hexlify(content).decode('UTF-8')[:])
for tt in t.keys():
	print(tlvs[str(tt)] + " : " + str(t[tt]))
	if str(tt) == "18":
		subts = {}
		subts["01"] = "24.1 UsServiceFlowRef"
		subts["06"] = "24.6 QosParamSetType"
		subts["07"] = "24.7 TrafficPriority"
		subts["08"] = "24.8 MaxRateSustained"
		subts["09"] = "24.9 MaxTrafficBurst"
		subts["0a"] = "24.10 MinReservedRate"
		subts["0b"] = "24.11 MinResPacketSize"
		subts["0c"] = "24.12 ActQosParamsTimeout"
		subts["0d"] = "24.13 AdmQosParamsTimeout"
		subts["0e"] = "24.14 MaxConcatenatedBurst"
		subts["0f"] = "24.15 SchedulingType"
		subts["10"] = "24.16 RequestOrTxPolicy"
		subts["11"] = "24.17 NominalPollInterval"
		subts["12"] = "24.18 ActQosParamsTimeout"
		subtvs = TLV(subts)
		st = subtvs.parse(t[tt])
		for stt in st.keys():
			print(subts[str(stt)] + " : " + str(st[stt]))
	elif str(tt) == "19":
		subts = {}
		subts["01"] = "25.1 DsServiceFlowRef"
		subts["04"] = "25.4 ServiceClassName"
		subts["06"] = "25.6 QosParamSetType"
		subts["07"] = "25.7 TrafficPriority"
		subts["08"] = "25.8 MaxRateSustained"
		subts["09"] = "25.9 MaxTrafficBurst"
		subts["0a"] = "25.10 MinReservedRate"
		subts["0b"] = "25.11 MinResPacketSize"
		subts["0c"] = "25.12 ActQosParamsTimeout"
		subts["0d"] = "25.13 AdmQosParamsTimeout"
		subts["0e"] = "25.14 MaxConcatenatedBurst"
		subts["0f"] = "25.15 SchedulingType"
		subts["10"] = "25.16 RequestOrTxPolicy"
		subts["11"] = "25.17 NominalPollInterval"
		subts["12"] = "25.18 ActQosParamsTimeout"
		subtvs = TLV(subts)
		st = subtvs.parse(t[tt])
		for stt in st.keys():
			print(subts[str(stt)] + " : " + str(st[stt]))
	elif str(tt) == "16":
		subts = {}
		subts["01"] = "22.1 ClassifierRef"
		subts["03"] = "22.3 ServiceFlowRef"
		subts["05"] = "25.5 RulePriority"
		subts["06"] = "22.6 ActivationState"
		subts["09"] = "22.9 IpPacketClassifier"
		# subts["0a"] = "25.10 MinReservedRate"
		# subts["0c"] = "25.12 ActQosParamsTimeout"
		# subts["0d"] = "25.13 AdmQosParamsTimeout"
		# subts["0e"] = "25.14 MaxConcatenatedBurst"
		# subts["0f"] = "25.15 SchedulingType"
		# subts["10"] = "25.16 RequestOrTxPolicy"
		# subts["11"] = "25.17 NominalPollInterval"
		# subts["12"] = "25.18 ActQosParamsTimeout"
		subtvs = TLV(subts)
		st = subtvs.parse(t[tt])
		for stt in st.keys():
			print(subts[str(stt)] + " : " + str(st[stt]))
			if str(stt) ==  "09":
				ssts = {}
				ssts["01"] = "22.9.1 IpTos"
				ssts["02"] = "22.9.2 IpProto"
				ssts["03"] = "22.9.3 IpSrcAddr"
				ssts["07"] = "22.9.7 SrcPortStart"
				ssts["08"] = "22.9.8 SrcPortEnd"
				ssts["09"] = "22.9.9 DstPortStart"
				ssts["0a"] = "22.9.10 DstPortEnd"
				ssubtvs = TLV(ssts)
				sst = ssubtvs.parse(st[stt])
				for sstt in sst.keys():
					print(ssts[str(sstt)] + " : " + str(sst[sstt]))
				
	elif str(tt) == "17":
		subts = {}
		subts["01"] = "23.1 ClassifierRef"
		subts["03"] = "23.3 ServiceFlowRef"
		subts["05"] = "23.5 RulePriority"
		subts["06"] = "23.6 ActivationState"
		subts["09"] = "23.9 IpPacketClassifier"
		# subts["0a"] = "25.10 MinReservedRate"
		# subts["0c"] = "25.12 ActQosParamsTimeout"
		# subts["0d"] = "25.13 AdmQosParamsTimeout"
		# subts["0e"] = "25.14 MaxConcatenatedBurst"
		# subts["0f"] = "25.15 SchedulingType"
		# subts["10"] = "25.16 RequestOrTxPolicy"
		# subts["11"] = "25.17 NominalPollInterval"
		# subts["12"] = "25.18 ActQosParamsTimeout"
		subtvs = TLV(subts)
		st = subtvs.parse(t[tt])
		for stt in st.keys():
			print(subts[str(stt)] + " : " + str(st[stt]))
			if str(stt) ==  "09":
				ssts = {}
				ssts["01"] = "23.9.1 IpTos"
				ssts["02"] = "23.9.2 IpProto"
				ssts["03"] = "23.9.3 IpSrcAddr"
				ssts["04"] = "23.9.4 IpSrcMask"
				ssts["07"] = "23.9.7 SrcPortStart"
				ssts["08"] = "23.9.8 SrcPortEnd"
				ssts["09"] = "23.9.9 DstPortStart"
				ssts["0a"] = "23.9.10 DstPortEnd"
				ssubtvs = TLV(ssts)
				sst = ssubtvs.parse(st[stt])
				for sstt in sst.keys():
					print(ssts[str(sstt)] + " : " + str(sst[sstt]))
				
	