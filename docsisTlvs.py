# For aesthetic reasons, the user is encouraged to put this in a database or something

DocsisTlvs = {}
DocsisTlvs["00"] = {}
DocsisTlvs["00"]["description"] = "/* Pad */"
DocsisTlvs["00"]["hex"] = "00"
DocsisTlvs["00"]["valueType"] = "00"
DocsisTlvs["00"]["subTlvs"] = []

DocsisTlvs["01"] = {}
DocsisTlvs["01"]["description"] = "DownstreamFrequency"
DocsisTlvs["01"]["hex"] = "01"
DocsisTlvs["01"]["valueType"] = "uint"
DocsisTlvs["01"]["subTlvs"] = []

DocsisTlvs["02"] = {}
DocsisTlvs["02"]["description"] = "UpstreamChannelId"
DocsisTlvs["02"]["hex"] = "02"
DocsisTlvs["02"]["valueType"] = "uchar"
DocsisTlvs["02"]["subTlvs"] = []

DocsisTlvs["03"] = {}
DocsisTlvs["03"]["description"] = "NetworkAccess"
DocsisTlvs["03"]["hex"] = "03"
DocsisTlvs["03"]["valueType"] = "uchar"
DocsisTlvs["03"]["subTlvs"] = []

DocsisTlvs["04"] = {}
DocsisTlvs["04"]["description"] = "ClassOfService"
DocsisTlvs["04"]["hex"] = "04"
DocsisTlvs["04"]["valueType"] = "s"
DocsisTlvs["04"]["subTlvs"] = []

DocsisTlvs["05"] = {}
DocsisTlvs["05"]["description"] = "ModemCapabilities"
DocsisTlvs["05"]["hex"] = "05"
DocsisTlvs["05"]["valueType"] = "s"
DocsisTlvs["05"]["subTlvs"] = []

DocsisTlvs["06"] = {}
DocsisTlvs["06"]["description"] = "CmMic"
DocsisTlvs["06"]["hex"] = "06"
DocsisTlvs["06"]["valueType"] = "00"
DocsisTlvs["06"]["subTlvs"] = []

DocsisTlvs["07"] = {}
DocsisTlvs["07"]["description"] = "CmtsMic"
DocsisTlvs["07"]["hex"] = "07"
DocsisTlvs["07"]["valueType"] = "00"
DocsisTlvs["07"]["subTlvs"] = []

DocsisTlvs["09"] = {}
DocsisTlvs["09"]["description"] = "SwUpgradeFilename"
DocsisTlvs["09"]["hex"] = "09"
DocsisTlvs["09"]["valueType"] = "string"
DocsisTlvs["09"]["subTlvs"] = []

DocsisTlvs["10"] = {}
DocsisTlvs["10"]["description"] = "SnmpWriteControl"
DocsisTlvs["10"]["hex"] = "0a"
DocsisTlvs["10"]["valueType"] = "00"
DocsisTlvs["10"]["subTlvs"] = []

DocsisTlvs["11"] = {}
DocsisTlvs["11"]["description"] = "SnmpMibObject"
DocsisTlvs["11"]["hex"] = "0b"
DocsisTlvs["11"]["valueType"] = "00"
DocsisTlvs["11"]["subTlvs"] = []

DocsisTlvs["12"] = {}
DocsisTlvs["12"]["description"] = "ModemIPAddress"
DocsisTlvs["12"]["hex"] = "0c"
DocsisTlvs["12"]["valueType"] = "ip"
DocsisTlvs["12"]["subTlvs"] = []

DocsisTlvs["14"] = {}
DocsisTlvs["14"]["description"] = "CpeMacAddress"
DocsisTlvs["14"]["hex"] = "0e"
DocsisTlvs["14"]["valueType"] = "ether"
DocsisTlvs["14"]["subTlvs"] = []

DocsisTlvs["17"] = {}
DocsisTlvs["17"]["description"] = "BaselinePrivacy"
DocsisTlvs["17"]["hex"] = "11"
DocsisTlvs["17"]["valueType"] = "s"
DocsisTlvs["17"]["subTlvs"] = []

DocsisTlvs["18"] = {}
DocsisTlvs["18"]["description"] = "MaxCPE"
DocsisTlvs["18"]["hex"] = "12"
DocsisTlvs["18"]["valueType"] = "uchar"
DocsisTlvs["18"]["subTlvs"] = []

DocsisTlvs["19"] = {}
DocsisTlvs["19"]["description"] = "TftpTimestamp"
DocsisTlvs["19"]["hex"] = "13"
DocsisTlvs["19"]["valueType"] = "uint"
DocsisTlvs["19"]["subTlvs"] = []

DocsisTlvs["20"] = {}
DocsisTlvs["20"]["description"] = "TftpModemAddress"
DocsisTlvs["20"]["hex"] = "14"
DocsisTlvs["20"]["valueType"] = "ip"
DocsisTlvs["20"]["subTlvs"] = []

DocsisTlvs["21"] = {}
DocsisTlvs["21"]["description"] = "SwUpgradeServer"
DocsisTlvs["21"]["hex"] = "15"
DocsisTlvs["21"]["valueType"] = "ip"
DocsisTlvs["21"]["subTlvs"] = []

DocsisTlvs["22"] = {}
DocsisTlvs["22"]["description"] = "UsPacketClass"
DocsisTlvs["22"]["hex"] = "16"
DocsisTlvs["22"]["valueType"] = "s"
DocsisTlvs["22"]["subTlvs"] = []

DocsisTlvs["23"] = {}
DocsisTlvs["23"]["description"] = "DsPacketClass"
DocsisTlvs["23"]["hex"] = "17"
DocsisTlvs["23"]["valueType"] = "s"
DocsisTlvs["23"]["subTlvs"] = []

DocsisTlvs["24"] = {}
DocsisTlvs["24"]["description"] = "UsServiceFlow"
DocsisTlvs["24"]["hex"] = "18"
DocsisTlvs["24"]["valueType"] = "s"
DocsisTlvs["24"]["subTlvs"] = []

DocsisTlvs["25"] = {}
DocsisTlvs["25"]["description"] = "DsServiceFlow"
DocsisTlvs["25"]["hex"] = "19"
DocsisTlvs["25"]["valueType"] = "s"
DocsisTlvs["25"]["subTlvs"] = []

DocsisTlvs["26"] = {}
DocsisTlvs["26"]["description"] = "PHS"
DocsisTlvs["26"]["hex"] = "1a"
DocsisTlvs["26"]["valueType"] = "s"
DocsisTlvs["26"]["subTlvs"] = []

DocsisTlvs["28"] = {}
DocsisTlvs["28"]["description"] = "MaxClassifiers"
DocsisTlvs["28"]["hex"] = "1c"
DocsisTlvs["28"]["valueType"] = "ushort"
DocsisTlvs["28"]["subTlvs"] = []

DocsisTlvs["29"] = {}
DocsisTlvs["29"]["description"] = "GlobalPrivacyEnable"
DocsisTlvs["29"]["hex"] = "1d"
DocsisTlvs["29"]["valueType"] = "uchar"
DocsisTlvs["29"]["subTlvs"] = []

DocsisTlvs["33"] = {}
DocsisTlvs["33"]["description"] = "CoSignerCVCData"
DocsisTlvs["33"]["hex"] = "21"
DocsisTlvs["33"]["valueType"] = "hexstr"
DocsisTlvs["33"]["subTlvs"] = []

DocsisTlvs["43"] = {}
DocsisTlvs["43"]["description"] = "VendorSpecific"
DocsisTlvs["43"]["hex"] = "2b"
DocsisTlvs["43"]["valueType"] = "s"
DocsisTlvs["43"]["subTlvs"] = []

DocsisTlvs["60"] = {}
DocsisTlvs["60"]["description"] = "UpstreamDropPacketClassification"
DocsisTlvs["60"]["hex"] = "3c"
DocsisTlvs["60"]["valueType"] = "s"
DocsisTlvs["60"]["subTlvs"] = []

DocsisTlvs["202"] = {}
DocsisTlvs["202"]["description"] = "eRouter"
DocsisTlvs["202"]["hex"] = "ca"
DocsisTlvs["202"]["valueType"] = "s"
DocsisTlvs["202"]["subTlvs"] = []

### tlv4
d4subs = {}

d4subs["01"] = {}
d4subs["01"]["description"] = "ClassID"
d4subs["01"]["hex"] = "01"
d4subs["01"]["valueType"] = "uchar"
d4subs["01"]["subTlvs"] = []

d4subs["02"] = {}
d4subs["02"]["description"] = "MaxRateDown"
d4subs["02"]["hex"] = "02"
d4subs["02"]["valueType"] = "uint"
d4subs["02"]["subTlvs"] = []

d4subs["03"] = {}
d4subs["03"]["description"] = "MaxRateUp"
d4subs["03"]["hex"] = "03"
d4subs["03"]["valueType"] = "uint"
d4subs["03"]["subTlvs"] = []

d4subs["04"] = {}
d4subs["04"]["description"] = "PriorityUp"
d4subs["04"]["hex"] = "04"
d4subs["04"]["valueType"] = "uchar"
d4subs["04"]["subTlvs"] = []

d4subs["05"] = {}
d4subs["05"]["description"] = "GuaranteedUp"
d4subs["05"]["hex"] = "05"
d4subs["05"]["valueType"] = "uint"
d4subs["05"]["subTlvs"] = []

d4subs["06"] = {}
d4subs["06"]["description"] = "MaxBurstUp"
d4subs["06"]["hex"] = "06"
d4subs["06"]["valueType"] = "ushort"
d4subs["06"]["subTlvs"] = []

d4subs["07"] = {}
d4subs["07"]["description"] = "PrivacyEnable"
d4subs["07"]["hex"] = "07"
d4subs["07"]["valueType"] = "uchar"
d4subs["07"]["subTlvs"] = []

DocsisTlvs["04"]["subTlvs"] = d4subs

### tlv5
d5subs = {}

d5subs["01"] = {}
d5subs["01"]["description"] = "ConcatenationSupport"
d5subs["01"]["hex"] = "01"
d5subs["01"]["valueType"] = "uchar"
d5subs["01"]["subTlvs"] = []

d5subs["02"] = {}
d5subs["02"]["description"] = "ModemDocsisVersion"
d5subs["02"]["hex"] = "02"
d5subs["02"]["valueType"] = "uchar"
d5subs["02"]["subTlvs"] = []

d5subs["03"] = {}
d5subs["03"]["description"] = "FragmentationSupport"
d5subs["03"]["hex"] = "03"
d5subs["03"]["valueType"] = "uchar"
d5subs["03"]["subTlvs"] = []

d5subs["04"] = {}
d5subs["04"]["description"] = "PHSSupport"
d5subs["04"]["hex"] = "04"
d5subs["04"]["valueType"] = "uchar"
d5subs["04"]["subTlvs"] = []

d5subs["05"] = {}
d5subs["05"]["description"] = "IGMPSupport"
d5subs["05"]["hex"] = "05"
d5subs["05"]["valueType"] = "uchar"
d5subs["05"]["subTlvs"] = []

d5subs["06"] = {}
d5subs["06"]["description"] = "BaselinePrivacySupport"
d5subs["06"]["hex"] = "06"
d5subs["06"]["valueType"] = "uchar"
d5subs["06"]["subTlvs"] = []

d5subs["07"] = {}
d5subs["07"]["description"] = "DownstreamSAIDSupport"
d5subs["07"]["hex"] = "07"
d5subs["07"]["valueType"] = "uchar"
d5subs["07"]["subTlvs"] = []

d5subs["08"] = {}
d5subs["08"]["description"] = "UpstreamSIDSupport"
d5subs["08"]["hex"] = "08"
d5subs["08"]["valueType"] = "uchar"
d5subs["08"]["subTlvs"] = []

d5subs["09"] = {}
d5subs["09"]["description"] = "OptionalFilteringSupport"
d5subs["09"]["hex"] = "09"
d5subs["09"]["valueType"] = "uchar"
d5subs["09"]["subTlvs"] = []

d5subs["10"] = {}
d5subs["10"]["description"] = "TransmitPreEqualizerTapsPerModulationInterval"
d5subs["10"]["hex"] = "0a"
d5subs["10"]["valueType"] = "uchar"
d5subs["10"]["subTlvs"] = []

d5subs["11"] = {}
d5subs["11"]["description"] = "NumberofTransmitEqualizerTaps"
d5subs["11"]["hex"] = "0b"
d5subs["11"]["valueType"] = "uchar"
d5subs["11"]["subTlvs"] = []

d5subs["12"] = {}
d5subs["12"]["description"] = "DCCSupport"
d5subs["12"]["hex"] = "0c"
d5subs["12"]["valueType"] = "uint"
d5subs["12"]["subTlvs"] = []

d5subs["13"] = {}
d5subs["13"]["description"] = "IPFiltersSupport"
d5subs["13"]["hex"] = "0d"
d5subs["13"]["valueType"] = "ushort"
d5subs["13"]["subTlvs"] = []

d5subs["14"] = {}
d5subs["14"]["description"] = "LLCFiltersSupport"
d5subs["14"]["hex"] = "0e"
d5subs["14"]["valueType"] = "ushort"
d5subs["14"]["subTlvs"] = []

d5subs["15"] = {}
d5subs["15"]["description"] = "ExpandedUnicastSIDSpace"
d5subs["15"]["hex"] = "0f"
d5subs["15"]["valueType"] = "uchar"
d5subs["15"]["subTlvs"] = []

d5subs["16"] = {}
d5subs["16"]["description"] = "RangingHoldOffSupport"
d5subs["16"]["hex"] = "10"
d5subs["16"]["valueType"] = "hexstr"
d5subs["16"]["subTlvs"] = []

d5subs["17"] = {}
d5subs["17"]["description"] = "L2VPNCapability"
d5subs["17"]["hex"] = "11"
d5subs["17"]["valueType"] = "uchar"
d5subs["17"]["subTlvs"] = []

d5subs["18"] = {}
d5subs["18"]["description"] = "L2VPNeSAFEHostCapability"
d5subs["18"]["hex"] = "12"
d5subs["18"]["valueType"] = "hexstr"
d5subs["18"]["subTlvs"] = []

d5subs["19"] = {}
d5subs["19"]["description"] = "DUTFilteringSupport"
d5subs["19"]["hex"] = "13"
d5subs["19"]["valueType"] = "uchar"
d5subs["19"]["subTlvs"] = []

d5subs["20"] = {}
d5subs["20"]["description"] = "UpstreamFrequencyRangeSupport"
d5subs["20"]["hex"] = "14"
d5subs["20"]["valueType"] = "uchar"
d5subs["20"]["subTlvs"] = []

d5subs["21"] = {}
d5subs["21"]["description"] = "UpstreamSymbolRateSupport"
d5subs["21"]["hex"] = "15"
d5subs["21"]["valueType"] = "uchar"
d5subs["21"]["subTlvs"] = []
#todo: keep going from here
d5subs["22"] = {}
d5subs["22"]["description"] = "SelectableActiveCodeMode2Support"
d5subs["22"]["hex"] = "01"
d5subs["22"]["valueType"] = "uchar"
d5subs["22"]["subTlvs"] = []

d5subs["23"] = {}
d5subs["23"]["description"] = "CodeHoppingMode2Support"
d5subs["23"]["hex"] = "02"
d5subs["23"]["valueType"] = "uchar"
d5subs["23"]["subTlvs"] = []

d5subs["24"] = {}
d5subs["24"]["description"] = "MultipleTransmitChannelSupport"
d5subs["24"]["hex"] = "03"
d5subs["24"]["valueType"] = "uchar"
d5subs["24"]["subTlvs"] = []

d5subs["25"] = {}
d5subs["25"]["description"] = "M512MspsUpstreamTransmitChannel"
d5subs["25"]["hex"] = "04"
d5subs["25"]["valueType"] = "uchar"
d5subs["25"]["subTlvs"] = []

d5subs["26"] = {}
d5subs["26"]["description"] = "M256MspsUpstreamTransmitChannel"
d5subs["26"]["hex"] = "05"
d5subs["26"]["valueType"] = "uchar"
d5subs["26"]["subTlvs"] = []

d5subs["27"] = {}
d5subs["27"]["description"] = "TotalSIDClusterSupport"
d5subs["27"]["hex"] = "06"
d5subs["27"]["valueType"] = "uchar"
d5subs["27"]["subTlvs"] = []

d5subs["28"] = {}
d5subs["28"]["description"] = "SIDClustersPerServiceFlow"
d5subs["28"]["hex"] = "07"
d5subs["28"]["valueType"] = "uchar"
d5subs["28"]["subTlvs"] = []

d5subs["29"] = {}
d5subs["29"]["description"] = "MultipleReceiveChannelSupport"
d5subs["29"]["hex"] = "01"
d5subs["29"]["valueType"] = "uchar"
d5subs["29"]["subTlvs"] = []

d5subs["30"] = {}
d5subs["30"]["description"] = "TotalDownstreamServiceIDSupport"
d5subs["30"]["hex"] = "02"
d5subs["30"]["valueType"] = "uchar"
d5subs["30"]["subTlvs"] = []

d5subs["31"] = {}
d5subs["31"]["description"] = "ResequencingDownstreamServiceID"
d5subs["31"]["hex"] = "03"
d5subs["31"]["valueType"] = "uchar"
d5subs["31"]["subTlvs"] = []

d5subs["32"] = {}
d5subs["32"]["description"] = "MulticastDownstreamServiceID"
d5subs["32"]["hex"] = "04"
d5subs["32"]["valueType"] = "uchar"
d5subs["32"]["subTlvs"] = []

d5subs["33"] = {}
d5subs["33"]["description"] = "MulticastDSIDForwarding"
d5subs["33"]["hex"] = "05"
d5subs["33"]["valueType"] = "uchar"
d5subs["33"]["subTlvs"] = []

d5subs["34"] = {}
d5subs["34"]["description"] = "FrameControlTypeForwarding"
d5subs["34"]["hex"] = "06"
d5subs["34"]["valueType"] = "uchar"
d5subs["34"]["subTlvs"] = []

d5subs["35"] = {}
d5subs["35"]["description"] = "DPVCapability"
d5subs["35"]["hex"] = "07"
d5subs["35"]["valueType"] = "uchar"
d5subs["35"]["subTlvs"] = []

d5subs["36"] = {}
d5subs["36"]["description"] = "UnsolicitedGrantServiceSupport"
d5subs["36"]["hex"] = "01"
d5subs["36"]["valueType"] = "uchar"
d5subs["36"]["subTlvs"] = []

d5subs["37"] = {}
d5subs["37"]["description"] = "MAPandUCDReceiptSupport"
d5subs["37"]["hex"] = "02"
d5subs["37"]["valueType"] = "uchar"
d5subs["37"]["subTlvs"] = []

d5subs["38"] = {}
d5subs["38"]["description"] = "UpstreamDropClassifierSupport"
d5subs["38"]["hex"] = "03"
d5subs["38"]["valueType"] = "ushort"
d5subs["38"]["subTlvs"] = []

d5subs["39"] = {}
d5subs["39"]["description"] = "IPv6Support"
d5subs["39"]["hex"] = "04"
d5subs["39"]["valueType"] = "uchar"
d5subs["39"]["subTlvs"] = []

d5subs["40"] = {}
d5subs["40"]["description"] = "ExtendedUpstreamTransmitPower"
d5subs["40"]["hex"] = "05"
d5subs["40"]["valueType"] = "uchar"
d5subs["40"]["subTlvs"] = []

d5subs["41"] = {}
d5subs["41"]["description"] = "MPLSClassificationSupport"
d5subs["41"]["hex"] = "06"
d5subs["41"]["valueType"] = "hexstr"
d5subs["41"]["subTlvs"] = []

d5subs["42"] = {}
d5subs["42"]["description"] = "DONUCapabilitiesEncoding"
d5subs["42"]["hex"] = "07"
d5subs["42"]["valueType"] = "hexstr"
d5subs["42"]["subTlvs"] = []

d5subs["44"] = {}
d5subs["44"]["description"] = "EnergyManagementCapabilities"
d5subs["44"]["hex"] = "05"
d5subs["44"]["valueType"] = "hexstr"
d5subs["44"]["subTlvs"] = []

d5subs["45"] = {}
d5subs["45"]["description"] = "CDOCSISCapabilityEncoding"
d5subs["45"]["hex"] = "06"
d5subs["45"]["valueType"] = "hexstr"
d5subs["45"]["subTlvs"] = []

d5subs["46"] = {}
d5subs["46"]["description"] = "CMSTATUSACK"
d5subs["46"]["hex"] = "07"
d5subs["46"]["valueType"] = "uchar"
d5subs["46"]["subTlvs"] = []

DocsisTlvs["05"]["subTlvs"] = d5subs

d17subs = {}
DocsisTlvs["17"]["subTlvs"] = d17subs

d22subs = {}
d22subs["01"] = "22.1 ClassifierRef"
d22subs["03"] = "22.3 ServiceFlowRef"
d22subs["05"] = "25.5 RulePriority"
d22subs["06"] = "22.6 ActivationState"
d22subs["09"] = "22.9 IpPacketClassifier"
d22_9subs = {}
d22_9subs["01"] = "22.9.1 IpTos"
d22_9subs["02"] = "22.9.2 IpProto"
d22_9subs["03"] = "22.9.3 IpSrcAddr"
d22_9subs["07"] = "22.9.7 SrcPortStart"
d22_9subs["08"] = "22.9.8 SrcPortEnd"
d22_9subs["09"] = "22.9.9 DstPortStart"
d22_9subs["0a"] = "22.9.10 DstPortEnd"
d22subs["09"]["subTlvs"] = d22_9subs
DocsisTlvs["22"]["subTlvs"] = d22subs

d23subs = {}
d23subs["01"] = "23.1 ClassifierRef"
d23subs["03"] = "23.3 ServiceFlowRef"
d23subs["05"] = "23.5 RulePriority"
d23subs["06"] = "23.6 ActivationState"
d23subs["09"] = "23.9 IpPacketClassifier"
d23_9subs["01"] = "23.9.1 IpTos"
d23_9subs["02"] = "23.9.2 IpProto"
d23_9subs["03"] = "23.9.3 IpSrcAddr"
d23_9subs["04"] = "23.9.4 IpSrcMask"
d23_9subs["07"] = "23.9.7 SrcPortStart"
d23_9subs["08"] = "23.9.8 SrcPortEnd"
d23_9subs["09"] = "23.9.9 DstPortStart"
d23_9subs["0a"] = "23.9.10 DstPortEnd"
d23subs["09"]["subTlvs"] = d23_9subs
DocsisTlvs["23"]["subTlvs"] = d23subs

d24subs = {}
d24subs["01"] = "24.1 UsServiceFlowRef"
d24subs["06"] = "24.6 QosParamSetType"
d24subs["07"] = "24.7 TrafficPriority"
d24subs["08"] = "24.8 MaxRateSustained"
d24subs["09"] = "24.9 MaxTrafficBurst"
d24subs["0a"] = "24.10 MinReservedRate"
d24subs["0b"] = "24.11 MinResPacketSize"
d24subs["0c"] = "24.12 ActQosParamsTimeout"
d24subs["0d"] = "24.13 AdmQosParamsTimeout"
d24subs["0e"] = "24.14 MaxConcatenatedBurst"
d24subs["0f"] = "24.15 SchedulingType"
d24subs["10"] = "24.16 RequestOrTxPolicy"
d24subs["11"] = "24.17 NominalPollInterval"
d24subs["12"] = "24.18 ActQosParamsTimeout"
DocsisTlvs["24"]["subTlvs"] = d24subs

d25subs = {}
d25subs["01"] = "24.1 UsServiceFlowRef"
d25subs["06"] = "24.6 QosParamSetType"
d25subs["07"] = "24.7 TrafficPriority"
d25subs["08"] = "24.8 MaxRateSustained"
d25subs["09"] = "24.9 MaxTrafficBurst"
d25subs["0a"] = "24.10 MinReservedRate"
d25subs["0b"] = "24.11 MinResPacketSize"
d25subs["0c"] = "24.12 ActQosParamsTimeout"
d25subs["0d"] = "24.13 AdmQosParamsTimeout"
d25subs["0e"] = "24.14 MaxConcatenatedBurst"
d25subs["0f"] = "24.15 SchedulingType"
d25subs["10"] = "24.16 RequestOrTxPolicy"
d25subs["11"] = "24.17 NominalPollInterval"
d25subs["12"] = "24.18 ActQosParamsTimeout"
DocsisTlvs["25"]["subTlvs"] = d25subs