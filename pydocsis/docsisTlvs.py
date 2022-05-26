# For aesthetic reasons, the user is encouraged to put this in a database or something

DocsisTlvs = {}

DocsisTlvs["00"] = {}
DocsisTlvs["00"]["description"] = "/* Pad */"
DocsisTlvs["00"]["hex"] = "00"
DocsisTlvs["00"]["datatype"] = "special"
DocsisTlvs["00"]["subTlvs"] = {}

DocsisTlvs["01"] = {}
DocsisTlvs["01"]["description"] = "DownstreamFrequency"
DocsisTlvs["01"]["hex"] = "01"
DocsisTlvs["01"]["datatype"] = "uint"
DocsisTlvs["01"]["subTlvs"] = {}

DocsisTlvs["02"] = {}
DocsisTlvs["02"]["description"] = "UpstreamChannelId"
DocsisTlvs["02"]["hex"] = "02"
DocsisTlvs["02"]["datatype"] = "uchar"
DocsisTlvs["02"]["subTlvs"] = {}

DocsisTlvs["03"] = {}
DocsisTlvs["03"]["description"] = "NetworkAccess"
DocsisTlvs["03"]["hex"] = "03"
DocsisTlvs["03"]["datatype"] = "uchar"
DocsisTlvs["03"]["subTlvs"] = {}

DocsisTlvs["04"] = {}
DocsisTlvs["04"]["description"] = "ClassOfService"
DocsisTlvs["04"]["hex"] = "04"
DocsisTlvs["04"]["datatype"] = "aggregate"
DocsisTlvs["04"]["subTlvs"] = {}

DocsisTlvs["04"]["subTlvs"]["01"] = {}
DocsisTlvs["04"]["subTlvs"]["01"]["description"] = "ClassID"
DocsisTlvs["04"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["04"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["04"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["04"]["subTlvs"]["02"] = {}
DocsisTlvs["04"]["subTlvs"]["02"]["description"] = "MaxRateDown"
DocsisTlvs["04"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["04"]["subTlvs"]["02"]["datatype"] = "uint"
DocsisTlvs["04"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["04"]["subTlvs"]["03"] = {}
DocsisTlvs["04"]["subTlvs"]["03"]["description"] = "MaxRateUp"
DocsisTlvs["04"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["04"]["subTlvs"]["03"]["datatype"] = "uint"
DocsisTlvs["04"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["04"]["subTlvs"]["04"] = {}
DocsisTlvs["04"]["subTlvs"]["04"]["description"] = "PriorityUp"
DocsisTlvs["04"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["04"]["subTlvs"]["04"]["datatype"] = "uchar"
DocsisTlvs["04"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["04"]["subTlvs"]["05"] = {}
DocsisTlvs["04"]["subTlvs"]["05"]["description"] = "GuaranteedUp"
DocsisTlvs["04"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["04"]["subTlvs"]["05"]["datatype"] = "uint"
DocsisTlvs["04"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["04"]["subTlvs"]["06"] = {}
DocsisTlvs["04"]["subTlvs"]["06"]["description"] = "MaxBurstUp"
DocsisTlvs["04"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["04"]["subTlvs"]["06"]["datatype"] = "ushort"
DocsisTlvs["04"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["04"]["subTlvs"]["07"] = {}
DocsisTlvs["04"]["subTlvs"]["07"]["description"] = "PrivacyEnable"
DocsisTlvs["04"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["04"]["subTlvs"]["07"]["datatype"] = "uchar"
DocsisTlvs["04"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["04"]["subTlvs"]["15"] = {}
DocsisTlvs["04"]["subTlvs"]["15"]["description"] = "Technicolor thing"
DocsisTlvs["04"]["subTlvs"]["15"]["hex"] = "0f"
DocsisTlvs["04"]["subTlvs"]["15"]["datatype"] = "unknown"
DocsisTlvs["04"]["subTlvs"]["15"]["subTlvs"] = {}

DocsisTlvs["04"]["subTlvs"]["61"] = {}
DocsisTlvs["04"]["subTlvs"]["61"]["description"] = "Technicolor thing"
DocsisTlvs["04"]["subTlvs"]["61"]["hex"] = "3d"
DocsisTlvs["04"]["subTlvs"]["61"]["datatype"] = "unknown"
DocsisTlvs["04"]["subTlvs"]["61"]["subTlvs"] = {}

DocsisTlvs["04"]["subTlvs"]["103"] = {}
DocsisTlvs["04"]["subTlvs"]["103"]["description"] = "Technicolor thing"
DocsisTlvs["04"]["subTlvs"]["103"]["hex"] = "67"
DocsisTlvs["04"]["subTlvs"]["103"]["datatype"] = "unknown"
DocsisTlvs["04"]["subTlvs"]["103"]["subTlvs"] = {}

DocsisTlvs["05"] = {}
DocsisTlvs["05"]["description"] = "ModemCapabilities"
DocsisTlvs["05"]["hex"] = "05"
DocsisTlvs["05"]["datatype"] = "aggregate"
DocsisTlvs["05"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["01"] = {}
DocsisTlvs["05"]["subTlvs"]["01"]["description"] = "ConcatenationSupport"
DocsisTlvs["05"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["05"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["05"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["02"] = {}
DocsisTlvs["05"]["subTlvs"]["02"]["description"] = "ModemDocsisVersion"
DocsisTlvs["05"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["05"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["05"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["03"] = {}
DocsisTlvs["05"]["subTlvs"]["03"]["description"] = "FragmentationSupport"
DocsisTlvs["05"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["05"]["subTlvs"]["03"]["datatype"] = "uchar"
DocsisTlvs["05"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["04"] = {}
DocsisTlvs["05"]["subTlvs"]["04"]["description"] = "PHSSupport"
DocsisTlvs["05"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["05"]["subTlvs"]["04"]["datatype"] = "uchar"
DocsisTlvs["05"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["05"] = {}
DocsisTlvs["05"]["subTlvs"]["05"]["description"] = "IGMPSupport"
DocsisTlvs["05"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["05"]["subTlvs"]["05"]["datatype"] = "uchar"
DocsisTlvs["05"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["06"] = {}
DocsisTlvs["05"]["subTlvs"]["06"]["description"] = "BaselinePrivacySupport"
DocsisTlvs["05"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["05"]["subTlvs"]["06"]["datatype"] = "uchar"
DocsisTlvs["05"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["07"] = {}
DocsisTlvs["05"]["subTlvs"]["07"]["description"] = "DownstreamSAIDSupport"
DocsisTlvs["05"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["05"]["subTlvs"]["07"]["datatype"] = "uchar"
DocsisTlvs["05"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["08"] = {}
DocsisTlvs["05"]["subTlvs"]["08"]["description"] = "UpstreamSIDSupport"
DocsisTlvs["05"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["05"]["subTlvs"]["08"]["datatype"] = "uchar"
DocsisTlvs["05"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["09"] = {}
DocsisTlvs["05"]["subTlvs"]["09"]["description"] = "OptionalFilteringSupport"
DocsisTlvs["05"]["subTlvs"]["09"]["hex"] = "09"
DocsisTlvs["05"]["subTlvs"]["09"]["datatype"] = "uchar"
DocsisTlvs["05"]["subTlvs"]["09"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["10"] = {}
DocsisTlvs["05"]["subTlvs"]["10"]["description"] = "TransmitPreEqualizerTapsPerModulationInterval"
DocsisTlvs["05"]["subTlvs"]["10"]["hex"] = "0a"
DocsisTlvs["05"]["subTlvs"]["10"]["datatype"] = "uchar"
DocsisTlvs["05"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["11"] = {}
DocsisTlvs["05"]["subTlvs"]["11"]["description"] = "NumberofTransmitEqualizerTaps"
DocsisTlvs["05"]["subTlvs"]["11"]["hex"] = "0b"
DocsisTlvs["05"]["subTlvs"]["11"]["datatype"] = "uchar"
DocsisTlvs["05"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["12"] = {}
DocsisTlvs["05"]["subTlvs"]["12"]["description"] = "DCCSupport"
DocsisTlvs["05"]["subTlvs"]["12"]["hex"] = "0c"
DocsisTlvs["05"]["subTlvs"]["12"]["datatype"] = "uchar"
DocsisTlvs["05"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["13"] = {}
DocsisTlvs["05"]["subTlvs"]["13"]["description"] = "IPFiltersSupport"
DocsisTlvs["05"]["subTlvs"]["13"]["hex"] = "0d"
DocsisTlvs["05"]["subTlvs"]["13"]["datatype"] = "ushort"
DocsisTlvs["05"]["subTlvs"]["13"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["14"] = {}
DocsisTlvs["05"]["subTlvs"]["14"]["description"] = "LLCFiltersSupport"
DocsisTlvs["05"]["subTlvs"]["14"]["hex"] = "0e"
DocsisTlvs["05"]["subTlvs"]["14"]["datatype"] = "ushort"
DocsisTlvs["05"]["subTlvs"]["14"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["15"] = {}
DocsisTlvs["05"]["subTlvs"]["15"]["description"] = "ExpandedUnicastSIDSpace"
DocsisTlvs["05"]["subTlvs"]["15"]["hex"] = "0f"
DocsisTlvs["05"]["subTlvs"]["15"]["datatype"] = "uchar"
DocsisTlvs["05"]["subTlvs"]["15"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["16"] = {}
DocsisTlvs["05"]["subTlvs"]["16"]["description"] = "RangingHoldOffSupport"
DocsisTlvs["05"]["subTlvs"]["16"]["hex"] = "10"
DocsisTlvs["05"]["subTlvs"]["16"]["datatype"] = "hexstr"
DocsisTlvs["05"]["subTlvs"]["16"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["17"] = {}
DocsisTlvs["05"]["subTlvs"]["17"]["description"] = "L2VPNCapability"
DocsisTlvs["05"]["subTlvs"]["17"]["hex"] = "11"
DocsisTlvs["05"]["subTlvs"]["17"]["datatype"] = "uchar"
DocsisTlvs["05"]["subTlvs"]["17"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["18"] = {}
DocsisTlvs["05"]["subTlvs"]["18"]["description"] = "L2VPNeSAFEHostCapability"
DocsisTlvs["05"]["subTlvs"]["18"]["hex"] = "12"
DocsisTlvs["05"]["subTlvs"]["18"]["datatype"] = "hexstr"
DocsisTlvs["05"]["subTlvs"]["18"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["19"] = {}
DocsisTlvs["05"]["subTlvs"]["19"]["description"] = "DUTFilteringSupport"
DocsisTlvs["05"]["subTlvs"]["19"]["hex"] = "13"
DocsisTlvs["05"]["subTlvs"]["19"]["datatype"] = "uchar"
DocsisTlvs["05"]["subTlvs"]["19"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["20"] = {}
DocsisTlvs["05"]["subTlvs"]["20"]["description"] = "UpstreamFrequencyRangeSupport"
DocsisTlvs["05"]["subTlvs"]["20"]["hex"] = "14"
DocsisTlvs["05"]["subTlvs"]["20"]["datatype"] = "uchar"
DocsisTlvs["05"]["subTlvs"]["20"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["21"] = {}
DocsisTlvs["05"]["subTlvs"]["21"]["description"] = "UpstreamSymbolRateSupport"
DocsisTlvs["05"]["subTlvs"]["21"]["hex"] = "15"
DocsisTlvs["05"]["subTlvs"]["21"]["datatype"] = "uchar"
DocsisTlvs["05"]["subTlvs"]["21"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["22"] = {}
DocsisTlvs["05"]["subTlvs"]["22"]["description"] = "SelectableActiveCodeMode2Support"
DocsisTlvs["05"]["subTlvs"]["22"]["hex"] = "16"
DocsisTlvs["05"]["subTlvs"]["22"]["datatype"] = "uchar"
DocsisTlvs["05"]["subTlvs"]["22"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["23"] = {}
DocsisTlvs["05"]["subTlvs"]["23"]["description"] = "CodeHoppingMode2Support"
DocsisTlvs["05"]["subTlvs"]["23"]["hex"] = "17"
DocsisTlvs["05"]["subTlvs"]["23"]["datatype"] = "uchar"
DocsisTlvs["05"]["subTlvs"]["23"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["24"] = {}
DocsisTlvs["05"]["subTlvs"]["24"]["description"] = "MultipleTransmitChannelSupport"
DocsisTlvs["05"]["subTlvs"]["24"]["hex"] = "18"
DocsisTlvs["05"]["subTlvs"]["24"]["datatype"] = "uchar"
DocsisTlvs["05"]["subTlvs"]["24"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["25"] = {}
DocsisTlvs["05"]["subTlvs"]["25"]["description"] = "M512MspsUpstreamTransmitChannel"
DocsisTlvs["05"]["subTlvs"]["25"]["hex"] = "19"
DocsisTlvs["05"]["subTlvs"]["25"]["datatype"] = "uchar"
DocsisTlvs["05"]["subTlvs"]["25"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["26"] = {}
DocsisTlvs["05"]["subTlvs"]["26"]["description"] = "M256MspsUpstreamTransmitChannel"
DocsisTlvs["05"]["subTlvs"]["26"]["hex"] = "1a"
DocsisTlvs["05"]["subTlvs"]["26"]["datatype"] = "uchar"
DocsisTlvs["05"]["subTlvs"]["26"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["27"] = {}
DocsisTlvs["05"]["subTlvs"]["27"]["description"] = "TotalSIDClusterSupport"
DocsisTlvs["05"]["subTlvs"]["27"]["hex"] = "1b"
DocsisTlvs["05"]["subTlvs"]["27"]["datatype"] = "uchar"
DocsisTlvs["05"]["subTlvs"]["27"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["28"] = {}
DocsisTlvs["05"]["subTlvs"]["28"]["description"] = "SIDClustersPerServiceFlow"
DocsisTlvs["05"]["subTlvs"]["28"]["hex"] = "1c"
DocsisTlvs["05"]["subTlvs"]["28"]["datatype"] = "uchar"
DocsisTlvs["05"]["subTlvs"]["28"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["29"] = {}
DocsisTlvs["05"]["subTlvs"]["29"]["description"] = "MultipleReceiveChannelSupport"
DocsisTlvs["05"]["subTlvs"]["29"]["hex"] = "1d"
DocsisTlvs["05"]["subTlvs"]["29"]["datatype"] = "uchar"
DocsisTlvs["05"]["subTlvs"]["29"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["30"] = {}
DocsisTlvs["05"]["subTlvs"]["30"]["description"] = "TotalDownstreamServiceIDSupport"
DocsisTlvs["05"]["subTlvs"]["30"]["hex"] = "1e"
DocsisTlvs["05"]["subTlvs"]["30"]["datatype"] = "uchar"
DocsisTlvs["05"]["subTlvs"]["30"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["31"] = {}
DocsisTlvs["05"]["subTlvs"]["31"]["description"] = "ResequencingDownstreamServiceID"
DocsisTlvs["05"]["subTlvs"]["31"]["hex"] = "1f"
DocsisTlvs["05"]["subTlvs"]["31"]["datatype"] = "uchar"
DocsisTlvs["05"]["subTlvs"]["31"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["32"] = {}
DocsisTlvs["05"]["subTlvs"]["32"]["description"] = "MulticastDownstreamServiceID"
DocsisTlvs["05"]["subTlvs"]["32"]["hex"] = "20"
DocsisTlvs["05"]["subTlvs"]["32"]["datatype"] = "uchar"
DocsisTlvs["05"]["subTlvs"]["32"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["33"] = {}
DocsisTlvs["05"]["subTlvs"]["33"]["description"] = "MulticastDSIDForwarding"
DocsisTlvs["05"]["subTlvs"]["33"]["hex"] = "21"
DocsisTlvs["05"]["subTlvs"]["33"]["datatype"] = "uchar"
DocsisTlvs["05"]["subTlvs"]["33"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["34"] = {}
DocsisTlvs["05"]["subTlvs"]["34"]["description"] = "FrameControlTypeForwarding"
DocsisTlvs["05"]["subTlvs"]["34"]["hex"] = "22"
DocsisTlvs["05"]["subTlvs"]["34"]["datatype"] = "uchar"
DocsisTlvs["05"]["subTlvs"]["34"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["35"] = {}
DocsisTlvs["05"]["subTlvs"]["35"]["description"] = "DPVCapability"
DocsisTlvs["05"]["subTlvs"]["35"]["hex"] = "23"
DocsisTlvs["05"]["subTlvs"]["35"]["datatype"] = "uchar"
DocsisTlvs["05"]["subTlvs"]["35"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["36"] = {}
DocsisTlvs["05"]["subTlvs"]["36"]["description"] = "UnsolicitedGrantServiceSupport"
DocsisTlvs["05"]["subTlvs"]["36"]["hex"] = "24"
DocsisTlvs["05"]["subTlvs"]["36"]["datatype"] = "uchar"
DocsisTlvs["05"]["subTlvs"]["36"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["37"] = {}
DocsisTlvs["05"]["subTlvs"]["37"]["description"] = "MAPandUCDReceiptSupport"
DocsisTlvs["05"]["subTlvs"]["37"]["hex"] = "25"
DocsisTlvs["05"]["subTlvs"]["37"]["datatype"] = "uchar"
DocsisTlvs["05"]["subTlvs"]["37"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["38"] = {}
DocsisTlvs["05"]["subTlvs"]["38"]["description"] = "UpstreamDropClassifierSupport"
DocsisTlvs["05"]["subTlvs"]["38"]["hex"] = "26"
DocsisTlvs["05"]["subTlvs"]["38"]["datatype"] = "ushort"
DocsisTlvs["05"]["subTlvs"]["38"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["39"] = {}
DocsisTlvs["05"]["subTlvs"]["39"]["description"] = "IPv6Support"
DocsisTlvs["05"]["subTlvs"]["39"]["hex"] = "27"
DocsisTlvs["05"]["subTlvs"]["39"]["datatype"] = "uchar"
DocsisTlvs["05"]["subTlvs"]["39"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["40"] = {}
DocsisTlvs["05"]["subTlvs"]["40"]["description"] = "ExtendedUpstreamTransmitPower"
DocsisTlvs["05"]["subTlvs"]["40"]["hex"] = "28"
DocsisTlvs["05"]["subTlvs"]["40"]["datatype"] = "uchar"
DocsisTlvs["05"]["subTlvs"]["40"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["41"] = {}
DocsisTlvs["05"]["subTlvs"]["41"]["description"] = "MPLSClassificationSupport"
DocsisTlvs["05"]["subTlvs"]["41"]["hex"] = "29"
DocsisTlvs["05"]["subTlvs"]["41"]["datatype"] = "hexstr"
DocsisTlvs["05"]["subTlvs"]["41"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["42"] = {}
DocsisTlvs["05"]["subTlvs"]["42"]["description"] = "DONUCapabilitiesEncoding"
DocsisTlvs["05"]["subTlvs"]["42"]["hex"] = "2a"
DocsisTlvs["05"]["subTlvs"]["42"]["datatype"] = "hexstr"
DocsisTlvs["05"]["subTlvs"]["42"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["44"] = {}
DocsisTlvs["05"]["subTlvs"]["44"]["description"] = "EnergyManagementCapabilities"
DocsisTlvs["05"]["subTlvs"]["44"]["hex"] = "2c"
DocsisTlvs["05"]["subTlvs"]["44"]["datatype"] = "hexstr"
DocsisTlvs["05"]["subTlvs"]["44"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["45"] = {}
DocsisTlvs["05"]["subTlvs"]["45"]["description"] = "CDOCSISCapabilityEncoding"
DocsisTlvs["05"]["subTlvs"]["45"]["hex"] = "2d"
DocsisTlvs["05"]["subTlvs"]["45"]["datatype"] = "hexstr"
DocsisTlvs["05"]["subTlvs"]["45"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["46"] = {}
DocsisTlvs["05"]["subTlvs"]["46"]["description"] = "CMSTATUSACK"
DocsisTlvs["05"]["subTlvs"]["46"]["hex"] = "2e"
DocsisTlvs["05"]["subTlvs"]["46"]["datatype"] = "uchar"
DocsisTlvs["05"]["subTlvs"]["46"]["subTlvs"] = {}

DocsisTlvs["06"] = {}
DocsisTlvs["06"]["description"] = "CmMic"
DocsisTlvs["06"]["hex"] = "06"
DocsisTlvs["06"]["datatype"] = "md5"
DocsisTlvs["06"]["subTlvs"] = {}

DocsisTlvs["07"] = {}
DocsisTlvs["07"]["description"] = "CmtsMic"
DocsisTlvs["07"]["hex"] = "07"
DocsisTlvs["07"]["datatype"] = "md5"
DocsisTlvs["07"]["subTlvs"] = {}

DocsisTlvs["08"] = {}
DocsisTlvs["08"]["description"] = "Unknown"
DocsisTlvs["08"]["hex"] = "08"
DocsisTlvs["08"]["datatype"] = "unknown"
DocsisTlvs["08"]["subTlvs"] = {}

DocsisTlvs["09"] = {}
DocsisTlvs["09"]["description"] = "SwUpgradeFilename"
DocsisTlvs["09"]["hex"] = "09"
DocsisTlvs["09"]["datatype"] = "string"
DocsisTlvs["09"]["subTlvs"] = {}

DocsisTlvs["10"] = {}
DocsisTlvs["10"]["description"] = "SnmpWriteControl"
DocsisTlvs["10"]["hex"] = "0a"
DocsisTlvs["10"]["datatype"] = "snmp_wd"
DocsisTlvs["10"]["subTlvs"] = {}

DocsisTlvs["11"] = {}
DocsisTlvs["11"]["description"] = "SnmpMibObject"
DocsisTlvs["11"]["hex"] = "0b"
DocsisTlvs["11"]["datatype"] = "snmp_object"
DocsisTlvs["11"]["subTlvs"] = {}

DocsisTlvs["12"] = {}
DocsisTlvs["12"]["description"] = "ModemIPAddress"
DocsisTlvs["12"]["hex"] = "0c"
DocsisTlvs["12"]["datatype"] = "encode_ip"
DocsisTlvs["12"]["subTlvs"] = {}

DocsisTlvs["13"] = {}
DocsisTlvs["13"]["description"] = "Service(s) Not Available Response"
DocsisTlvs["13"]["hex"] = "0d"
DocsisTlvs["13"]["datatype"] = "encode_ip"
DocsisTlvs["13"]["subTlvs"] = {}

DocsisTlvs["14"] = {}
DocsisTlvs["14"]["description"] = "CpeMacAddress"
DocsisTlvs["14"]["hex"] = "0e"
DocsisTlvs["14"]["datatype"] = "ether"
DocsisTlvs["14"]["subTlvs"] = {}

DocsisTlvs["17"] = {}
DocsisTlvs["17"]["description"] = "BaselinePrivacy"
DocsisTlvs["17"]["hex"] = "11"
DocsisTlvs["17"]["datatype"] = "aggregate"
DocsisTlvs["17"]["subTlvs"] = {}

DocsisTlvs["17"]["subTlvs"]["01"] = {}
DocsisTlvs["17"]["subTlvs"]["01"]["description"] = "AuthTimeout"
DocsisTlvs["17"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["17"]["subTlvs"]["01"]["datatype"] = "uint"
DocsisTlvs["17"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["17"]["subTlvs"]["02"] = {}
DocsisTlvs["17"]["subTlvs"]["02"]["description"] = "ReAuthTimeout"
DocsisTlvs["17"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["17"]["subTlvs"]["02"]["datatype"] = "uint"
DocsisTlvs["17"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["17"]["subTlvs"]["03"] = {}
DocsisTlvs["17"]["subTlvs"]["03"]["description"] = "AuthGraceTime"
DocsisTlvs["17"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["17"]["subTlvs"]["03"]["datatype"] = "uint"
DocsisTlvs["17"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["17"]["subTlvs"]["04"] = {}
DocsisTlvs["17"]["subTlvs"]["04"]["description"] = "OperTimeout"
DocsisTlvs["17"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["17"]["subTlvs"]["04"]["datatype"] = "uint"
DocsisTlvs["17"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["17"]["subTlvs"]["05"] = {}
DocsisTlvs["17"]["subTlvs"]["05"]["description"] = "ReKeyTimeout"
DocsisTlvs["17"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["17"]["subTlvs"]["05"]["datatype"] = "uint"
DocsisTlvs["17"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["17"]["subTlvs"]["06"] = {}
DocsisTlvs["17"]["subTlvs"]["06"]["description"] = "TEKGraceTime"
DocsisTlvs["17"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["17"]["subTlvs"]["06"]["datatype"] = "uint"
DocsisTlvs["17"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["17"]["subTlvs"]["07"] = {}
DocsisTlvs["17"]["subTlvs"]["07"]["description"] = "AuthRejectTimeout"
DocsisTlvs["17"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["17"]["subTlvs"]["07"]["datatype"] = "uint"
DocsisTlvs["17"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["17"]["subTlvs"]["08"] = {}
DocsisTlvs["17"]["subTlvs"]["08"]["description"] = "SAMapWaitTimeout"
DocsisTlvs["17"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["17"]["subTlvs"]["08"]["datatype"] = "uint"
DocsisTlvs["17"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["17"]["subTlvs"]["09"] = {}
DocsisTlvs["17"]["subTlvs"]["09"]["description"] = "SAMapMaxRetries"
DocsisTlvs["17"]["subTlvs"]["09"]["hex"] = "09"
DocsisTlvs["17"]["subTlvs"]["09"]["datatype"] = "uint"
DocsisTlvs["17"]["subTlvs"]["09"]["subTlvs"] = {}

DocsisTlvs["18"] = {}
DocsisTlvs["18"]["description"] = "MaxCPE"
DocsisTlvs["18"]["hex"] = "12"
DocsisTlvs["18"]["datatype"] = "uchar"
DocsisTlvs["18"]["subTlvs"] = {}

DocsisTlvs["19"] = {}
DocsisTlvs["19"]["description"] = "TftpTimestamp"
DocsisTlvs["19"]["hex"] = "13"
DocsisTlvs["19"]["datatype"] = "uint"
DocsisTlvs["19"]["subTlvs"] = {}

DocsisTlvs["20"] = {}
DocsisTlvs["20"]["description"] = "TftpModemAddress"
DocsisTlvs["20"]["hex"] = "14"
DocsisTlvs["20"]["datatype"] = "encode_ip"
DocsisTlvs["20"]["subTlvs"] = {}

DocsisTlvs["21"] = {}
DocsisTlvs["21"]["description"] = "SwUpgradeServer"
DocsisTlvs["21"]["hex"] = "15"
DocsisTlvs["21"]["datatype"] = "encode_ip"
DocsisTlvs["21"]["subTlvs"] = {}

DocsisTlvs["22"] = {}
DocsisTlvs["22"]["description"] = "UsPacketClass"
DocsisTlvs["22"]["hex"] = "16"
DocsisTlvs["22"]["datatype"] = "aggregate"
DocsisTlvs["22"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["01"] = {}
DocsisTlvs["22"]["subTlvs"]["01"]["description"] = "ClassifierRef"
DocsisTlvs["22"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["22"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["22"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["02"] = {}
DocsisTlvs["22"]["subTlvs"]["02"]["description"] = "ClassifierId"
DocsisTlvs["22"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["22"]["subTlvs"]["02"]["datatype"] = "ushort"
DocsisTlvs["22"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["03"] = {}
DocsisTlvs["22"]["subTlvs"]["03"]["description"] = "ServiceFlowRef"
DocsisTlvs["22"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["22"]["subTlvs"]["03"]["datatype"] = "ushort"
DocsisTlvs["22"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["04"] = {}
DocsisTlvs["22"]["subTlvs"]["04"]["description"] = "ServiceFlowId"
DocsisTlvs["22"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["22"]["subTlvs"]["04"]["datatype"] = "uint"
DocsisTlvs["22"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["05"] = {}
DocsisTlvs["22"]["subTlvs"]["05"]["description"] = "RulePriority"
DocsisTlvs["22"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["22"]["subTlvs"]["05"]["datatype"] = "uchar"
DocsisTlvs["22"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["06"] = {}
DocsisTlvs["22"]["subTlvs"]["06"]["description"] = "ActivationState"
DocsisTlvs["22"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["22"]["subTlvs"]["06"]["datatype"] = "uchar"
DocsisTlvs["22"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["07"] = {}
DocsisTlvs["22"]["subTlvs"]["07"]["description"] = "DscAction"
DocsisTlvs["22"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["22"]["subTlvs"]["07"]["datatype"] = "uchar"
DocsisTlvs["22"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["09"] = {}
DocsisTlvs["22"]["subTlvs"]["09"]["description"] = "IpPacketClassifier"
DocsisTlvs["22"]["subTlvs"]["09"]["hex"] = "09"
DocsisTlvs["22"]["subTlvs"]["09"]["datatype"] = "aggregate"
DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["01"] = {}
DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["01"]["description"] = "IpTos"
DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["02"] = {}
DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["02"]["description"] = "IpProto"
DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["02"]["datatype"] = "ushort"
DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["03"] = {}
DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["03"]["description"] = "IpSrcAddr"
DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["03"]["datatype"] = "encode_ip"
DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["04"] = {}
DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["04"]["description"] = "IpSrcMask"
DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["04"]["datatype"] = "encode_ip"
DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["05"] = {}
DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["05"]["description"] = "IpDstAddr"
DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["05"]["datatype"] = "encode_ip"
DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["06"] = {}
DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["06"]["description"] = "IpDstMask"
DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["06"]["datatype"] = "encode_ip"
DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["07"] = {}
DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["07"]["description"] = "SrcPortStart"
DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["07"]["datatype"] = "ushort"
DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["08"] = {}
DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["08"]["description"] = "SrcPortEnd"
DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["08"]["datatype"] = "ushort"
DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["09"] = {}
DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["09"]["description"] = "DstPortStart"
DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["09"]["hex"] = "09"
DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["09"]["datatype"] = "ushort"
DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["09"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["10"] = {}
DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["10"]["description"] = "DstPortEnd"
DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["10"]["hex"] = "0a"
DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["10"]["datatype"] = "ushort"
DocsisTlvs["22"]["subTlvs"]["09"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["10"] = {}
DocsisTlvs["22"]["subTlvs"]["10"]["description"] = "LLCPacketClassifier"
DocsisTlvs["22"]["subTlvs"]["10"]["hex"] = "0a"
DocsisTlvs["22"]["subTlvs"]["10"]["datatype"] = "aggregate"
DocsisTlvs["22"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["10"]["subTlvs"]["01"] = {}
DocsisTlvs["22"]["subTlvs"]["10"]["subTlvs"]["01"]["description"] = "DstMacAddress"
DocsisTlvs["22"]["subTlvs"]["10"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["22"]["subTlvs"]["10"]["subTlvs"]["01"]["datatype"] = "(encode_ethermask)"
DocsisTlvs["22"]["subTlvs"]["10"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["10"]["subTlvs"]["02"] = {}
DocsisTlvs["22"]["subTlvs"]["10"]["subTlvs"]["02"]["description"] = "SrcMacAddress"
DocsisTlvs["22"]["subTlvs"]["10"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["22"]["subTlvs"]["10"]["subTlvs"]["02"]["datatype"] = "ether"
DocsisTlvs["22"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["10"]["subTlvs"]["03"] = {}
DocsisTlvs["22"]["subTlvs"]["10"]["subTlvs"]["03"]["description"] = "EtherType"
DocsisTlvs["22"]["subTlvs"]["10"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["22"]["subTlvs"]["10"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["10"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["11"] = {}
DocsisTlvs["22"]["subTlvs"]["11"]["description"] = "IEEE802Classifier"
DocsisTlvs["22"]["subTlvs"]["11"]["hex"] = "0b"
DocsisTlvs["22"]["subTlvs"]["11"]["datatype"] = "aggregate"
DocsisTlvs["22"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["11"]["subTlvs"]["01"] = {}
DocsisTlvs["22"]["subTlvs"]["11"]["subTlvs"]["01"]["description"] = "UserPriority"
DocsisTlvs["22"]["subTlvs"]["11"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["22"]["subTlvs"]["11"]["subTlvs"]["01"]["datatype"] = "char_list"
DocsisTlvs["22"]["subTlvs"]["11"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["11"]["subTlvs"]["02"] = {}
DocsisTlvs["22"]["subTlvs"]["11"]["subTlvs"]["02"]["description"] = "VlanID"
DocsisTlvs["22"]["subTlvs"]["11"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["22"]["subTlvs"]["11"]["subTlvs"]["02"]["datatype"] = "ushort"
DocsisTlvs["22"]["subTlvs"]["11"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["12"] = {}
DocsisTlvs["22"]["subTlvs"]["12"]["description"] = "PcIPv6PacketClassification"
DocsisTlvs["22"]["subTlvs"]["12"]["hex"] = "0c"
DocsisTlvs["22"]["subTlvs"]["12"]["datatype"] = "aggregate"
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["01"] = {}
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["01"]["description"] = "PcIPv6TrafficClassRangeAndMask"
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["02"] = {}
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["02"]["description"] = "PcIPv6FlowLabel"
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["03"] = {}
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["03"]["description"] = "PcIPv6NextHeaderType"
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["03"]["datatype"] = "ushort"
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["04"] = {}
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["04"]["description"] = "PcIPv6SourceAddress"
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["04"]["datatype"] = "encode_ip"
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["05"] = {}
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["05"]["description"] = "PcIPv6SourcePrefixLength"
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["05"]["datatype"] = "uchar"
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["06"] = {}
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["06"]["description"] = "PcIPv6DestAddress"
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["06"]["datatype"] = "encode_ip"
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["07"] = {}
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["07"]["description"] = "PcIPv6DestPrefixLength"
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["07"]["datatype"] = "uchar"
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["13"] = {}
DocsisTlvs["22"]["subTlvs"]["13"]["description"] = "PcCMIMEncoding"
DocsisTlvs["22"]["subTlvs"]["13"]["hex"] = "0d"
DocsisTlvs["22"]["subTlvs"]["13"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["13"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["14"] = {}
DocsisTlvs["22"]["subTlvs"]["14"]["description"] = "STagCTagFrameClassification"
DocsisTlvs["22"]["subTlvs"]["14"]["hex"] = "0e"
DocsisTlvs["22"]["subTlvs"]["14"]["datatype"] = "aggregate"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["01"] = {}
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["01"]["description"] = "STPID"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["02"] = {}
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["02"]["description"] = "SVID"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["03"] = {}
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["03"]["description"] = "SPCP"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["04"] = {}
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["04"]["description"] = "SDEI"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["05"] = {}
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["05"]["description"] = "CTPID"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["05"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["06"] = {}
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["06"]["description"] = "CVID"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["06"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["07"] = {}
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["07"]["description"] = "CPCP"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["07"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["08"] = {}
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["08"]["description"] = "CCFI"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["08"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["09"] = {}
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["09"]["description"] = "STCI"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["09"]["hex"] = "09"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["09"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["09"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["10"] = {}
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["10"]["description"] = "CTCI"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["10"]["hex"] = "0a"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["10"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["15"] = {}
DocsisTlvs["22"]["subTlvs"]["15"]["description"] = "IEEE8021ahPacketClassification"
DocsisTlvs["22"]["subTlvs"]["15"]["hex"] = "0f"
DocsisTlvs["22"]["subTlvs"]["15"]["datatype"] = "aggregate"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["01"] = {}
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["01"]["description"] = "ITPID"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["02"] = {}
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["02"]["description"] = "ISID"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["03"] = {}
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["03"]["description"] = "ITCI"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["04"] = {}
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["04"]["description"] = "IPCP"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["05"] = {}
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["05"]["description"] = "IDEI"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["05"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["06"] = {}
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["06"]["description"] = "IUCA"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["06"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["07"] = {}
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["07"]["description"] = "BTPID"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["07"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["08"] = {}
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["08"]["description"] = "BTCI"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["08"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["09"] = {}
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["09"]["description"] = "BPCP"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["09"]["hex"] = "09"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["09"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["09"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["10"] = {}
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["10"]["description"] = "BDEI"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["10"]["hex"] = "0a"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["10"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["11"] = {}
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["11"]["description"] = "BVID"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["11"]["hex"] = "0b"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["11"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["12"] = {}
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["12"]["description"] = "BDA"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["12"]["hex"] = "0c"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["12"]["datatype"] = "ether"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["13"] = {}
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["13"]["description"] = "BSA"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["13"]["hex"] = "0d"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["13"]["datatype"] = "ether"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["13"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["16"] = {}
DocsisTlvs["22"]["subTlvs"]["16"]["description"] = "ICMPv4ICMPv6PacketClassification"
DocsisTlvs["22"]["subTlvs"]["16"]["hex"] = "10"
DocsisTlvs["22"]["subTlvs"]["16"]["datatype"] = "aggregate"
DocsisTlvs["22"]["subTlvs"]["16"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["16"]["subTlvs"]["01"] = {}
DocsisTlvs["22"]["subTlvs"]["16"]["subTlvs"]["01"]["description"] = "ICMPv4ICMPv6TypeStart"
DocsisTlvs["22"]["subTlvs"]["16"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["22"]["subTlvs"]["16"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["22"]["subTlvs"]["16"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["16"]["subTlvs"]["02"] = {}
DocsisTlvs["22"]["subTlvs"]["16"]["subTlvs"]["02"]["description"] = "ICMPv4ICMPv6TypeEnd"
DocsisTlvs["22"]["subTlvs"]["16"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["22"]["subTlvs"]["16"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["22"]["subTlvs"]["16"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["17"] = {}
DocsisTlvs["22"]["subTlvs"]["17"]["description"] = "MPLSClassificationEncoding"
DocsisTlvs["22"]["subTlvs"]["17"]["hex"] = "11"
DocsisTlvs["22"]["subTlvs"]["17"]["datatype"] = "aggregate"
DocsisTlvs["22"]["subTlvs"]["17"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["17"]["subTlvs"]["01"] = {}
DocsisTlvs["22"]["subTlvs"]["17"]["subTlvs"]["01"]["description"] = "MPLSTCbits"
DocsisTlvs["22"]["subTlvs"]["17"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["22"]["subTlvs"]["17"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["17"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["17"]["subTlvs"]["02"] = {}
DocsisTlvs["22"]["subTlvs"]["17"]["subTlvs"]["02"]["description"] = "MPLSLabel"
DocsisTlvs["22"]["subTlvs"]["17"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["22"]["subTlvs"]["17"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["17"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["description"] = "VendorSpecific"
DocsisTlvs["22"]["subTlvs"]["43"]["hex"] = "2b"
DocsisTlvs["22"]["subTlvs"]["43"]["datatype"] = "aggregate"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["01"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["01"]["description"] = "CMLoadBalancingPolicyID"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["01"]["datatype"] = "uint"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["02"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["02"]["description"] = "CMLoadBalancingPriority"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["02"]["datatype"] = "uint"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["03"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["03"]["description"] = "CMLoadBalancingGroupID"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["03"]["datatype"] = "uint"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["04"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["04"]["description"] = "CMRangingClassIDExtension"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["04"]["datatype"] = "ushort"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["description"] = "L2VPNEncoding"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["datatype"] = "aggregate"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["01"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["01"]["description"] = "VPNIdentifier"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["description"] = "NSIEncapsulation"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["datatype"] = "aggregate"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["01"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["01"]["description"] = "ServiceMultiplexingValueOther"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["01"]["datatype"] = "lenzero"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["02"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["02"]["description"] = "NSIEncapsulationSingleQTag"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["02"]["datatype"] = "ushort"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["03"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["03"]["description"] = "NSIEncapsulationDualQTag"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["03"]["datatype"] = "dual_qtag"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["description"] = "ServiceMultiplexingValueMPLSPW"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["datatype"] = "aggregate"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["01"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["01"]["description"] = "MPLSPseudowireID"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["01"]["datatype"] = "uint"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["02"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["02"]["description"] = "MPLSPeerIpAddress"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["02"]["datatype"] = "char_ip_ip6"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["03"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["03"]["description"] = "MPLSPseudowireType"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["03"]["datatype"] = "uchar"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["04"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["04"]["description"] = "MPLSBackupPseudowireID"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["04"]["datatype"] = "uint"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["05"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["05"]["description"] = "MPLSBackupPeerIpAddress"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["05"]["datatype"] = "char_ip_ip6"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["05"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["05"]["description"] = "ServiceMultiplexingValueL2TPv3Peer"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["05"]["datatype"] = "char_ip_ip6"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["description"] = "IEEE8021ahEncapsulation"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["datatype"] = "aggregate"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["01"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["01"]["description"] = "ITCIEncapsulation"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["02"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["02"]["description"] = "BDAEncapsulation"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["03"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["03"]["description"] = "BTCIEncapsulation"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["04"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["04"]["description"] = "ITPIDEncapsulation"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["05"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["05"]["description"] = "IPCPEncapsulation"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["05"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["06"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["06"]["description"] = "IDEIEncapsulation"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["06"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["07"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["07"]["description"] = "IUCAEncapsulation"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["07"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["08"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["08"]["description"] = "ISIDEncapsulation"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["08"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["09"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["09"]["description"] = "BTPIDEncapsulation"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["09"]["hex"] = "09"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["09"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["09"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["10"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["10"]["description"] = "BPCPEncapsulation"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["10"]["hex"] = "0a"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["10"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["11"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["11"]["description"] = "BDEIEncapsulation"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["11"]["hex"] = "0b"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["11"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["12"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["12"]["description"] = "BVIDEncapsulation"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["12"]["hex"] = "0c"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["12"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["08"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["08"]["description"] = "ServiceMultiplexingValueIEEE8021adSTPID"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["08"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["03"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["03"]["description"] = "eSAFEDHCPSnooping"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["04"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["04"]["description"] = "CMInterfaceMaskCMIMSubtype"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["05"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["05"]["description"] = "AttachmentGroupID"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["05"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["06"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["06"]["description"] = "SourceAttachmentIndividualID"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["06"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["07"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["07"]["description"] = "TargetAttachmentIndividualID"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["07"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["08"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["08"]["description"] = "IngressUserPriority"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["08"]["datatype"] = "uchar"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["09"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["09"]["description"] = "UserPriorityRange"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["09"]["hex"] = "09"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["09"]["datatype"] = "char_list"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["09"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["10"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["10"]["description"] = "L2VPNSADescriptorSubtype"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["10"]["hex"] = "0a"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["10"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["12"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["12"]["description"] = "PseudowireType"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["12"]["hex"] = "0c"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["12"]["datatype"] = "uchar"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["13"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["13"]["description"] = "L2VPNMode"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["13"]["hex"] = "0d"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["13"]["datatype"] = "uchar"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["13"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["description"] = "TPIDTranslation"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["hex"] = "0e"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["datatype"] = "aggregate"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["01"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["01"]["description"] = "UpstreamTPIDTranslation"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["02"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["02"]["description"] = "DownstreamTPIDTranslation"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["03"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["03"]["description"] = "UpstreamSTPIDTranslation"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["04"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["04"]["description"] = "DownstreamSTPIDTranslation"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["05"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["05"]["description"] = "UpstreamBTPIDTranslation"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["05"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["06"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["06"]["description"] = "DownstreamBTPIDTranslation"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["06"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["07"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["07"]["description"] = "UpstreamITPIDTranslation"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["07"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["08"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["08"]["description"] = "DownstreamITPIDTranslation"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["08"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["description"] = "L2CPProcessing"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["hex"] = "0f"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["datatype"] = "aggregate"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["01"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["01"]["description"] = "L2CPTunnelMode"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["02"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["02"]["description"] = "L2CPDMACAddress"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["02"]["datatype"] = "ether"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["03"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["03"]["description"] = "L2CPOverwrotingDMACAddress"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["03"]["datatype"] = "ether"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["16"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["16"]["description"] = "DACDisableEnableConfiguration"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["16"]["hex"] = "10"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["16"]["datatype"] = "uchar"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["16"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["18"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["18"]["description"] = "PseudowireClass"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["18"]["hex"] = "12"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["18"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["18"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["description"] = "ServiceDelimiter"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["hex"] = "13"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["datatype"] = "aggregate"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["01"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["01"]["description"] = "CVIDDelimiter"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["02"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["02"]["description"] = "SVIDDelimiter"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["03"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["03"]["description"] = "ISIDDelimiter"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["04"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["04"]["description"] = "BVIDDelimiter"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["description"] = "VirtualSwitchInstanceEncoding"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["hex"] = "14"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["datatype"] = "aggregate"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["01"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["01"]["description"] = "VPLSClass"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["02"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["02"]["description"] = "ETreeRole"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["03"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["03"]["description"] = "ETreeRootVID"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["04"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["04"]["description"] = "ETreeLeafVID"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["description"] = "BGPAttribute"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["hex"] = "15"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["datatype"] = "aggregate"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["01"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["01"]["description"] = "BGPVPNID"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["01"]["datatype"] = "uint"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["02"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["02"]["description"] = "RouteDistinguisher"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["03"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["03"]["description"] = "RouteTargetImport"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["04"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["04"]["description"] = "RouteTargetExport"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["05"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["05"]["description"] = "CEIDVEID"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["05"]["datatype"] = "ushort"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["23"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["23"]["description"] = "PseudowireSignaling"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["23"]["hex"] = "17"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["23"]["datatype"] = "uchar"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["23"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["description"] = "SOAMSubtype"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["hex"] = "18"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["datatype"] = "aggregate"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["description"] = "MEPConfiguration"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["datatype"] = "aggregate"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["01"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["01"]["description"] = "MDLevel"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["02"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["02"]["description"] = "MDName"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["02"]["datatype"] = "string"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["03"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["03"]["description"] = "MAName"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["03"]["datatype"] = "string"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["04"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["04"]["description"] = "MEPID"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["04"]["datatype"] = "ushort"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["description"] = "RemoteMEPConfiguration"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["datatype"] = "aggregate"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["01"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["01"]["description"] = "RemoteMDLevel"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["02"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["02"]["description"] = "RemoteMDName"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["02"]["datatype"] = "string"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["03"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["03"]["description"] = "RemoteMAName"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["03"]["datatype"] = "string"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["04"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["04"]["description"] = "RemoteMEPID"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["04"]["datatype"] = "ushort"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["description"] = "FaultManagementConfiguration"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["datatype"] = "aggregate"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["01"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["01"]["description"] = "ContinuityCheckMessages"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["02"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["02"]["description"] = "LoopbackFunction"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["03"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["03"]["description"] = "LinktraceFunction"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["03"]["datatype"] = "uchar"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["description"] = "PerformanceManagementConfiguration"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["datatype"] = "aggregate"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["description"] = "FrameDelayMeasurement"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["datatype"] = "aggregate"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["01"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["01"]["description"] = "FrameDelayMeasurementEnable"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["02"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["02"]["description"] = "FrameDelayMeasurementOneWayTwoWay"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["03"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["03"]["description"] = "FrameDelayMeasurementTransmissionPeriodicity"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["03"]["datatype"] = "ushort"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["description"] = "FrameLossMeasurement"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["datatype"] = "aggregate"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["01"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["01"]["description"] = "FrameLossMeasurementEnable"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["02"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["02"]["description"] = "FrameLossMeasurementTransmissionPeriodicity"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["26"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["26"]["description"] = "L2VPNDSID"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["26"]["hex"] = "1a"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["26"]["datatype"] = "uint24"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["26"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["description"] = "VendorSpecificL2VPNSubtype"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["hex"] = "2b"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["datatype"] = "aggregate"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["subTlvs"]["08"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["subTlvs"]["08"]["description"] = "VendorIdentifier"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["subTlvs"]["08"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["06"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["06"]["description"] = "ExtendedCMTSMICConfigurationSetting"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["06"]["datatype"] = "aggregate"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["01"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["01"]["description"] = "ExtendedCMTSMICHMACtype"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["02"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["02"]["description"] = "ExtendedCMTSMICBitmap"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["03"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["03"]["description"] = "ExplicitExtendedCMTSMICDigest"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["07"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["07"]["description"] = "SAVAuthorizationEncoding"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["07"]["datatype"] = "aggregate"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["01"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["01"]["description"] = "SAVGroupName"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["01"]["datatype"] = "string"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["description"] = "SAVStaticPrefixRule"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["datatype"] = "aggregate"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["01"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["01"]["description"] = "SAVStaticPrefixAddress"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["01"]["datatype"] = "ip_ip6"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["02"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["02"]["description"] = "SAVStaticPrefixLength"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["08"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["08"]["description"] = "VendorIdentifier"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["08"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["09"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["09"]["description"] = "CMAttributeMasks"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["09"]["hex"] = "09"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["09"]["datatype"] = "aggregate"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["01"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["01"]["description"] = "CMDownstreamRequiredAttributeMask"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["02"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["02"]["description"] = "CMDownstreamForbiddenAttributeMask"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["03"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["03"]["description"] = "CMUpstreamRequiredAttributeMask"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["04"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["04"]["description"] = "CMUpstreamForbiddenAttributeMask"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["description"] = "IPMulticastJoinAuthorization"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["hex"] = "0a"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["datatype"] = "aggregate"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["01"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["01"]["description"] = "IPMulticastProfileName"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["01"]["datatype"] = "string"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["description"] = "IPMulticastJoinAuthStaticSessionRule"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["datatype"] = "aggregate"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["01"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["01"]["description"] = "MulticastRulePriority"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["02"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["02"]["description"] = "AuthorizationAction"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["03"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["03"]["description"] = "SourcePrefixAddress"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["03"]["datatype"] = "ip_ip6"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["04"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["04"]["description"] = "SourcePrefixLength"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["04"]["datatype"] = "uchar"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["05"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["05"]["description"] = "GroupPrefixAddress"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["05"]["datatype"] = "ip_ip6"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["06"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["06"]["description"] = "GroupPrefixLength"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["06"]["datatype"] = "uchar"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["03"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["03"]["description"] = "MaximumMulticastSessions"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["03"]["datatype"] = "ushort"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["11"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["11"]["description"] = "ServiceTypeIdentifier"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["11"]["hex"] = "0b"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["11"]["datatype"] = "string"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"]["description"] = "DEMARCAutoConfiguration"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"]["hex"] = "0c"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"]["datatype"] = "aggregate"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["01"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["01"]["description"] = "DACDisableEnableConfig"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["02"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["02"]["description"] = "CMIMEncoding"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["03"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["03"]["description"] = "UpstreamServiceClassName"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["03"]["datatype"] = "strzero"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["04"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["04"]["description"] = "DownstreamServiceClassName"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["04"]["datatype"] = "strzero"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["23"] = {}
DocsisTlvs["23"]["description"] = "DsPacketClass"
DocsisTlvs["23"]["hex"] = "17"
DocsisTlvs["23"]["datatype"] = "aggregate"
DocsisTlvs["23"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["01"] = {}
DocsisTlvs["23"]["subTlvs"]["01"]["description"] = "ClassifierRef"
DocsisTlvs["23"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["23"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["23"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["02"] = {}
DocsisTlvs["23"]["subTlvs"]["02"]["description"] = "ClassifierId"
DocsisTlvs["23"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["23"]["subTlvs"]["02"]["datatype"] = "ushort"
DocsisTlvs["23"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["03"] = {}
DocsisTlvs["23"]["subTlvs"]["03"]["description"] = "ServiceFlowRef"
DocsisTlvs["23"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["23"]["subTlvs"]["03"]["datatype"] = "ushort"
DocsisTlvs["23"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["04"] = {}
DocsisTlvs["23"]["subTlvs"]["04"]["description"] = "ServiceFlowId"
DocsisTlvs["23"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["23"]["subTlvs"]["04"]["datatype"] = "uint"
DocsisTlvs["23"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["05"] = {}
DocsisTlvs["23"]["subTlvs"]["05"]["description"] = "RulePriority"
DocsisTlvs["23"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["23"]["subTlvs"]["05"]["datatype"] = "uchar"
DocsisTlvs["23"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["06"] = {}
DocsisTlvs["23"]["subTlvs"]["06"]["description"] = "ActivationState"
DocsisTlvs["23"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["23"]["subTlvs"]["06"]["datatype"] = "uchar"
DocsisTlvs["23"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["07"] = {}
DocsisTlvs["23"]["subTlvs"]["07"]["description"] = "DscAction"
DocsisTlvs["23"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["23"]["subTlvs"]["07"]["datatype"] = "uchar"
DocsisTlvs["23"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["09"] = {}
DocsisTlvs["23"]["subTlvs"]["09"]["description"] = "IpPacketClassifier"
DocsisTlvs["23"]["subTlvs"]["09"]["hex"] = "09"
DocsisTlvs["23"]["subTlvs"]["09"]["datatype"] = "aggregate"
DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["01"] = {}
DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["01"]["description"] = "IpTos"
DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["02"] = {}
DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["02"]["description"] = "IpProto"
DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["02"]["datatype"] = "ushort"
DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["03"] = {}
DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["03"]["description"] = "IpSrcAddr"
DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["03"]["datatype"] = "encode_ip"
DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["04"] = {}
DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["04"]["description"] = "IpSrcMask"
DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["04"]["datatype"] = "encode_ip"
DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["05"] = {}
DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["05"]["description"] = "IpDstAddr"
DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["05"]["datatype"] = "encode_ip"
DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["06"] = {}
DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["06"]["description"] = "IpDstMask"
DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["06"]["datatype"] = "encode_ip"
DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["07"] = {}
DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["07"]["description"] = "SrcPortStart"
DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["07"]["datatype"] = "ushort"
DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["08"] = {}
DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["08"]["description"] = "SrcPortEnd"
DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["08"]["datatype"] = "ushort"
DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["09"] = {}
DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["09"]["description"] = "DstPortStart"
DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["09"]["hex"] = "09"
DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["09"]["datatype"] = "ushort"
DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["09"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["10"] = {}
DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["10"]["description"] = "DstPortEnd"
DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["10"]["hex"] = "0a"
DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["10"]["datatype"] = "ushort"
DocsisTlvs["23"]["subTlvs"]["09"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["10"] = {}
DocsisTlvs["23"]["subTlvs"]["10"]["description"] = "LLCPacketClassifier"
DocsisTlvs["23"]["subTlvs"]["10"]["hex"] = "0a"
DocsisTlvs["23"]["subTlvs"]["10"]["datatype"] = "aggregate"
DocsisTlvs["23"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["10"]["subTlvs"]["01"] = {}
DocsisTlvs["23"]["subTlvs"]["10"]["subTlvs"]["01"]["description"] = "DstMacAddress"
DocsisTlvs["23"]["subTlvs"]["10"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["23"]["subTlvs"]["10"]["subTlvs"]["01"]["datatype"] = "(encode_ethermask)"
DocsisTlvs["23"]["subTlvs"]["10"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["10"]["subTlvs"]["02"] = {}
DocsisTlvs["23"]["subTlvs"]["10"]["subTlvs"]["02"]["description"] = "SrcMacAddress"
DocsisTlvs["23"]["subTlvs"]["10"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["23"]["subTlvs"]["10"]["subTlvs"]["02"]["datatype"] = "ether"
DocsisTlvs["23"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["10"]["subTlvs"]["03"] = {}
DocsisTlvs["23"]["subTlvs"]["10"]["subTlvs"]["03"]["description"] = "EtherType"
DocsisTlvs["23"]["subTlvs"]["10"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["23"]["subTlvs"]["10"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["10"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["11"] = {}
DocsisTlvs["23"]["subTlvs"]["11"]["description"] = "IEEE802Classifier"
DocsisTlvs["23"]["subTlvs"]["11"]["hex"] = "0b"
DocsisTlvs["23"]["subTlvs"]["11"]["datatype"] = "aggregate"
DocsisTlvs["23"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["11"]["subTlvs"]["01"] = {}
DocsisTlvs["23"]["subTlvs"]["11"]["subTlvs"]["01"]["description"] = "UserPriority"
DocsisTlvs["23"]["subTlvs"]["11"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["23"]["subTlvs"]["11"]["subTlvs"]["01"]["datatype"] = "char_list"
DocsisTlvs["23"]["subTlvs"]["11"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["11"]["subTlvs"]["02"] = {}
DocsisTlvs["23"]["subTlvs"]["11"]["subTlvs"]["02"]["description"] = "VlanID"
DocsisTlvs["23"]["subTlvs"]["11"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["23"]["subTlvs"]["11"]["subTlvs"]["02"]["datatype"] = "ushort"
DocsisTlvs["23"]["subTlvs"]["11"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["12"] = {}
DocsisTlvs["23"]["subTlvs"]["12"]["description"] = "PcIPv6PacketClassification"
DocsisTlvs["23"]["subTlvs"]["12"]["hex"] = "0c"
DocsisTlvs["23"]["subTlvs"]["12"]["datatype"] = "aggregate"
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["01"] = {}
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["01"]["description"] = "PcIPv6TrafficClassRangeAndMask"
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["02"] = {}
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["02"]["description"] = "PcIPv6FlowLabel"
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["03"] = {}
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["03"]["description"] = "PcIPv6NextHeaderType"
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["03"]["datatype"] = "ushort"
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["04"] = {}
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["04"]["description"] = "PcIPv6SourceAddress"
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["04"]["datatype"] = "encode_ip"
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["05"] = {}
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["05"]["description"] = "PcIPv6SourcePrefixLength"
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["05"]["datatype"] = "uchar"
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["06"] = {}
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["06"]["description"] = "PcIPv6DestAddress"
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["06"]["datatype"] = "encode_ip"
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["07"] = {}
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["07"]["description"] = "PcIPv6DestPrefixLength"
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["07"]["datatype"] = "uchar"
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["13"] = {}
DocsisTlvs["23"]["subTlvs"]["13"]["description"] = "PcCMIMEncoding"
DocsisTlvs["23"]["subTlvs"]["13"]["hex"] = "0d"
DocsisTlvs["23"]["subTlvs"]["13"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["13"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["14"] = {}
DocsisTlvs["23"]["subTlvs"]["14"]["description"] = "STagCTagFrameClassification"
DocsisTlvs["23"]["subTlvs"]["14"]["hex"] = "0e"
DocsisTlvs["23"]["subTlvs"]["14"]["datatype"] = "aggregate"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["01"] = {}
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["01"]["description"] = "STPID"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["02"] = {}
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["02"]["description"] = "SVID"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["03"] = {}
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["03"]["description"] = "SPCP"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["04"] = {}
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["04"]["description"] = "SDEI"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["05"] = {}
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["05"]["description"] = "CTPID"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["05"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["06"] = {}
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["06"]["description"] = "CVID"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["06"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["07"] = {}
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["07"]["description"] = "CPCP"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["07"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["08"] = {}
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["08"]["description"] = "CCFI"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["08"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["09"] = {}
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["09"]["description"] = "STCI"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["09"]["hex"] = "09"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["09"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["09"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["10"] = {}
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["10"]["description"] = "CTCI"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["10"]["hex"] = "0a"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["10"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["15"] = {}
DocsisTlvs["23"]["subTlvs"]["15"]["description"] = "IEEE8021ahPacketClassification"
DocsisTlvs["23"]["subTlvs"]["15"]["hex"] = "0f"
DocsisTlvs["23"]["subTlvs"]["15"]["datatype"] = "aggregate"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["01"] = {}
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["01"]["description"] = "ITPID"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["02"] = {}
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["02"]["description"] = "ISID"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["03"] = {}
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["03"]["description"] = "ITCI"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["04"] = {}
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["04"]["description"] = "IPCP"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["05"] = {}
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["05"]["description"] = "IDEI"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["05"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["06"] = {}
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["06"]["description"] = "IUCA"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["06"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["07"] = {}
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["07"]["description"] = "BTPID"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["07"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["08"] = {}
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["08"]["description"] = "BTCI"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["08"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["09"] = {}
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["09"]["description"] = "BPCP"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["09"]["hex"] = "09"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["09"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["09"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["10"] = {}
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["10"]["description"] = "BDEI"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["10"]["hex"] = "0a"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["10"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["11"] = {}
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["11"]["description"] = "BVID"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["11"]["hex"] = "0b"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["11"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["12"] = {}
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["12"]["description"] = "BDA"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["12"]["hex"] = "0c"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["12"]["datatype"] = "ether"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["13"] = {}
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["13"]["description"] = "BSA"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["13"]["hex"] = "0d"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["13"]["datatype"] = "ether"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["13"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["16"] = {}
DocsisTlvs["23"]["subTlvs"]["16"]["description"] = "ICMPv4ICMPv6PacketClassification"
DocsisTlvs["23"]["subTlvs"]["16"]["hex"] = "10"
DocsisTlvs["23"]["subTlvs"]["16"]["datatype"] = "aggregate"
DocsisTlvs["23"]["subTlvs"]["16"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["16"]["subTlvs"]["01"] = {}
DocsisTlvs["23"]["subTlvs"]["16"]["subTlvs"]["01"]["description"] = "ICMPv4ICMPv6TypeStart"
DocsisTlvs["23"]["subTlvs"]["16"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["23"]["subTlvs"]["16"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["23"]["subTlvs"]["16"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["16"]["subTlvs"]["02"] = {}
DocsisTlvs["23"]["subTlvs"]["16"]["subTlvs"]["02"]["description"] = "ICMPv4ICMPv6TypeEnd"
DocsisTlvs["23"]["subTlvs"]["16"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["23"]["subTlvs"]["16"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["23"]["subTlvs"]["16"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["17"] = {}
DocsisTlvs["23"]["subTlvs"]["17"]["description"] = "MPLSClassificationEncoding"
DocsisTlvs["23"]["subTlvs"]["17"]["hex"] = "11"
DocsisTlvs["23"]["subTlvs"]["17"]["datatype"] = "aggregate"
DocsisTlvs["23"]["subTlvs"]["17"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["17"]["subTlvs"]["01"] = {}
DocsisTlvs["23"]["subTlvs"]["17"]["subTlvs"]["01"]["description"] = "MPLSTCbits"
DocsisTlvs["23"]["subTlvs"]["17"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["23"]["subTlvs"]["17"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["17"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["17"]["subTlvs"]["02"] = {}
DocsisTlvs["23"]["subTlvs"]["17"]["subTlvs"]["02"]["description"] = "MPLSLabel"
DocsisTlvs["23"]["subTlvs"]["17"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["23"]["subTlvs"]["17"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["17"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["description"] = "VendorSpecific"
DocsisTlvs["23"]["subTlvs"]["43"]["hex"] = "2b"
DocsisTlvs["23"]["subTlvs"]["43"]["datatype"] = "aggregate"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["01"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["01"]["description"] = "CMLoadBalancingPolicyID"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["01"]["datatype"] = "uint"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["02"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["02"]["description"] = "CMLoadBalancingPriority"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["02"]["datatype"] = "uint"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["03"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["03"]["description"] = "CMLoadBalancingGroupID"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["03"]["datatype"] = "uint"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["04"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["04"]["description"] = "CMRangingClassIDExtension"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["04"]["datatype"] = "ushort"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["description"] = "L2VPNEncoding"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["datatype"] = "aggregate"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["01"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["01"]["description"] = "VPNIdentifier"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["description"] = "NSIEncapsulation"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["datatype"] = "aggregate"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["01"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["01"]["description"] = "ServiceMultiplexingValueOther"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["01"]["datatype"] = "lenzero"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["02"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["02"]["description"] = "NSIEncapsulationSingleQTag"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["02"]["datatype"] = "ushort"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["03"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["03"]["description"] = "NSIEncapsulationDualQTag"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["03"]["datatype"] = "dual_qtag"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["description"] = "ServiceMultiplexingValueMPLSPW"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["datatype"] = "aggregate"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["01"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["01"]["description"] = "MPLSPseudowireID"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["01"]["datatype"] = "uint"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["02"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["02"]["description"] = "MPLSPeerIpAddress"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["02"]["datatype"] = "char_ip_ip6"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["03"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["03"]["description"] = "MPLSPseudowireType"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["03"]["datatype"] = "uchar"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["04"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["04"]["description"] = "MPLSBackupPseudowireID"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["04"]["datatype"] = "uint"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["05"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["05"]["description"] = "MPLSBackupPeerIpAddress"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["05"]["datatype"] = "char_ip_ip6"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["05"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["05"]["description"] = "ServiceMultiplexingValueL2TPv3Peer"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["05"]["datatype"] = "char_ip_ip6"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["description"] = "IEEE8021ahEncapsulation"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["datatype"] = "aggregate"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["01"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["01"]["description"] = "ITCIEncapsulation"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["02"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["02"]["description"] = "BDAEncapsulation"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["03"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["03"]["description"] = "BTCIEncapsulation"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["04"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["04"]["description"] = "ITPIDEncapsulation"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["05"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["05"]["description"] = "IPCPEncapsulation"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["05"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["06"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["06"]["description"] = "IDEIEncapsulation"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["06"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["07"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["07"]["description"] = "IUCAEncapsulation"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["07"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["08"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["08"]["description"] = "ISIDEncapsulation"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["08"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["09"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["09"]["description"] = "BTPIDEncapsulation"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["09"]["hex"] = "09"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["09"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["09"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["10"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["10"]["description"] = "BPCPEncapsulation"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["10"]["hex"] = "0a"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["10"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["11"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["11"]["description"] = "BDEIEncapsulation"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["11"]["hex"] = "0b"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["11"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["12"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["12"]["description"] = "BVIDEncapsulation"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["12"]["hex"] = "0c"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["12"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["08"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["08"]["description"] = "ServiceMultiplexingValueIEEE8021adSTPID"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["08"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["03"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["03"]["description"] = "eSAFEDHCPSnooping"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["04"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["04"]["description"] = "CMInterfaceMaskCMIMSubtype"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["05"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["05"]["description"] = "AttachmentGroupID"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["05"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["06"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["06"]["description"] = "SourceAttachmentIndividualID"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["06"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["07"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["07"]["description"] = "TargetAttachmentIndividualID"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["07"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["08"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["08"]["description"] = "IngressUserPriority"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["08"]["datatype"] = "uchar"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["09"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["09"]["description"] = "UserPriorityRange"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["09"]["hex"] = "09"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["09"]["datatype"] = "char_list"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["09"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["10"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["10"]["description"] = "L2VPNSADescriptorSubtype"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["10"]["hex"] = "0a"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["10"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["12"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["12"]["description"] = "PseudowireType"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["12"]["hex"] = "0c"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["12"]["datatype"] = "uchar"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["13"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["13"]["description"] = "L2VPNMode"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["13"]["hex"] = "0d"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["13"]["datatype"] = "uchar"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["13"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["description"] = "TPIDTranslation"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["hex"] = "0e"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["datatype"] = "aggregate"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["01"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["01"]["description"] = "UpstreamTPIDTranslation"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["02"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["02"]["description"] = "DownstreamTPIDTranslation"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["03"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["03"]["description"] = "UpstreamSTPIDTranslation"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["04"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["04"]["description"] = "DownstreamSTPIDTranslation"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["05"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["05"]["description"] = "UpstreamBTPIDTranslation"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["05"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["06"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["06"]["description"] = "DownstreamBTPIDTranslation"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["06"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["07"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["07"]["description"] = "UpstreamITPIDTranslation"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["07"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["08"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["08"]["description"] = "DownstreamITPIDTranslation"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["08"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["description"] = "L2CPProcessing"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["hex"] = "0f"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["datatype"] = "aggregate"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["01"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["01"]["description"] = "L2CPTunnelMode"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["02"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["02"]["description"] = "L2CPDMACAddress"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["02"]["datatype"] = "ether"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["03"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["03"]["description"] = "L2CPOverwrotingDMACAddress"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["03"]["datatype"] = "ether"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["16"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["16"]["description"] = "DACDisableEnableConfiguration"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["16"]["hex"] = "10"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["16"]["datatype"] = "uchar"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["16"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["18"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["18"]["description"] = "PseudowireClass"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["18"]["hex"] = "12"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["18"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["18"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["description"] = "ServiceDelimiter"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["hex"] = "13"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["datatype"] = "aggregate"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["01"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["01"]["description"] = "CVIDDelimiter"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["02"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["02"]["description"] = "SVIDDelimiter"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["03"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["03"]["description"] = "ISIDDelimiter"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["04"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["04"]["description"] = "BVIDDelimiter"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["description"] = "VirtualSwitchInstanceEncoding"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["hex"] = "14"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["datatype"] = "aggregate"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["01"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["01"]["description"] = "VPLSClass"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["02"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["02"]["description"] = "ETreeRole"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["03"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["03"]["description"] = "ETreeRootVID"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["04"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["04"]["description"] = "ETreeLeafVID"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["description"] = "BGPAttribute"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["hex"] = "15"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["datatype"] = "aggregate"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["01"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["01"]["description"] = "BGPVPNID"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["01"]["datatype"] = "uint"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["02"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["02"]["description"] = "RouteDistinguisher"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["03"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["03"]["description"] = "RouteTargetImport"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["04"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["04"]["description"] = "RouteTargetExport"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["05"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["05"]["description"] = "CEIDVEID"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["05"]["datatype"] = "ushort"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["23"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["23"]["description"] = "PseudowireSignaling"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["23"]["hex"] = "17"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["23"]["datatype"] = "uchar"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["23"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["description"] = "SOAMSubtype"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["hex"] = "18"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["datatype"] = "aggregate"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["description"] = "MEPConfiguration"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["datatype"] = "aggregate"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["01"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["01"]["description"] = "MDLevel"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["02"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["02"]["description"] = "MDName"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["02"]["datatype"] = "string"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["03"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["03"]["description"] = "MAName"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["03"]["datatype"] = "string"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["04"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["04"]["description"] = "MEPID"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["04"]["datatype"] = "ushort"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["description"] = "RemoteMEPConfiguration"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["datatype"] = "aggregate"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["01"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["01"]["description"] = "RemoteMDLevel"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["02"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["02"]["description"] = "RemoteMDName"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["02"]["datatype"] = "string"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["03"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["03"]["description"] = "RemoteMAName"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["03"]["datatype"] = "string"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["04"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["04"]["description"] = "RemoteMEPID"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["04"]["datatype"] = "ushort"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["description"] = "FaultManagementConfiguration"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["datatype"] = "aggregate"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["01"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["01"]["description"] = "ContinuityCheckMessages"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["02"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["02"]["description"] = "LoopbackFunction"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["03"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["03"]["description"] = "LinktraceFunction"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["03"]["datatype"] = "uchar"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["description"] = "PerformanceManagementConfiguration"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["datatype"] = "aggregate"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["description"] = "FrameDelayMeasurement"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["datatype"] = "aggregate"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["01"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["01"]["description"] = "FrameDelayMeasurementEnable"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["02"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["02"]["description"] = "FrameDelayMeasurementOneWayTwoWay"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["03"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["03"]["description"] = "FrameDelayMeasurementTransmissionPeriodicity"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["03"]["datatype"] = "ushort"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["description"] = "FrameLossMeasurement"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["datatype"] = "aggregate"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["01"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["01"]["description"] = "FrameLossMeasurementEnable"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["02"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["02"]["description"] = "FrameLossMeasurementTransmissionPeriodicity"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["26"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["26"]["description"] = "L2VPNDSID"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["26"]["hex"] = "1a"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["26"]["datatype"] = "uint24"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["26"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["description"] = "VendorSpecificL2VPNSubtype"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["hex"] = "2b"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["datatype"] = "aggregate"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["subTlvs"]["08"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["subTlvs"]["08"]["description"] = "VendorIdentifier"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["subTlvs"]["08"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["06"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["06"]["description"] = "ExtendedCMTSMICConfigurationSetting"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["06"]["datatype"] = "aggregate"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["01"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["01"]["description"] = "ExtendedCMTSMICHMACtype"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["02"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["02"]["description"] = "ExtendedCMTSMICBitmap"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["03"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["03"]["description"] = "ExplicitExtendedCMTSMICDigest"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["07"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["07"]["description"] = "SAVAuthorizationEncoding"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["07"]["datatype"] = "aggregate"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["01"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["01"]["description"] = "SAVGroupName"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["01"]["datatype"] = "string"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["description"] = "SAVStaticPrefixRule"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["datatype"] = "aggregate"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["01"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["01"]["description"] = "SAVStaticPrefixAddress"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["01"]["datatype"] = "ip_ip6"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["02"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["02"]["description"] = "SAVStaticPrefixLength"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["08"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["08"]["description"] = "VendorIdentifier"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["08"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["09"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["09"]["description"] = "CMAttributeMasks"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["09"]["hex"] = "09"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["09"]["datatype"] = "aggregate"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["01"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["01"]["description"] = "CMDownstreamRequiredAttributeMask"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["02"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["02"]["description"] = "CMDownstreamForbiddenAttributeMask"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["03"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["03"]["description"] = "CMUpstreamRequiredAttributeMask"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["04"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["04"]["description"] = "CMUpstreamForbiddenAttributeMask"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["description"] = "IPMulticastJoinAuthorization"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["hex"] = "0a"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["datatype"] = "aggregate"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["01"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["01"]["description"] = "IPMulticastProfileName"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["01"]["datatype"] = "string"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["description"] = "IPMulticastJoinAuthStaticSessionRule"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["datatype"] = "aggregate"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["01"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["01"]["description"] = "MulticastRulePriority"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["02"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["02"]["description"] = "AuthorizationAction"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["03"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["03"]["description"] = "SourcePrefixAddress"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["03"]["datatype"] = "ip_ip6"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["04"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["04"]["description"] = "SourcePrefixLength"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["04"]["datatype"] = "uchar"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["05"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["05"]["description"] = "GroupPrefixAddress"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["05"]["datatype"] = "ip_ip6"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["06"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["06"]["description"] = "GroupPrefixLength"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["06"]["datatype"] = "uchar"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["03"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["03"]["description"] = "MaximumMulticastSessions"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["03"]["datatype"] = "ushort"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["11"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["11"]["description"] = "ServiceTypeIdentifier"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["11"]["hex"] = "0b"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["11"]["datatype"] = "string"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"]["description"] = "DEMARCAutoConfiguration"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"]["hex"] = "0c"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"]["datatype"] = "aggregate"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["01"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["01"]["description"] = "DACDisableEnableConfig"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["02"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["02"]["description"] = "CMIMEncoding"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["03"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["03"]["description"] = "UpstreamServiceClassName"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["03"]["datatype"] = "strzero"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["04"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["04"]["description"] = "DownstreamServiceClassName"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["04"]["datatype"] = "strzero"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["24"] = {}
DocsisTlvs["24"]["description"] = "UsServiceFlow"
DocsisTlvs["24"]["hex"] = "18"
DocsisTlvs["24"]["datatype"] = "aggregate"
DocsisTlvs["24"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["01"] = {}
DocsisTlvs["24"]["subTlvs"]["01"]["description"] = "UsServiceFlowRef"
DocsisTlvs["24"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["24"]["subTlvs"]["01"]["datatype"] = "ushort"
DocsisTlvs["24"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["02"] = {}
DocsisTlvs["24"]["subTlvs"]["02"]["description"] = "UsServiceFlowId"
DocsisTlvs["24"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["24"]["subTlvs"]["02"]["datatype"] = "uint"
DocsisTlvs["24"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["03"] = {}
DocsisTlvs["24"]["subTlvs"]["03"]["description"] = "ServiceIdentifier"
DocsisTlvs["24"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["24"]["subTlvs"]["03"]["datatype"] = "ushort"
DocsisTlvs["24"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["04"] = {}
DocsisTlvs["24"]["subTlvs"]["04"]["description"] = "ServiceClassName"
DocsisTlvs["24"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["24"]["subTlvs"]["04"]["datatype"] = "strzero"
DocsisTlvs["24"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["06"] = {}
DocsisTlvs["24"]["subTlvs"]["06"]["description"] = "QosParamSetType"
DocsisTlvs["24"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["24"]["subTlvs"]["06"]["datatype"] = "uchar"
DocsisTlvs["24"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["07"] = {}
DocsisTlvs["24"]["subTlvs"]["07"]["description"] = "TrafficPriority"
DocsisTlvs["24"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["24"]["subTlvs"]["07"]["datatype"] = "uchar"
DocsisTlvs["24"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["08"] = {}
DocsisTlvs["24"]["subTlvs"]["08"]["description"] = "MaxRateSustained"
DocsisTlvs["24"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["24"]["subTlvs"]["08"]["datatype"] = "uint"
DocsisTlvs["24"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["09"] = {}
DocsisTlvs["24"]["subTlvs"]["09"]["description"] = "MaxTrafficBurst"
DocsisTlvs["24"]["subTlvs"]["09"]["hex"] = "09"
DocsisTlvs["24"]["subTlvs"]["09"]["datatype"] = "uint"
DocsisTlvs["24"]["subTlvs"]["09"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["10"] = {}
DocsisTlvs["24"]["subTlvs"]["10"]["description"] = "MinReservedRate"
DocsisTlvs["24"]["subTlvs"]["10"]["hex"] = "0a"
DocsisTlvs["24"]["subTlvs"]["10"]["datatype"] = "uint"
DocsisTlvs["24"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["11"] = {}
DocsisTlvs["24"]["subTlvs"]["11"]["description"] = "MinResPacketSize"
DocsisTlvs["24"]["subTlvs"]["11"]["hex"] = "0b"
DocsisTlvs["24"]["subTlvs"]["11"]["datatype"] = "ushort"
DocsisTlvs["24"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["12"] = {}
DocsisTlvs["24"]["subTlvs"]["12"]["description"] = "ActQosParamsTimeout"
DocsisTlvs["24"]["subTlvs"]["12"]["hex"] = "0c"
DocsisTlvs["24"]["subTlvs"]["12"]["datatype"] = "ushort"
DocsisTlvs["24"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["13"] = {}
DocsisTlvs["24"]["subTlvs"]["13"]["description"] = "AdmQosParamsTimeout"
DocsisTlvs["24"]["subTlvs"]["13"]["hex"] = "0d"
DocsisTlvs["24"]["subTlvs"]["13"]["datatype"] = "ushort"
DocsisTlvs["24"]["subTlvs"]["13"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["14"] = {}
DocsisTlvs["24"]["subTlvs"]["14"]["description"] = "MaxConcatenatedBurst"
DocsisTlvs["24"]["subTlvs"]["14"]["hex"] = "0e"
DocsisTlvs["24"]["subTlvs"]["14"]["datatype"] = "ushort"
DocsisTlvs["24"]["subTlvs"]["14"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["15"] = {}
DocsisTlvs["24"]["subTlvs"]["15"]["description"] = "SchedulingType"
DocsisTlvs["24"]["subTlvs"]["15"]["hex"] = "0f"
DocsisTlvs["24"]["subTlvs"]["15"]["datatype"] = "uchar"
DocsisTlvs["24"]["subTlvs"]["15"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["16"] = {}
DocsisTlvs["24"]["subTlvs"]["16"]["description"] = "RequestOrTxPolicy"
DocsisTlvs["24"]["subTlvs"]["16"]["hex"] = "10"
DocsisTlvs["24"]["subTlvs"]["16"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["16"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["17"] = {}
DocsisTlvs["24"]["subTlvs"]["17"]["description"] = "NominalPollInterval"
DocsisTlvs["24"]["subTlvs"]["17"]["hex"] = "11"
DocsisTlvs["24"]["subTlvs"]["17"]["datatype"] = "uint"
DocsisTlvs["24"]["subTlvs"]["17"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["18"] = {}
DocsisTlvs["24"]["subTlvs"]["18"]["description"] = "ToleratedPollJitter"
DocsisTlvs["24"]["subTlvs"]["18"]["hex"] = "12"
DocsisTlvs["24"]["subTlvs"]["18"]["datatype"] = "uint"
DocsisTlvs["24"]["subTlvs"]["18"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["19"] = {}
DocsisTlvs["24"]["subTlvs"]["19"]["description"] = "UnsolicitedGrantSize"
DocsisTlvs["24"]["subTlvs"]["19"]["hex"] = "13"
DocsisTlvs["24"]["subTlvs"]["19"]["datatype"] = "ushort"
DocsisTlvs["24"]["subTlvs"]["19"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["20"] = {}
DocsisTlvs["24"]["subTlvs"]["20"]["description"] = "NominalGrantInterval"
DocsisTlvs["24"]["subTlvs"]["20"]["hex"] = "14"
DocsisTlvs["24"]["subTlvs"]["20"]["datatype"] = "uint"
DocsisTlvs["24"]["subTlvs"]["20"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["21"] = {}
DocsisTlvs["24"]["subTlvs"]["21"]["description"] = "ToleratedGrantJitter"
DocsisTlvs["24"]["subTlvs"]["21"]["hex"] = "15"
DocsisTlvs["24"]["subTlvs"]["21"]["datatype"] = "uint"
DocsisTlvs["24"]["subTlvs"]["21"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["22"] = {}
DocsisTlvs["24"]["subTlvs"]["22"]["description"] = "GrantsPerInterval"
DocsisTlvs["24"]["subTlvs"]["22"]["hex"] = "16"
DocsisTlvs["24"]["subTlvs"]["22"]["datatype"] = "uchar"
DocsisTlvs["24"]["subTlvs"]["22"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["23"] = {}
DocsisTlvs["24"]["subTlvs"]["23"]["description"] = "IpTosOverwrite"
DocsisTlvs["24"]["subTlvs"]["23"]["hex"] = "17"
DocsisTlvs["24"]["subTlvs"]["23"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["23"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["26"] = {}
DocsisTlvs["24"]["subTlvs"]["26"]["description"] = "MultipliertoNumberofBytesRequested"
DocsisTlvs["24"]["subTlvs"]["26"]["hex"] = "1a"
DocsisTlvs["24"]["subTlvs"]["26"]["datatype"] = "uchar"
DocsisTlvs["24"]["subTlvs"]["26"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["27"] = {}
DocsisTlvs["24"]["subTlvs"]["27"]["description"] = "UpstreamPeakTrafficRate"
DocsisTlvs["24"]["subTlvs"]["27"]["hex"] = "1b"
DocsisTlvs["24"]["subTlvs"]["27"]["datatype"] = "uint"
DocsisTlvs["24"]["subTlvs"]["27"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["31"] = {}
DocsisTlvs["24"]["subTlvs"]["31"]["description"] = "ServiceFlowRequiredAttributeMask"
DocsisTlvs["24"]["subTlvs"]["31"]["hex"] = "1f"
DocsisTlvs["24"]["subTlvs"]["31"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["31"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["32"] = {}
DocsisTlvs["24"]["subTlvs"]["32"]["description"] = "ServiceFlowForbiddenAttributeMask"
DocsisTlvs["24"]["subTlvs"]["32"]["hex"] = "20"
DocsisTlvs["24"]["subTlvs"]["32"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["32"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["33"] = {}
DocsisTlvs["24"]["subTlvs"]["33"]["description"] = "ServiceFlowAttributeAggregationRuleMask"
DocsisTlvs["24"]["subTlvs"]["33"]["hex"] = "21"
DocsisTlvs["24"]["subTlvs"]["33"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["33"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["34"] = {}
DocsisTlvs["24"]["subTlvs"]["34"]["description"] = "ApplicationIdentifier"
DocsisTlvs["24"]["subTlvs"]["34"]["hex"] = "22"
DocsisTlvs["24"]["subTlvs"]["34"]["datatype"] = "uint"
DocsisTlvs["24"]["subTlvs"]["34"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["35"] = {}
DocsisTlvs["24"]["subTlvs"]["35"]["description"] = "BufferControl"
DocsisTlvs["24"]["subTlvs"]["35"]["hex"] = "23"
DocsisTlvs["24"]["subTlvs"]["35"]["datatype"] = "aggregate"
DocsisTlvs["24"]["subTlvs"]["35"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["35"]["subTlvs"]["01"] = {}
DocsisTlvs["24"]["subTlvs"]["35"]["subTlvs"]["01"]["description"] = "MinimumBuffer"
DocsisTlvs["24"]["subTlvs"]["35"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["24"]["subTlvs"]["35"]["subTlvs"]["01"]["datatype"] = "uint"
DocsisTlvs["24"]["subTlvs"]["35"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["35"]["subTlvs"]["02"] = {}
DocsisTlvs["24"]["subTlvs"]["35"]["subTlvs"]["02"]["description"] = "TargetBuffer"
DocsisTlvs["24"]["subTlvs"]["35"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["24"]["subTlvs"]["35"]["subTlvs"]["02"]["datatype"] = "uint"
DocsisTlvs["24"]["subTlvs"]["35"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["35"]["subTlvs"]["03"] = {}
DocsisTlvs["24"]["subTlvs"]["35"]["subTlvs"]["03"]["description"] = "MaximumBuffer"
DocsisTlvs["24"]["subTlvs"]["35"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["24"]["subTlvs"]["35"]["subTlvs"]["03"]["datatype"] = "uint"
DocsisTlvs["24"]["subTlvs"]["35"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["36"] = {}
DocsisTlvs["24"]["subTlvs"]["36"]["description"] = "UpstreamAggregateServiceFlowReference"
DocsisTlvs["24"]["subTlvs"]["36"]["hex"] = "24"
DocsisTlvs["24"]["subTlvs"]["36"]["datatype"] = "aggregate"
DocsisTlvs["24"]["subTlvs"]["36"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["37"] = {}
DocsisTlvs["24"]["subTlvs"]["37"]["description"] = "UpstreamMESPReference"
DocsisTlvs["24"]["subTlvs"]["37"]["hex"] = "25"
DocsisTlvs["24"]["subTlvs"]["37"]["datatype"] = "ushort"
DocsisTlvs["24"]["subTlvs"]["37"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["40"] = {}
DocsisTlvs["24"]["subTlvs"]["40"]["description"] = "AQMEncodings"
DocsisTlvs["24"]["subTlvs"]["40"]["hex"] = "28"
DocsisTlvs["24"]["subTlvs"]["40"]["datatype"] = "aggregate"
DocsisTlvs["24"]["subTlvs"]["40"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["40"]["subTlvs"]["01"] = {}
DocsisTlvs["24"]["subTlvs"]["40"]["subTlvs"]["01"]["description"] = "SFAQMDisable"
DocsisTlvs["24"]["subTlvs"]["40"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["24"]["subTlvs"]["40"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["24"]["subTlvs"]["40"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["40"]["subTlvs"]["02"] = {}
DocsisTlvs["24"]["subTlvs"]["40"]["subTlvs"]["02"]["description"] = "SFAQMLatencyTarget"
DocsisTlvs["24"]["subTlvs"]["40"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["24"]["subTlvs"]["40"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["24"]["subTlvs"]["40"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["41"] = {}
DocsisTlvs["24"]["subTlvs"]["41"]["description"] = "DataRateUnitSetting"
DocsisTlvs["24"]["subTlvs"]["41"]["hex"] = "29"
DocsisTlvs["24"]["subTlvs"]["41"]["datatype"] = "uchar"
DocsisTlvs["24"]["subTlvs"]["41"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["description"] = "VendorSpecific"
DocsisTlvs["24"]["subTlvs"]["43"]["hex"] = "2b"
DocsisTlvs["24"]["subTlvs"]["43"]["datatype"] = "aggregate"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["01"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["01"]["description"] = "CMLoadBalancingPolicyID"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["01"]["datatype"] = "uint"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["02"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["02"]["description"] = "CMLoadBalancingPriority"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["02"]["datatype"] = "uint"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["03"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["03"]["description"] = "CMLoadBalancingGroupID"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["03"]["datatype"] = "uint"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["04"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["04"]["description"] = "CMRangingClassIDExtension"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["04"]["datatype"] = "ushort"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["description"] = "L2VPNEncoding"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["datatype"] = "aggregate"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["01"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["01"]["description"] = "VPNIdentifier"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["description"] = "NSIEncapsulation"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["datatype"] = "aggregate"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["01"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["01"]["description"] = "ServiceMultiplexingValueOther"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["01"]["datatype"] = "lenzero"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["02"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["02"]["description"] = "NSIEncapsulationSingleQTag"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["02"]["datatype"] = "ushort"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["03"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["03"]["description"] = "NSIEncapsulationDualQTag"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["03"]["datatype"] = "dual_qtag"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["description"] = "ServiceMultiplexingValueMPLSPW"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["datatype"] = "aggregate"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["01"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["01"]["description"] = "MPLSPseudowireID"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["01"]["datatype"] = "uint"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["02"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["02"]["description"] = "MPLSPeerIpAddress"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["02"]["datatype"] = "char_ip_ip6"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["03"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["03"]["description"] = "MPLSPseudowireType"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["03"]["datatype"] = "uchar"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["04"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["04"]["description"] = "MPLSBackupPseudowireID"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["04"]["datatype"] = "uint"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["05"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["05"]["description"] = "MPLSBackupPeerIpAddress"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["05"]["datatype"] = "char_ip_ip6"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["05"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["05"]["description"] = "ServiceMultiplexingValueL2TPv3Peer"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["05"]["datatype"] = "char_ip_ip6"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["description"] = "IEEE8021ahEncapsulation"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["datatype"] = "aggregate"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["01"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["01"]["description"] = "ITCIEncapsulation"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["02"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["02"]["description"] = "BDAEncapsulation"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["03"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["03"]["description"] = "BTCIEncapsulation"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["04"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["04"]["description"] = "ITPIDEncapsulation"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["05"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["05"]["description"] = "IPCPEncapsulation"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["05"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["06"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["06"]["description"] = "IDEIEncapsulation"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["06"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["07"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["07"]["description"] = "IUCAEncapsulation"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["07"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["08"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["08"]["description"] = "ISIDEncapsulation"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["08"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["09"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["09"]["description"] = "BTPIDEncapsulation"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["09"]["hex"] = "09"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["09"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["09"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["10"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["10"]["description"] = "BPCPEncapsulation"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["10"]["hex"] = "0a"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["10"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["11"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["11"]["description"] = "BDEIEncapsulation"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["11"]["hex"] = "0b"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["11"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["12"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["12"]["description"] = "BVIDEncapsulation"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["12"]["hex"] = "0c"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["12"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["08"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["08"]["description"] = "ServiceMultiplexingValueIEEE8021adSTPID"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["08"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["03"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["03"]["description"] = "eSAFEDHCPSnooping"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["04"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["04"]["description"] = "CMInterfaceMaskCMIMSubtype"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["05"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["05"]["description"] = "AttachmentGroupID"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["05"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["06"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["06"]["description"] = "SourceAttachmentIndividualID"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["06"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["07"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["07"]["description"] = "TargetAttachmentIndividualID"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["07"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["08"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["08"]["description"] = "IngressUserPriority"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["08"]["datatype"] = "uchar"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["09"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["09"]["description"] = "UserPriorityRange"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["09"]["hex"] = "09"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["09"]["datatype"] = "char_list"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["09"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["10"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["10"]["description"] = "L2VPNSADescriptorSubtype"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["10"]["hex"] = "0a"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["10"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["12"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["12"]["description"] = "PseudowireType"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["12"]["hex"] = "0c"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["12"]["datatype"] = "uchar"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["13"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["13"]["description"] = "L2VPNMode"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["13"]["hex"] = "0d"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["13"]["datatype"] = "uchar"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["13"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["description"] = "TPIDTranslation"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["hex"] = "0e"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["datatype"] = "aggregate"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["01"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["01"]["description"] = "UpstreamTPIDTranslation"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["02"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["02"]["description"] = "DownstreamTPIDTranslation"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["03"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["03"]["description"] = "UpstreamSTPIDTranslation"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["04"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["04"]["description"] = "DownstreamSTPIDTranslation"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["05"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["05"]["description"] = "UpstreamBTPIDTranslation"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["05"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["06"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["06"]["description"] = "DownstreamBTPIDTranslation"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["06"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["07"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["07"]["description"] = "UpstreamITPIDTranslation"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["07"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["08"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["08"]["description"] = "DownstreamITPIDTranslation"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["08"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["description"] = "L2CPProcessing"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["hex"] = "0f"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["datatype"] = "aggregate"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["01"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["01"]["description"] = "L2CPTunnelMode"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["02"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["02"]["description"] = "L2CPDMACAddress"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["02"]["datatype"] = "ether"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["03"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["03"]["description"] = "L2CPOverwrotingDMACAddress"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["03"]["datatype"] = "ether"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["16"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["16"]["description"] = "DACDisableEnableConfiguration"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["16"]["hex"] = "10"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["16"]["datatype"] = "uchar"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["16"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["18"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["18"]["description"] = "PseudowireClass"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["18"]["hex"] = "12"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["18"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["18"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["description"] = "ServiceDelimiter"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["hex"] = "13"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["datatype"] = "aggregate"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["01"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["01"]["description"] = "CVIDDelimiter"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["02"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["02"]["description"] = "SVIDDelimiter"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["03"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["03"]["description"] = "ISIDDelimiter"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["04"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["04"]["description"] = "BVIDDelimiter"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["description"] = "VirtualSwitchInstanceEncoding"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["hex"] = "14"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["datatype"] = "aggregate"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["01"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["01"]["description"] = "VPLSClass"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["02"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["02"]["description"] = "ETreeRole"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["03"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["03"]["description"] = "ETreeRootVID"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["04"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["04"]["description"] = "ETreeLeafVID"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["description"] = "BGPAttribute"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["hex"] = "15"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["datatype"] = "aggregate"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["01"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["01"]["description"] = "BGPVPNID"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["01"]["datatype"] = "uint"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["02"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["02"]["description"] = "RouteDistinguisher"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["03"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["03"]["description"] = "RouteTargetImport"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["04"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["04"]["description"] = "RouteTargetExport"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["05"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["05"]["description"] = "CEIDVEID"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["05"]["datatype"] = "ushort"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["23"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["23"]["description"] = "PseudowireSignaling"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["23"]["hex"] = "17"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["23"]["datatype"] = "uchar"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["23"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["description"] = "SOAMSubtype"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["hex"] = "18"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["datatype"] = "aggregate"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["description"] = "MEPConfiguration"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["datatype"] = "aggregate"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["01"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["01"]["description"] = "MDLevel"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["02"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["02"]["description"] = "MDName"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["02"]["datatype"] = "string"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["03"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["03"]["description"] = "MAName"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["03"]["datatype"] = "string"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["04"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["04"]["description"] = "MEPID"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["04"]["datatype"] = "ushort"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["description"] = "RemoteMEPConfiguration"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["datatype"] = "aggregate"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["01"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["01"]["description"] = "RemoteMDLevel"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["02"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["02"]["description"] = "RemoteMDName"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["02"]["datatype"] = "string"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["03"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["03"]["description"] = "RemoteMAName"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["03"]["datatype"] = "string"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["04"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["04"]["description"] = "RemoteMEPID"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["04"]["datatype"] = "ushort"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["description"] = "FaultManagementConfiguration"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["datatype"] = "aggregate"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["01"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["01"]["description"] = "ContinuityCheckMessages"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["02"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["02"]["description"] = "LoopbackFunction"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["03"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["03"]["description"] = "LinktraceFunction"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["03"]["datatype"] = "uchar"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["description"] = "PerformanceManagementConfiguration"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["datatype"] = "aggregate"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["description"] = "FrameDelayMeasurement"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["datatype"] = "aggregate"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["01"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["01"]["description"] = "FrameDelayMeasurementEnable"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["02"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["02"]["description"] = "FrameDelayMeasurementOneWayTwoWay"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["03"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["03"]["description"] = "FrameDelayMeasurementTransmissionPeriodicity"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["03"]["datatype"] = "ushort"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["description"] = "FrameLossMeasurement"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["datatype"] = "aggregate"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["01"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["01"]["description"] = "FrameLossMeasurementEnable"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["02"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["02"]["description"] = "FrameLossMeasurementTransmissionPeriodicity"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["26"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["26"]["description"] = "L2VPNDSID"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["26"]["hex"] = "1a"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["26"]["datatype"] = "uint24"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["26"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["description"] = "VendorSpecificL2VPNSubtype"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["hex"] = "2b"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["datatype"] = "aggregate"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["subTlvs"]["08"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["subTlvs"]["08"]["description"] = "VendorIdentifier"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["subTlvs"]["08"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["06"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["06"]["description"] = "ExtendedCMTSMICConfigurationSetting"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["06"]["datatype"] = "aggregate"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["01"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["01"]["description"] = "ExtendedCMTSMICHMACtype"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["02"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["02"]["description"] = "ExtendedCMTSMICBitmap"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["03"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["03"]["description"] = "ExplicitExtendedCMTSMICDigest"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["07"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["07"]["description"] = "SAVAuthorizationEncoding"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["07"]["datatype"] = "aggregate"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["01"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["01"]["description"] = "SAVGroupName"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["01"]["datatype"] = "string"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["description"] = "SAVStaticPrefixRule"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["datatype"] = "aggregate"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["01"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["01"]["description"] = "SAVStaticPrefixAddress"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["01"]["datatype"] = "ip_ip6"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["02"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["02"]["description"] = "SAVStaticPrefixLength"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["08"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["08"]["description"] = "VendorIdentifier"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["08"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["09"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["09"]["description"] = "CMAttributeMasks"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["09"]["hex"] = "09"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["09"]["datatype"] = "aggregate"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["01"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["01"]["description"] = "CMDownstreamRequiredAttributeMask"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["02"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["02"]["description"] = "CMDownstreamForbiddenAttributeMask"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["03"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["03"]["description"] = "CMUpstreamRequiredAttributeMask"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["04"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["04"]["description"] = "CMUpstreamForbiddenAttributeMask"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["description"] = "IPMulticastJoinAuthorization"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["hex"] = "0a"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["datatype"] = "aggregate"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["01"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["01"]["description"] = "IPMulticastProfileName"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["01"]["datatype"] = "string"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["description"] = "IPMulticastJoinAuthStaticSessionRule"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["datatype"] = "aggregate"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["01"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["01"]["description"] = "MulticastRulePriority"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["02"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["02"]["description"] = "AuthorizationAction"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["03"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["03"]["description"] = "SourcePrefixAddress"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["03"]["datatype"] = "ip_ip6"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["04"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["04"]["description"] = "SourcePrefixLength"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["04"]["datatype"] = "uchar"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["05"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["05"]["description"] = "GroupPrefixAddress"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["05"]["datatype"] = "ip_ip6"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["06"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["06"]["description"] = "GroupPrefixLength"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["06"]["datatype"] = "uchar"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["03"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["03"]["description"] = "MaximumMulticastSessions"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["03"]["datatype"] = "ushort"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["11"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["11"]["description"] = "ServiceTypeIdentifier"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["11"]["hex"] = "0b"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["11"]["datatype"] = "string"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"]["description"] = "DEMARCAutoConfiguration"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"]["hex"] = "0c"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"]["datatype"] = "aggregate"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["01"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["01"]["description"] = "DACDisableEnableConfig"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["02"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["02"]["description"] = "CMIMEncoding"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["03"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["03"]["description"] = "UpstreamServiceClassName"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["03"]["datatype"] = "strzero"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["04"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["04"]["description"] = "DownstreamServiceClassName"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["04"]["datatype"] = "strzero"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["25"] = {}
DocsisTlvs["25"]["description"] = "DsServiceFlow"
DocsisTlvs["25"]["hex"] = "19"
DocsisTlvs["25"]["datatype"] = "aggregate"
DocsisTlvs["25"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["01"] = {}
DocsisTlvs["25"]["subTlvs"]["01"]["description"] = "DsServiceFlowRef"
DocsisTlvs["25"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["25"]["subTlvs"]["01"]["datatype"] = "ushort"
DocsisTlvs["25"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["02"] = {}
DocsisTlvs["25"]["subTlvs"]["02"]["description"] = "DsServiceFlowId"
DocsisTlvs["25"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["25"]["subTlvs"]["02"]["datatype"] = "uint"
DocsisTlvs["25"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["04"] = {}
DocsisTlvs["25"]["subTlvs"]["04"]["description"] = "ServiceClassName"
DocsisTlvs["25"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["25"]["subTlvs"]["04"]["datatype"] = "strzero"
DocsisTlvs["25"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["06"] = {}
DocsisTlvs["25"]["subTlvs"]["06"]["description"] = "QosParamSetType"
DocsisTlvs["25"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["25"]["subTlvs"]["06"]["datatype"] = "uchar"
DocsisTlvs["25"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["07"] = {}
DocsisTlvs["25"]["subTlvs"]["07"]["description"] = "TrafficPriority"
DocsisTlvs["25"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["25"]["subTlvs"]["07"]["datatype"] = "uchar"
DocsisTlvs["25"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["08"] = {}
DocsisTlvs["25"]["subTlvs"]["08"]["description"] = "MaxRateSustained"
DocsisTlvs["25"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["25"]["subTlvs"]["08"]["datatype"] = "uint"
DocsisTlvs["25"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["09"] = {}
DocsisTlvs["25"]["subTlvs"]["09"]["description"] = "MaxTrafficBurst"
DocsisTlvs["25"]["subTlvs"]["09"]["hex"] = "09"
DocsisTlvs["25"]["subTlvs"]["09"]["datatype"] = "uint"
DocsisTlvs["25"]["subTlvs"]["09"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["10"] = {}
DocsisTlvs["25"]["subTlvs"]["10"]["description"] = "MinReservedRate"
DocsisTlvs["25"]["subTlvs"]["10"]["hex"] = "0a"
DocsisTlvs["25"]["subTlvs"]["10"]["datatype"] = "uint"
DocsisTlvs["25"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["11"] = {}
DocsisTlvs["25"]["subTlvs"]["11"]["description"] = "MinResPacketSize"
DocsisTlvs["25"]["subTlvs"]["11"]["hex"] = "0b"
DocsisTlvs["25"]["subTlvs"]["11"]["datatype"] = "ushort"
DocsisTlvs["25"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["12"] = {}
DocsisTlvs["25"]["subTlvs"]["12"]["description"] = "ActQosParamsTimeout"
DocsisTlvs["25"]["subTlvs"]["12"]["hex"] = "0c"
DocsisTlvs["25"]["subTlvs"]["12"]["datatype"] = "ushort"
DocsisTlvs["25"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["13"] = {}
DocsisTlvs["25"]["subTlvs"]["13"]["description"] = "AdmQosParamsTimeout"
DocsisTlvs["25"]["subTlvs"]["13"]["hex"] = "0d"
DocsisTlvs["25"]["subTlvs"]["13"]["datatype"] = "ushort"
DocsisTlvs["25"]["subTlvs"]["13"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["14"] = {}
DocsisTlvs["25"]["subTlvs"]["14"]["description"] = "MaxDsLatency"
DocsisTlvs["25"]["subTlvs"]["14"]["hex"] = "0e"
DocsisTlvs["25"]["subTlvs"]["14"]["datatype"] = "uint"
DocsisTlvs["25"]["subTlvs"]["14"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["17"] = {}
DocsisTlvs["25"]["subTlvs"]["17"]["description"] = "DsResequencing"
DocsisTlvs["25"]["subTlvs"]["17"]["hex"] = "11"
DocsisTlvs["25"]["subTlvs"]["17"]["datatype"] = "uchar"
DocsisTlvs["25"]["subTlvs"]["17"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["23"] = {}
DocsisTlvs["25"]["subTlvs"]["23"]["description"] = "IpTosOverwrite"
DocsisTlvs["25"]["subTlvs"]["23"]["hex"] = "17"
DocsisTlvs["25"]["subTlvs"]["23"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["23"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["27"] = {}
DocsisTlvs["25"]["subTlvs"]["27"]["description"] = "DownstreamPeakTrafficRate"
DocsisTlvs["25"]["subTlvs"]["27"]["hex"] = "1b"
DocsisTlvs["25"]["subTlvs"]["27"]["datatype"] = "uint"
DocsisTlvs["25"]["subTlvs"]["27"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["31"] = {}
DocsisTlvs["25"]["subTlvs"]["31"]["description"] = "ServiceFlowRequiredAttributeMask"
DocsisTlvs["25"]["subTlvs"]["31"]["hex"] = "1f"
DocsisTlvs["25"]["subTlvs"]["31"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["31"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["32"] = {}
DocsisTlvs["25"]["subTlvs"]["32"]["description"] = "ServiceFlowForbiddenAttributeMask"
DocsisTlvs["25"]["subTlvs"]["32"]["hex"] = "20"
DocsisTlvs["25"]["subTlvs"]["32"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["32"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["33"] = {}
DocsisTlvs["25"]["subTlvs"]["33"]["description"] = "ServiceFlowAttributeAggregationRuleMask"
DocsisTlvs["25"]["subTlvs"]["33"]["hex"] = "21"
DocsisTlvs["25"]["subTlvs"]["33"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["33"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["34"] = {}
DocsisTlvs["25"]["subTlvs"]["34"]["description"] = "ApplicationIdentifier"
DocsisTlvs["25"]["subTlvs"]["34"]["hex"] = "22"
DocsisTlvs["25"]["subTlvs"]["34"]["datatype"] = "uint"
DocsisTlvs["25"]["subTlvs"]["34"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["35"] = {}
DocsisTlvs["25"]["subTlvs"]["35"]["description"] = "BufferControl"
DocsisTlvs["25"]["subTlvs"]["35"]["hex"] = "23"
DocsisTlvs["25"]["subTlvs"]["35"]["datatype"] = "aggregate"
DocsisTlvs["25"]["subTlvs"]["35"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["35"]["subTlvs"]["01"] = {}
DocsisTlvs["25"]["subTlvs"]["35"]["subTlvs"]["01"]["description"] = "MinimumBuffer"
DocsisTlvs["25"]["subTlvs"]["35"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["25"]["subTlvs"]["35"]["subTlvs"]["01"]["datatype"] = "uint"
DocsisTlvs["25"]["subTlvs"]["35"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["35"]["subTlvs"]["02"] = {}
DocsisTlvs["25"]["subTlvs"]["35"]["subTlvs"]["02"]["description"] = "TargetBuffer"
DocsisTlvs["25"]["subTlvs"]["35"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["25"]["subTlvs"]["35"]["subTlvs"]["02"]["datatype"] = "uint"
DocsisTlvs["25"]["subTlvs"]["35"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["35"]["subTlvs"]["03"] = {}
DocsisTlvs["25"]["subTlvs"]["35"]["subTlvs"]["03"]["description"] = "MaximumBuffer"
DocsisTlvs["25"]["subTlvs"]["35"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["25"]["subTlvs"]["35"]["subTlvs"]["03"]["datatype"] = "uint"
DocsisTlvs["25"]["subTlvs"]["35"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["36"] = {}
DocsisTlvs["25"]["subTlvs"]["36"]["description"] = "DownstreamAggregateServiceFlowReference"
DocsisTlvs["25"]["subTlvs"]["36"]["hex"] = "24"
DocsisTlvs["25"]["subTlvs"]["36"]["datatype"] = "aggregate"
DocsisTlvs["25"]["subTlvs"]["36"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["37"] = {}
DocsisTlvs["25"]["subTlvs"]["37"]["description"] = "DownstreamMESPReference"
DocsisTlvs["25"]["subTlvs"]["37"]["hex"] = "25"
DocsisTlvs["25"]["subTlvs"]["37"]["datatype"] = "ushort"
DocsisTlvs["25"]["subTlvs"]["37"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["40"] = {}
DocsisTlvs["25"]["subTlvs"]["40"]["description"] = "AQMEncodings"
DocsisTlvs["25"]["subTlvs"]["40"]["hex"] = "28"
DocsisTlvs["25"]["subTlvs"]["40"]["datatype"] = "aggregate"
DocsisTlvs["25"]["subTlvs"]["40"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["40"]["subTlvs"]["01"] = {}
DocsisTlvs["25"]["subTlvs"]["40"]["subTlvs"]["01"]["description"] = "SFAQMDisable"
DocsisTlvs["25"]["subTlvs"]["40"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["25"]["subTlvs"]["40"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["25"]["subTlvs"]["40"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["40"]["subTlvs"]["02"] = {}
DocsisTlvs["25"]["subTlvs"]["40"]["subTlvs"]["02"]["description"] = "SFAQMLatencyTarget"
DocsisTlvs["25"]["subTlvs"]["40"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["25"]["subTlvs"]["40"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["25"]["subTlvs"]["40"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["41"] = {}
DocsisTlvs["25"]["subTlvs"]["41"]["description"] = "DataRateUnitSetting"
DocsisTlvs["25"]["subTlvs"]["41"]["hex"] = "29"
DocsisTlvs["25"]["subTlvs"]["41"]["datatype"] = "uchar"
DocsisTlvs["25"]["subTlvs"]["41"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["description"] = "VendorSpecific"
DocsisTlvs["25"]["subTlvs"]["43"]["hex"] = "2b"
DocsisTlvs["25"]["subTlvs"]["43"]["datatype"] = "aggregate"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["01"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["01"]["description"] = "CMLoadBalancingPolicyID"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["01"]["datatype"] = "uint"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["02"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["02"]["description"] = "CMLoadBalancingPriority"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["02"]["datatype"] = "uint"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["03"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["03"]["description"] = "CMLoadBalancingGroupID"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["03"]["datatype"] = "uint"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["04"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["04"]["description"] = "CMRangingClassIDExtension"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["04"]["datatype"] = "ushort"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["description"] = "L2VPNEncoding"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["datatype"] = "aggregate"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["01"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["01"]["description"] = "VPNIdentifier"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["description"] = "NSIEncapsulation"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["datatype"] = "aggregate"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["01"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["01"]["description"] = "ServiceMultiplexingValueOther"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["01"]["datatype"] = "lenzero"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["02"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["02"]["description"] = "NSIEncapsulationSingleQTag"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["02"]["datatype"] = "ushort"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["03"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["03"]["description"] = "NSIEncapsulationDualQTag"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["03"]["datatype"] = "dual_qtag"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["description"] = "ServiceMultiplexingValueMPLSPW"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["datatype"] = "aggregate"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["01"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["01"]["description"] = "MPLSPseudowireID"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["01"]["datatype"] = "uint"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["02"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["02"]["description"] = "MPLSPeerIpAddress"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["02"]["datatype"] = "char_ip_ip6"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["03"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["03"]["description"] = "MPLSPseudowireType"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["03"]["datatype"] = "uchar"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["04"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["04"]["description"] = "MPLSBackupPseudowireID"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["04"]["datatype"] = "uint"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["05"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["05"]["description"] = "MPLSBackupPeerIpAddress"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["05"]["datatype"] = "char_ip_ip6"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["05"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["05"]["description"] = "ServiceMultiplexingValueL2TPv3Peer"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["05"]["datatype"] = "char_ip_ip6"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["description"] = "IEEE8021ahEncapsulation"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["datatype"] = "aggregate"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["01"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["01"]["description"] = "ITCIEncapsulation"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["02"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["02"]["description"] = "BDAEncapsulation"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["03"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["03"]["description"] = "BTCIEncapsulation"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["04"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["04"]["description"] = "ITPIDEncapsulation"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["05"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["05"]["description"] = "IPCPEncapsulation"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["05"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["06"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["06"]["description"] = "IDEIEncapsulation"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["06"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["07"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["07"]["description"] = "IUCAEncapsulation"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["07"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["08"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["08"]["description"] = "ISIDEncapsulation"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["08"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["09"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["09"]["description"] = "BTPIDEncapsulation"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["09"]["hex"] = "09"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["09"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["09"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["10"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["10"]["description"] = "BPCPEncapsulation"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["10"]["hex"] = "0a"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["10"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["11"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["11"]["description"] = "BDEIEncapsulation"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["11"]["hex"] = "0b"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["11"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["12"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["12"]["description"] = "BVIDEncapsulation"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["12"]["hex"] = "0c"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["12"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["08"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["08"]["description"] = "ServiceMultiplexingValueIEEE8021adSTPID"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["08"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["03"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["03"]["description"] = "eSAFEDHCPSnooping"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["04"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["04"]["description"] = "CMInterfaceMaskCMIMSubtype"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["05"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["05"]["description"] = "AttachmentGroupID"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["05"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["06"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["06"]["description"] = "SourceAttachmentIndividualID"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["06"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["07"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["07"]["description"] = "TargetAttachmentIndividualID"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["07"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["08"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["08"]["description"] = "IngressUserPriority"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["08"]["datatype"] = "uchar"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["09"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["09"]["description"] = "UserPriorityRange"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["09"]["hex"] = "09"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["09"]["datatype"] = "char_list"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["09"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["10"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["10"]["description"] = "L2VPNSADescriptorSubtype"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["10"]["hex"] = "0a"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["10"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["12"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["12"]["description"] = "PseudowireType"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["12"]["hex"] = "0c"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["12"]["datatype"] = "uchar"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["13"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["13"]["description"] = "L2VPNMode"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["13"]["hex"] = "0d"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["13"]["datatype"] = "uchar"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["13"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["description"] = "TPIDTranslation"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["hex"] = "0e"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["datatype"] = "aggregate"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["01"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["01"]["description"] = "UpstreamTPIDTranslation"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["02"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["02"]["description"] = "DownstreamTPIDTranslation"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["03"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["03"]["description"] = "UpstreamSTPIDTranslation"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["04"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["04"]["description"] = "DownstreamSTPIDTranslation"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["05"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["05"]["description"] = "UpstreamBTPIDTranslation"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["05"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["06"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["06"]["description"] = "DownstreamBTPIDTranslation"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["06"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["07"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["07"]["description"] = "UpstreamITPIDTranslation"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["07"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["08"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["08"]["description"] = "DownstreamITPIDTranslation"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["08"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["description"] = "L2CPProcessing"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["hex"] = "0f"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["datatype"] = "aggregate"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["01"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["01"]["description"] = "L2CPTunnelMode"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["02"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["02"]["description"] = "L2CPDMACAddress"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["02"]["datatype"] = "ether"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["03"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["03"]["description"] = "L2CPOverwrotingDMACAddress"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["03"]["datatype"] = "ether"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["16"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["16"]["description"] = "DACDisableEnableConfiguration"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["16"]["hex"] = "10"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["16"]["datatype"] = "uchar"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["16"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["18"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["18"]["description"] = "PseudowireClass"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["18"]["hex"] = "12"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["18"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["18"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["description"] = "ServiceDelimiter"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["hex"] = "13"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["datatype"] = "aggregate"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["01"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["01"]["description"] = "CVIDDelimiter"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["02"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["02"]["description"] = "SVIDDelimiter"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["03"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["03"]["description"] = "ISIDDelimiter"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["04"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["04"]["description"] = "BVIDDelimiter"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["description"] = "VirtualSwitchInstanceEncoding"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["hex"] = "14"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["datatype"] = "aggregate"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["01"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["01"]["description"] = "VPLSClass"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["02"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["02"]["description"] = "ETreeRole"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["03"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["03"]["description"] = "ETreeRootVID"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["04"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["04"]["description"] = "ETreeLeafVID"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["description"] = "BGPAttribute"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["hex"] = "15"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["datatype"] = "aggregate"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["01"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["01"]["description"] = "BGPVPNID"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["01"]["datatype"] = "uint"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["02"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["02"]["description"] = "RouteDistinguisher"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["03"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["03"]["description"] = "RouteTargetImport"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["04"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["04"]["description"] = "RouteTargetExport"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["05"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["05"]["description"] = "CEIDVEID"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["05"]["datatype"] = "ushort"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["23"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["23"]["description"] = "PseudowireSignaling"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["23"]["hex"] = "17"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["23"]["datatype"] = "uchar"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["23"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["description"] = "SOAMSubtype"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["hex"] = "18"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["datatype"] = "aggregate"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["description"] = "MEPConfiguration"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["datatype"] = "aggregate"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["01"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["01"]["description"] = "MDLevel"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["02"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["02"]["description"] = "MDName"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["02"]["datatype"] = "string"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["03"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["03"]["description"] = "MAName"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["03"]["datatype"] = "string"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["04"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["04"]["description"] = "MEPID"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["04"]["datatype"] = "ushort"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["description"] = "RemoteMEPConfiguration"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["datatype"] = "aggregate"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["01"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["01"]["description"] = "RemoteMDLevel"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["02"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["02"]["description"] = "RemoteMDName"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["02"]["datatype"] = "string"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["03"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["03"]["description"] = "RemoteMAName"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["03"]["datatype"] = "string"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["04"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["04"]["description"] = "RemoteMEPID"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["04"]["datatype"] = "ushort"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["description"] = "FaultManagementConfiguration"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["datatype"] = "aggregate"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["01"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["01"]["description"] = "ContinuityCheckMessages"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["02"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["02"]["description"] = "LoopbackFunction"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["03"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["03"]["description"] = "LinktraceFunction"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["03"]["datatype"] = "uchar"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["description"] = "PerformanceManagementConfiguration"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["datatype"] = "aggregate"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["description"] = "FrameDelayMeasurement"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["datatype"] = "aggregate"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["01"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["01"]["description"] = "FrameDelayMeasurementEnable"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["02"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["02"]["description"] = "FrameDelayMeasurementOneWayTwoWay"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["03"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["03"]["description"] = "FrameDelayMeasurementTransmissionPeriodicity"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["03"]["datatype"] = "ushort"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["description"] = "FrameLossMeasurement"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["datatype"] = "aggregate"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["01"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["01"]["description"] = "FrameLossMeasurementEnable"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["02"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["02"]["description"] = "FrameLossMeasurementTransmissionPeriodicity"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["26"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["26"]["description"] = "L2VPNDSID"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["26"]["hex"] = "1a"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["26"]["datatype"] = "uint24"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["26"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["description"] = "VendorSpecificL2VPNSubtype"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["hex"] = "2b"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["datatype"] = "aggregate"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["subTlvs"]["08"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["subTlvs"]["08"]["description"] = "VendorIdentifier"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["subTlvs"]["08"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["06"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["06"]["description"] = "ExtendedCMTSMICConfigurationSetting"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["06"]["datatype"] = "aggregate"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["01"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["01"]["description"] = "ExtendedCMTSMICHMACtype"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["02"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["02"]["description"] = "ExtendedCMTSMICBitmap"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["03"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["03"]["description"] = "ExplicitExtendedCMTSMICDigest"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["07"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["07"]["description"] = "SAVAuthorizationEncoding"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["07"]["datatype"] = "aggregate"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["01"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["01"]["description"] = "SAVGroupName"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["01"]["datatype"] = "string"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["description"] = "SAVStaticPrefixRule"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["datatype"] = "aggregate"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["01"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["01"]["description"] = "SAVStaticPrefixAddress"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["01"]["datatype"] = "ip_ip6"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["02"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["02"]["description"] = "SAVStaticPrefixLength"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["08"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["08"]["description"] = "VendorIdentifier"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["08"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["09"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["09"]["description"] = "CMAttributeMasks"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["09"]["hex"] = "09"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["09"]["datatype"] = "aggregate"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["01"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["01"]["description"] = "CMDownstreamRequiredAttributeMask"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["02"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["02"]["description"] = "CMDownstreamForbiddenAttributeMask"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["03"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["03"]["description"] = "CMUpstreamRequiredAttributeMask"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["04"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["04"]["description"] = "CMUpstreamForbiddenAttributeMask"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["description"] = "IPMulticastJoinAuthorization"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["hex"] = "0a"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["datatype"] = "aggregate"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["01"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["01"]["description"] = "IPMulticastProfileName"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["01"]["datatype"] = "string"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["description"] = "IPMulticastJoinAuthStaticSessionRule"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["datatype"] = "aggregate"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["01"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["01"]["description"] = "MulticastRulePriority"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["02"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["02"]["description"] = "AuthorizationAction"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["03"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["03"]["description"] = "SourcePrefixAddress"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["03"]["datatype"] = "ip_ip6"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["04"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["04"]["description"] = "SourcePrefixLength"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["04"]["datatype"] = "uchar"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["05"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["05"]["description"] = "GroupPrefixAddress"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["05"]["datatype"] = "ip_ip6"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["06"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["06"]["description"] = "GroupPrefixLength"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["06"]["datatype"] = "uchar"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["03"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["03"]["description"] = "MaximumMulticastSessions"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["03"]["datatype"] = "ushort"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["11"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["11"]["description"] = "ServiceTypeIdentifier"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["11"]["hex"] = "0b"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["11"]["datatype"] = "string"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"]["description"] = "DEMARCAutoConfiguration"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"]["hex"] = "0c"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"]["datatype"] = "aggregate"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["01"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["01"]["description"] = "DACDisableEnableConfig"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["02"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["02"]["description"] = "CMIMEncoding"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["03"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["03"]["description"] = "UpstreamServiceClassName"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["03"]["datatype"] = "strzero"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["04"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["04"]["description"] = "DownstreamServiceClassName"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["04"]["datatype"] = "strzero"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["26"] = {}
DocsisTlvs["26"]["description"] = "PHS"
DocsisTlvs["26"]["hex"] = "1a"
DocsisTlvs["26"]["datatype"] = "aggregate   "
DocsisTlvs["26"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["01"] = {}
DocsisTlvs["26"]["subTlvs"]["01"]["description"] = "PHSClassifierRef"
DocsisTlvs["26"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["26"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["26"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["02"] = {}
DocsisTlvs["26"]["subTlvs"]["02"]["description"] = "PHSClassifierId"
DocsisTlvs["26"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["26"]["subTlvs"]["02"]["datatype"] = "ushort"
DocsisTlvs["26"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["03"] = {}
DocsisTlvs["26"]["subTlvs"]["03"]["description"] = "PHSServiceFlowRef"
DocsisTlvs["26"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["26"]["subTlvs"]["03"]["datatype"] = "ushort"
DocsisTlvs["26"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["04"] = {}
DocsisTlvs["26"]["subTlvs"]["04"]["description"] = "PHSServiceFlowId"
DocsisTlvs["26"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["26"]["subTlvs"]["04"]["datatype"] = "uint"
DocsisTlvs["26"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["05"] = {}
DocsisTlvs["26"]["subTlvs"]["05"]["description"] = "PHSDSCAction"
DocsisTlvs["26"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["26"]["subTlvs"]["05"]["datatype"] = "uchar"
DocsisTlvs["26"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["07"] = {}
DocsisTlvs["26"]["subTlvs"]["07"]["description"] = "PHSField"
DocsisTlvs["26"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["26"]["subTlvs"]["07"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["08"] = {}
DocsisTlvs["26"]["subTlvs"]["08"]["description"] = "PHSIndex"
DocsisTlvs["26"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["26"]["subTlvs"]["08"]["datatype"] = "uchar"
DocsisTlvs["26"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["09"] = {}
DocsisTlvs["26"]["subTlvs"]["09"]["description"] = "PHSMask"
DocsisTlvs["26"]["subTlvs"]["09"]["hex"] = "09"
DocsisTlvs["26"]["subTlvs"]["09"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["09"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["10"] = {}
DocsisTlvs["26"]["subTlvs"]["10"]["description"] = "PHSSize"
DocsisTlvs["26"]["subTlvs"]["10"]["hex"] = "0a"
DocsisTlvs["26"]["subTlvs"]["10"]["datatype"] = "uchar"
DocsisTlvs["26"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["11"] = {}
DocsisTlvs["26"]["subTlvs"]["11"]["description"] = "PHSVerify"
DocsisTlvs["26"]["subTlvs"]["11"]["hex"] = "0b"
DocsisTlvs["26"]["subTlvs"]["11"]["datatype"] = "uchar"
DocsisTlvs["26"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["13"] = {}
DocsisTlvs["26"]["subTlvs"]["13"]["description"] = "PHSDBCAction"
DocsisTlvs["26"]["subTlvs"]["13"]["hex"] = "0d"
DocsisTlvs["26"]["subTlvs"]["13"]["datatype"] = "uchar"
DocsisTlvs["26"]["subTlvs"]["13"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["description"] = "VendorSpecific"
DocsisTlvs["26"]["subTlvs"]["43"]["hex"] = "2b"
DocsisTlvs["26"]["subTlvs"]["43"]["datatype"] = "aggregate"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["01"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["01"]["description"] = "CMLoadBalancingPolicyID"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["01"]["datatype"] = "uint"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["02"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["02"]["description"] = "CMLoadBalancingPriority"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["02"]["datatype"] = "uint"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["03"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["03"]["description"] = "CMLoadBalancingGroupID"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["03"]["datatype"] = "uint"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["04"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["04"]["description"] = "CMRangingClassIDExtension"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["04"]["datatype"] = "ushort"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["description"] = "L2VPNEncoding"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["datatype"] = "aggregate"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["01"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["01"]["description"] = "VPNIdentifier"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["description"] = "NSIEncapsulation"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["datatype"] = "aggregate"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["01"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["01"]["description"] = "ServiceMultiplexingValueOther"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["01"]["datatype"] = "lenzero"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["02"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["02"]["description"] = "NSIEncapsulationSingleQTag"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["02"]["datatype"] = "ushort"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["03"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["03"]["description"] = "NSIEncapsulationDualQTag"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["03"]["datatype"] = "dual_qtag"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["description"] = "ServiceMultiplexingValueMPLSPW"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["datatype"] = "aggregate"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["01"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["01"]["description"] = "MPLSPseudowireID"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["01"]["datatype"] = "uint"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["02"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["02"]["description"] = "MPLSPeerIpAddress"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["02"]["datatype"] = "char_ip_ip6"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["03"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["03"]["description"] = "MPLSPseudowireType"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["03"]["datatype"] = "uchar"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["04"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["04"]["description"] = "MPLSBackupPseudowireID"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["04"]["datatype"] = "uint"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["05"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["05"]["description"] = "MPLSBackupPeerIpAddress"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["05"]["datatype"] = "char_ip_ip6"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["05"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["05"]["description"] = "ServiceMultiplexingValueL2TPv3Peer"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["05"]["datatype"] = "char_ip_ip6"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["description"] = "IEEE8021ahEncapsulation"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["datatype"] = "aggregate"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["01"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["01"]["description"] = "ITCIEncapsulation"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["02"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["02"]["description"] = "BDAEncapsulation"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["03"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["03"]["description"] = "BTCIEncapsulation"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["04"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["04"]["description"] = "ITPIDEncapsulation"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["05"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["05"]["description"] = "IPCPEncapsulation"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["05"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["06"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["06"]["description"] = "IDEIEncapsulation"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["06"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["07"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["07"]["description"] = "IUCAEncapsulation"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["07"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["08"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["08"]["description"] = "ISIDEncapsulation"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["08"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["09"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["09"]["description"] = "BTPIDEncapsulation"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["09"]["hex"] = "09"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["09"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["09"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["10"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["10"]["description"] = "BPCPEncapsulation"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["10"]["hex"] = "0a"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["10"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["11"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["11"]["description"] = "BDEIEncapsulation"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["11"]["hex"] = "0b"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["11"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["12"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["12"]["description"] = "BVIDEncapsulation"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["12"]["hex"] = "0c"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["12"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["08"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["08"]["description"] = "ServiceMultiplexingValueIEEE8021adSTPID"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["08"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["03"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["03"]["description"] = "eSAFEDHCPSnooping"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["04"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["04"]["description"] = "CMInterfaceMaskCMIMSubtype"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["05"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["05"]["description"] = "AttachmentGroupID"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["05"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["06"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["06"]["description"] = "SourceAttachmentIndividualID"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["06"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["07"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["07"]["description"] = "TargetAttachmentIndividualID"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["07"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["08"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["08"]["description"] = "IngressUserPriority"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["08"]["datatype"] = "uchar"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["09"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["09"]["description"] = "UserPriorityRange"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["09"]["hex"] = "09"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["09"]["datatype"] = "char_list"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["09"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["10"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["10"]["description"] = "L2VPNSADescriptorSubtype"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["10"]["hex"] = "0a"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["10"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["12"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["12"]["description"] = "PseudowireType"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["12"]["hex"] = "0c"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["12"]["datatype"] = "uchar"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["13"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["13"]["description"] = "L2VPNMode"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["13"]["hex"] = "0d"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["13"]["datatype"] = "uchar"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["13"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["description"] = "TPIDTranslation"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["hex"] = "0e"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["datatype"] = "aggregate"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["01"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["01"]["description"] = "UpstreamTPIDTranslation"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["02"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["02"]["description"] = "DownstreamTPIDTranslation"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["03"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["03"]["description"] = "UpstreamSTPIDTranslation"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["04"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["04"]["description"] = "DownstreamSTPIDTranslation"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["05"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["05"]["description"] = "UpstreamBTPIDTranslation"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["05"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["06"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["06"]["description"] = "DownstreamBTPIDTranslation"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["06"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["07"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["07"]["description"] = "UpstreamITPIDTranslation"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["07"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["08"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["08"]["description"] = "DownstreamITPIDTranslation"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["08"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["description"] = "L2CPProcessing"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["hex"] = "0f"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["datatype"] = "aggregate"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["01"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["01"]["description"] = "L2CPTunnelMode"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["02"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["02"]["description"] = "L2CPDMACAddress"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["02"]["datatype"] = "ether"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["03"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["03"]["description"] = "L2CPOverwrotingDMACAddress"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["03"]["datatype"] = "ether"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["16"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["16"]["description"] = "DACDisableEnableConfiguration"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["16"]["hex"] = "10"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["16"]["datatype"] = "uchar"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["16"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["18"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["18"]["description"] = "PseudowireClass"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["18"]["hex"] = "12"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["18"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["18"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["description"] = "ServiceDelimiter"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["hex"] = "13"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["datatype"] = "aggregate"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["01"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["01"]["description"] = "CVIDDelimiter"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["02"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["02"]["description"] = "SVIDDelimiter"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["03"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["03"]["description"] = "ISIDDelimiter"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["04"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["04"]["description"] = "BVIDDelimiter"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["description"] = "VirtualSwitchInstanceEncoding"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["hex"] = "14"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["datatype"] = "aggregate"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["01"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["01"]["description"] = "VPLSClass"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["02"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["02"]["description"] = "ETreeRole"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["03"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["03"]["description"] = "ETreeRootVID"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["04"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["04"]["description"] = "ETreeLeafVID"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["description"] = "BGPAttribute"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["hex"] = "15"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["datatype"] = "aggregate"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["01"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["01"]["description"] = "BGPVPNID"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["01"]["datatype"] = "uint"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["02"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["02"]["description"] = "RouteDistinguisher"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["03"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["03"]["description"] = "RouteTargetImport"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["04"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["04"]["description"] = "RouteTargetExport"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["05"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["05"]["description"] = "CEIDVEID"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["05"]["datatype"] = "ushort"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["23"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["23"]["description"] = "PseudowireSignaling"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["23"]["hex"] = "17"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["23"]["datatype"] = "uchar"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["23"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["description"] = "SOAMSubtype"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["hex"] = "18"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["datatype"] = "aggregate"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["description"] = "MEPConfiguration"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["datatype"] = "aggregate"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["01"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["01"]["description"] = "MDLevel"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["02"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["02"]["description"] = "MDName"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["02"]["datatype"] = "string"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["03"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["03"]["description"] = "MAName"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["03"]["datatype"] = "string"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["04"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["04"]["description"] = "MEPID"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["04"]["datatype"] = "ushort"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["description"] = "RemoteMEPConfiguration"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["datatype"] = "aggregate"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["01"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["01"]["description"] = "RemoteMDLevel"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["02"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["02"]["description"] = "RemoteMDName"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["02"]["datatype"] = "string"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["03"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["03"]["description"] = "RemoteMAName"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["03"]["datatype"] = "string"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["04"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["04"]["description"] = "RemoteMEPID"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["04"]["datatype"] = "ushort"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["description"] = "FaultManagementConfiguration"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["datatype"] = "aggregate"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["01"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["01"]["description"] = "ContinuityCheckMessages"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["02"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["02"]["description"] = "LoopbackFunction"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["03"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["03"]["description"] = "LinktraceFunction"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["03"]["datatype"] = "uchar"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["description"] = "PerformanceManagementConfiguration"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["datatype"] = "aggregate"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["description"] = "FrameDelayMeasurement"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["datatype"] = "aggregate"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["01"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["01"]["description"] = "FrameDelayMeasurementEnable"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["02"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["02"]["description"] = "FrameDelayMeasurementOneWayTwoWay"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["03"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["03"]["description"] = "FrameDelayMeasurementTransmissionPeriodicity"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["03"]["datatype"] = "ushort"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["description"] = "FrameLossMeasurement"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["datatype"] = "aggregate"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["01"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["01"]["description"] = "FrameLossMeasurementEnable"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["02"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["02"]["description"] = "FrameLossMeasurementTransmissionPeriodicity"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["26"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["26"]["description"] = "L2VPNDSID"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["26"]["hex"] = "1a"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["26"]["datatype"] = "uint24"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["26"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["description"] = "VendorSpecificL2VPNSubtype"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["hex"] = "2b"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["datatype"] = "aggregate"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["subTlvs"]["08"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["subTlvs"]["08"]["description"] = "VendorIdentifier"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["subTlvs"]["08"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["06"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["06"]["description"] = "ExtendedCMTSMICConfigurationSetting"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["06"]["datatype"] = "aggregate"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["01"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["01"]["description"] = "ExtendedCMTSMICHMACtype"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["02"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["02"]["description"] = "ExtendedCMTSMICBitmap"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["03"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["03"]["description"] = "ExplicitExtendedCMTSMICDigest"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["07"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["07"]["description"] = "SAVAuthorizationEncoding"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["07"]["datatype"] = "aggregate"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["01"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["01"]["description"] = "SAVGroupName"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["01"]["datatype"] = "string"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["description"] = "SAVStaticPrefixRule"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["datatype"] = "aggregate"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["01"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["01"]["description"] = "SAVStaticPrefixAddress"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["01"]["datatype"] = "ip_ip6"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["02"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["02"]["description"] = "SAVStaticPrefixLength"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["08"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["08"]["description"] = "VendorIdentifier"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["08"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["09"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["09"]["description"] = "CMAttributeMasks"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["09"]["hex"] = "09"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["09"]["datatype"] = "aggregate"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["01"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["01"]["description"] = "CMDownstreamRequiredAttributeMask"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["02"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["02"]["description"] = "CMDownstreamForbiddenAttributeMask"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["03"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["03"]["description"] = "CMUpstreamRequiredAttributeMask"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["04"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["04"]["description"] = "CMUpstreamForbiddenAttributeMask"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["description"] = "IPMulticastJoinAuthorization"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["hex"] = "0a"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["datatype"] = "aggregate"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["01"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["01"]["description"] = "IPMulticastProfileName"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["01"]["datatype"] = "string"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["description"] = "IPMulticastJoinAuthStaticSessionRule"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["datatype"] = "aggregate"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["01"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["01"]["description"] = "MulticastRulePriority"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["02"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["02"]["description"] = "AuthorizationAction"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["03"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["03"]["description"] = "SourcePrefixAddress"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["03"]["datatype"] = "ip_ip6"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["04"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["04"]["description"] = "SourcePrefixLength"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["04"]["datatype"] = "uchar"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["05"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["05"]["description"] = "GroupPrefixAddress"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["05"]["datatype"] = "ip_ip6"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["06"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["06"]["description"] = "GroupPrefixLength"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["06"]["datatype"] = "uchar"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["03"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["03"]["description"] = "MaximumMulticastSessions"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["03"]["datatype"] = "ushort"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["11"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["11"]["description"] = "ServiceTypeIdentifier"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["11"]["hex"] = "0b"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["11"]["datatype"] = "string"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"]["description"] = "DEMARCAutoConfiguration"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"]["hex"] = "0c"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"]["datatype"] = "aggregate"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["01"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["01"]["description"] = "DACDisableEnableConfig"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["02"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["02"]["description"] = "CMIMEncoding"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["03"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["03"]["description"] = "UpstreamServiceClassName"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["03"]["datatype"] = "strzero"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["04"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["04"]["description"] = "DownstreamServiceClassName"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["04"]["datatype"] = "strzero"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["28"] = {}
DocsisTlvs["28"]["description"] = "MaxClassifiers"
DocsisTlvs["28"]["hex"] = "1c"
DocsisTlvs["28"]["datatype"] = "ushort"
DocsisTlvs["28"]["subTlvs"] = {}

DocsisTlvs["29"] = {}
DocsisTlvs["29"]["description"] = "GlobalPrivacyEnable"
DocsisTlvs["29"]["hex"] = "1d"
DocsisTlvs["29"]["datatype"] = "uchar"
DocsisTlvs["29"]["subTlvs"] = {}

DocsisTlvs["32"] = {}
DocsisTlvs["32"]["description"] = "MfgCVCData"
DocsisTlvs["32"]["hex"] = "20"
DocsisTlvs["32"]["datatype"] = "hexstr"
DocsisTlvs["32"]["subTlvs"] = {}

DocsisTlvs["170"] = {}
DocsisTlvs["170"]["description"] = "ManufacturerCVC"
DocsisTlvs["170"]["hex"] = "aa"
DocsisTlvs["170"]["datatype"] = "(decode_hexstr)"
DocsisTlvs["170"]["subTlvs"] = {}

DocsisTlvs["33"] = {}
DocsisTlvs["33"]["description"] = "CoSignerCVCData"
DocsisTlvs["33"]["hex"] = "21"
DocsisTlvs["33"]["datatype"] = "hexstr"
DocsisTlvs["33"]["subTlvs"] = {}

DocsisTlvs["172"] = {}
DocsisTlvs["172"]["description"] = "CoSignerCVC"
DocsisTlvs["172"]["hex"] = "ac"
DocsisTlvs["172"]["datatype"] = "(decode_hexstr)"
DocsisTlvs["172"]["subTlvs"] = {}

DocsisTlvs["34"] = {}
DocsisTlvs["34"]["description"] = "SnmpV3Kickstart"
DocsisTlvs["34"]["hex"] = "22"
DocsisTlvs["34"]["datatype"] = "aggregate"
DocsisTlvs["34"]["subTlvs"] = {}

DocsisTlvs["34"]["subTlvs"]["01"] = {}
DocsisTlvs["34"]["subTlvs"]["01"]["description"] = "SnmpV3SecurityName"
DocsisTlvs["34"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["34"]["subTlvs"]["01"]["datatype"] = "string"
DocsisTlvs["34"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["34"]["subTlvs"]["02"] = {}
DocsisTlvs["34"]["subTlvs"]["02"]["description"] = "SnmpV3MgrPublicNumber"
DocsisTlvs["34"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["34"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["34"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["34"]["subTlvs"]["35"] = {}
DocsisTlvs["34"]["subTlvs"]["35"]["description"] = "unknown Technicolor crap"
DocsisTlvs["34"]["subTlvs"]["35"]["hex"] = "23"
DocsisTlvs["34"]["subTlvs"]["35"]["datatype"] = "unknown"
DocsisTlvs["34"]["subTlvs"]["35"]["subTlvs"] = {}

DocsisTlvs["35"] = {}
DocsisTlvs["35"]["description"] = "SubMgmtControl"
DocsisTlvs["35"]["hex"] = "23"
DocsisTlvs["35"]["datatype"] = "hexstr"
DocsisTlvs["35"]["subTlvs"] = {}

DocsisTlvs["36"] = {}
DocsisTlvs["36"]["description"] = "SubscriberManagementCPEIPTable"
DocsisTlvs["36"]["hex"] = "24"
DocsisTlvs["36"]["datatype"] = "(encode_ip_list)"
DocsisTlvs["36"]["subTlvs"] = {}

DocsisTlvs["37"] = {}
DocsisTlvs["37"]["description"] = "SubMgmtFilters"
DocsisTlvs["37"]["hex"] = "25"
DocsisTlvs["37"]["datatype"] = "(encode_ushort_list)"
DocsisTlvs["37"]["subTlvs"] = {}

DocsisTlvs["38"] = {}
DocsisTlvs["38"]["description"] = "SnmpV3TrapReceiver"
DocsisTlvs["38"]["hex"] = "26"
DocsisTlvs["38"]["datatype"] = "aggregate"
DocsisTlvs["38"]["subTlvs"] = {}

DocsisTlvs["38"]["subTlvs"]["01"] = {}
DocsisTlvs["38"]["subTlvs"]["01"]["description"] = "SnmpV3TrapRxIP"
DocsisTlvs["38"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["38"]["subTlvs"]["01"]["datatype"] = "encode_ip"
DocsisTlvs["38"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["38"]["subTlvs"]["02"] = {}
DocsisTlvs["38"]["subTlvs"]["02"]["description"] = "SnmpV3TrapRxPort"
DocsisTlvs["38"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["38"]["subTlvs"]["02"]["datatype"] = "ushort"
DocsisTlvs["38"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["38"]["subTlvs"]["03"] = {}
DocsisTlvs["38"]["subTlvs"]["03"]["description"] = "SnmpV3TrapRxType"
DocsisTlvs["38"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["38"]["subTlvs"]["03"]["datatype"] = "ushort"
DocsisTlvs["38"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["38"]["subTlvs"]["04"] = {}
DocsisTlvs["38"]["subTlvs"]["04"]["description"] = "SnmpV3TrapRxTimeout"
DocsisTlvs["38"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["38"]["subTlvs"]["04"]["datatype"] = "ushort"
DocsisTlvs["38"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["38"]["subTlvs"]["05"] = {}
DocsisTlvs["38"]["subTlvs"]["05"]["description"] = "SnmpV3TrapRxRetries"
DocsisTlvs["38"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["38"]["subTlvs"]["05"]["datatype"] = "ushort"
DocsisTlvs["38"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["38"]["subTlvs"]["06"] = {}
DocsisTlvs["38"]["subTlvs"]["06"]["description"] = "SnmpV3TrapRxFilterOID"
DocsisTlvs["38"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["38"]["subTlvs"]["06"]["datatype"] = "(encode_oid)"
DocsisTlvs["38"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["38"]["subTlvs"]["07"] = {}
DocsisTlvs["38"]["subTlvs"]["07"]["description"] = "SnmpV3TrapRxSecurityName"
DocsisTlvs["38"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["38"]["subTlvs"]["07"]["datatype"] = "string"
DocsisTlvs["38"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["38"]["subTlvs"]["08"] = {}
DocsisTlvs["38"]["subTlvs"]["08"]["description"] = "SnmpV3TrapRxIP6"
DocsisTlvs["38"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["38"]["subTlvs"]["08"]["datatype"] = "encode_ip"
DocsisTlvs["38"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["39"] = {}
DocsisTlvs["39"]["description"] = "DocsisTwoEnable"
DocsisTlvs["39"]["hex"] = "27"
DocsisTlvs["39"]["datatype"] = "uchar"
DocsisTlvs["39"]["subTlvs"] = {}

DocsisTlvs["40"] = {}
DocsisTlvs["40"]["description"] = "EnableTestModes"
DocsisTlvs["40"]["hex"] = "28"
DocsisTlvs["40"]["datatype"] = "uchar"
DocsisTlvs["40"]["subTlvs"] = {}

DocsisTlvs["41"] = {}
DocsisTlvs["41"]["description"] = "DsChannelList"
DocsisTlvs["41"]["hex"] = "29"
DocsisTlvs["41"]["datatype"] = "aggregate"
DocsisTlvs["41"]["subTlvs"] = {}

DocsisTlvs["41"]["subTlvs"]["01"] = {}
DocsisTlvs["41"]["subTlvs"]["01"]["description"] = "SingleDsChannel"
DocsisTlvs["41"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["41"]["subTlvs"]["01"]["datatype"] = "aggregate"
DocsisTlvs["41"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["41"]["subTlvs"]["01"]["subTlvs"]["01"] = {}
DocsisTlvs["41"]["subTlvs"]["01"]["subTlvs"]["01"]["description"] = "SingleDsTimeout"
DocsisTlvs["41"]["subTlvs"]["01"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["41"]["subTlvs"]["01"]["subTlvs"]["01"]["datatype"] = "ushort"
DocsisTlvs["41"]["subTlvs"]["01"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["41"]["subTlvs"]["01"]["subTlvs"]["02"] = {}
DocsisTlvs["41"]["subTlvs"]["01"]["subTlvs"]["02"]["description"] = "SingleDsFrequency"
DocsisTlvs["41"]["subTlvs"]["01"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["41"]["subTlvs"]["01"]["subTlvs"]["02"]["datatype"] = "uint"
DocsisTlvs["41"]["subTlvs"]["01"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["41"]["subTlvs"]["02"] = {}
DocsisTlvs["41"]["subTlvs"]["02"]["description"] = "DsFreqRange"
DocsisTlvs["41"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["41"]["subTlvs"]["02"]["datatype"] = "aggregate"
DocsisTlvs["41"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["41"]["subTlvs"]["02"]["subTlvs"]["01"] = {}
DocsisTlvs["41"]["subTlvs"]["02"]["subTlvs"]["01"]["description"] = "DsFreqRangeTimeout"
DocsisTlvs["41"]["subTlvs"]["02"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["41"]["subTlvs"]["02"]["subTlvs"]["01"]["datatype"] = "ushort"
DocsisTlvs["41"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["41"]["subTlvs"]["02"]["subTlvs"]["02"] = {}
DocsisTlvs["41"]["subTlvs"]["02"]["subTlvs"]["02"]["description"] = "DsFreqRangeStart"
DocsisTlvs["41"]["subTlvs"]["02"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["41"]["subTlvs"]["02"]["subTlvs"]["02"]["datatype"] = "uint"
DocsisTlvs["41"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["41"]["subTlvs"]["02"]["subTlvs"]["03"] = {}
DocsisTlvs["41"]["subTlvs"]["02"]["subTlvs"]["03"]["description"] = "DsFreqRangeEnd"
DocsisTlvs["41"]["subTlvs"]["02"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["41"]["subTlvs"]["02"]["subTlvs"]["03"]["datatype"] = "uint"
DocsisTlvs["41"]["subTlvs"]["02"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["41"]["subTlvs"]["02"]["subTlvs"]["04"] = {}
DocsisTlvs["41"]["subTlvs"]["02"]["subTlvs"]["04"]["description"] = "DsFreqRangeStepSize"
DocsisTlvs["41"]["subTlvs"]["02"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["41"]["subTlvs"]["02"]["subTlvs"]["04"]["datatype"] = "uint"
DocsisTlvs["41"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["41"]["subTlvs"]["03"] = {}
DocsisTlvs["41"]["subTlvs"]["03"]["description"] = "DefaultScanTimeout"
DocsisTlvs["41"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["41"]["subTlvs"]["03"]["datatype"] = "ushort"
DocsisTlvs["41"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["41"]["subTlvs"]["10"] = {}
DocsisTlvs["41"]["subTlvs"]["10"]["description"] = "Technicolor thing"
DocsisTlvs["41"]["subTlvs"]["10"]["hex"] = "0a"
DocsisTlvs["41"]["subTlvs"]["10"]["datatype"] = "unknown"
DocsisTlvs["41"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["42"] = {}
DocsisTlvs["42"]["description"] = "MulticastMACAddress"
DocsisTlvs["42"]["hex"] = "2a"
DocsisTlvs["42"]["datatype"] = "ether"
DocsisTlvs["42"]["subTlvs"] = {}

DocsisTlvs["43"] = {}
DocsisTlvs["43"]["description"] = "VendorSpecific"
DocsisTlvs["43"]["hex"] = "2b"
DocsisTlvs["43"]["datatype"] = "aggregate"
DocsisTlvs["43"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["01"] = {}
DocsisTlvs["43"]["subTlvs"]["01"]["description"] = "CMLoadBalancingPolicyID"
DocsisTlvs["43"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["43"]["subTlvs"]["01"]["datatype"] = "uint"
DocsisTlvs["43"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["02"] = {}
DocsisTlvs["43"]["subTlvs"]["02"]["description"] = "CMLoadBalancingPriority"
DocsisTlvs["43"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["43"]["subTlvs"]["02"]["datatype"] = "uint"
DocsisTlvs["43"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["03"] = {}
DocsisTlvs["43"]["subTlvs"]["03"]["description"] = "CMLoadBalancingGroupID"
DocsisTlvs["43"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["43"]["subTlvs"]["03"]["datatype"] = "uint"
DocsisTlvs["43"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["04"] = {}
DocsisTlvs["43"]["subTlvs"]["04"]["description"] = "CMRangingClassIDExtension"
DocsisTlvs["43"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["43"]["subTlvs"]["04"]["datatype"] = "ushort"
DocsisTlvs["43"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["description"] = "L2VPNEncoding"
DocsisTlvs["43"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["43"]["subTlvs"]["05"]["datatype"] = "aggregate"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["01"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["01"]["description"] = "VPNIdentifier"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["description"] = "NSIEncapsulation"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["datatype"] = "aggregate"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["01"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["01"]["description"] = "ServiceMultiplexingValueOther"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["01"]["datatype"] = "lenzero"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["02"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["02"]["description"] = "NSIEncapsulationSingleQTag"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["02"]["datatype"] = "ushort"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["03"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["03"]["description"] = "NSIEncapsulationDualQTag"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["03"]["datatype"] = "dual_qtag"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["description"] = "ServiceMultiplexingValueMPLSPW"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["datatype"] = "aggregate"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["01"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["01"]["description"] = "MPLSPseudowireID"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["01"]["datatype"] = "uint"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["02"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["02"]["description"] = "MPLSPeerIpAddress"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["02"]["datatype"] = "char_ip_ip6"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["03"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["03"]["description"] = "MPLSPseudowireType"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["03"]["datatype"] = "uchar"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["04"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["04"]["description"] = "MPLSBackupPseudowireID"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["04"]["datatype"] = "uint"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["05"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["05"]["description"] = "MPLSBackupPeerIpAddress"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["05"]["datatype"] = "char_ip_ip6"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["05"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["05"]["description"] = "ServiceMultiplexingValueL2TPv3Peer"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["05"]["datatype"] = "char_ip_ip6"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["description"] = "IEEE8021ahEncapsulation"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["datatype"] = "aggregate"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["01"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["01"]["description"] = "ITCIEncapsulation"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["02"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["02"]["description"] = "BDAEncapsulation"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["03"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["03"]["description"] = "BTCIEncapsulation"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["04"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["04"]["description"] = "ITPIDEncapsulation"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["05"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["05"]["description"] = "IPCPEncapsulation"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["05"]["datatype"] = "hexstr"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["06"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["06"]["description"] = "IDEIEncapsulation"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["06"]["datatype"] = "hexstr"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["07"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["07"]["description"] = "IUCAEncapsulation"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["07"]["datatype"] = "hexstr"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["08"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["08"]["description"] = "ISIDEncapsulation"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["08"]["datatype"] = "hexstr"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["09"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["09"]["description"] = "BTPIDEncapsulation"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["09"]["hex"] = "09"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["09"]["datatype"] = "hexstr"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["09"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["10"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["10"]["description"] = "BPCPEncapsulation"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["10"]["hex"] = "0a"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["10"]["datatype"] = "hexstr"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["11"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["11"]["description"] = "BDEIEncapsulation"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["11"]["hex"] = "0b"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["11"]["datatype"] = "hexstr"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["12"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["12"]["description"] = "BVIDEncapsulation"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["12"]["hex"] = "0c"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["12"]["datatype"] = "hexstr"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["08"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["08"]["description"] = "ServiceMultiplexingValueIEEE8021adSTPID"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["08"]["datatype"] = "hexstr"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["03"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["03"]["description"] = "eSAFEDHCPSnooping"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["04"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["04"]["description"] = "CMInterfaceMaskCMIMSubtype"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["05"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["05"]["description"] = "AttachmentGroupID"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["05"]["datatype"] = "hexstr"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["06"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["06"]["description"] = "SourceAttachmentIndividualID"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["06"]["datatype"] = "hexstr"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["07"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["07"]["description"] = "TargetAttachmentIndividualID"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["07"]["datatype"] = "hexstr"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["08"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["08"]["description"] = "IngressUserPriority"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["08"]["datatype"] = "uchar"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["09"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["09"]["description"] = "UserPriorityRange"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["09"]["hex"] = "09"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["09"]["datatype"] = "char_list"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["09"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["10"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["10"]["description"] = "L2VPNSADescriptorSubtype"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["10"]["hex"] = "0a"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["10"]["datatype"] = "hexstr"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["12"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["12"]["description"] = "PseudowireType"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["12"]["hex"] = "0c"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["12"]["datatype"] = "uchar"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["13"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["13"]["description"] = "L2VPNMode"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["13"]["hex"] = "0d"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["13"]["datatype"] = "uchar"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["13"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["14"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["14"]["description"] = "TPIDTranslation"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["14"]["hex"] = "0e"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["14"]["datatype"] = "aggregate"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["01"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["01"]["description"] = "UpstreamTPIDTranslation"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["02"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["02"]["description"] = "DownstreamTPIDTranslation"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["03"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["03"]["description"] = "UpstreamSTPIDTranslation"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["04"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["04"]["description"] = "DownstreamSTPIDTranslation"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["05"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["05"]["description"] = "UpstreamBTPIDTranslation"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["05"]["datatype"] = "hexstr"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["06"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["06"]["description"] = "DownstreamBTPIDTranslation"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["06"]["datatype"] = "hexstr"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["07"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["07"]["description"] = "UpstreamITPIDTranslation"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["07"]["datatype"] = "hexstr"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["08"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["08"]["description"] = "DownstreamITPIDTranslation"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["08"]["datatype"] = "hexstr"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["15"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["15"]["description"] = "L2CPProcessing"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["15"]["hex"] = "0f"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["15"]["datatype"] = "aggregate"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["01"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["01"]["description"] = "L2CPTunnelMode"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["02"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["02"]["description"] = "L2CPDMACAddress"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["02"]["datatype"] = "ether"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["03"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["03"]["description"] = "L2CPOverwrotingDMACAddress"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["03"]["datatype"] = "ether"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["16"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["16"]["description"] = "DACDisableEnableConfiguration"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["16"]["hex"] = "10"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["16"]["datatype"] = "uchar"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["16"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["18"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["18"]["description"] = "PseudowireClass"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["18"]["hex"] = "12"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["18"]["datatype"] = "hexstr"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["18"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["19"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["19"]["description"] = "ServiceDelimiter"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["19"]["hex"] = "13"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["19"]["datatype"] = "aggregate"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["01"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["01"]["description"] = "CVIDDelimiter"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["02"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["02"]["description"] = "SVIDDelimiter"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["03"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["03"]["description"] = "ISIDDelimiter"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["04"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["04"]["description"] = "BVIDDelimiter"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["20"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["20"]["description"] = "VirtualSwitchInstanceEncoding"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["20"]["hex"] = "14"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["20"]["datatype"] = "aggregate"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["01"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["01"]["description"] = "VPLSClass"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["02"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["02"]["description"] = "ETreeRole"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["03"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["03"]["description"] = "ETreeRootVID"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["04"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["04"]["description"] = "ETreeLeafVID"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["21"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["21"]["description"] = "BGPAttribute"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["21"]["hex"] = "15"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["21"]["datatype"] = "aggregate"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["01"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["01"]["description"] = "BGPVPNID"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["01"]["datatype"] = "uint"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["02"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["02"]["description"] = "RouteDistinguisher"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["03"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["03"]["description"] = "RouteTargetImport"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["04"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["04"]["description"] = "RouteTargetExport"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["05"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["05"]["description"] = "CEIDVEID"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["05"]["datatype"] = "ushort"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["23"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["23"]["description"] = "PseudowireSignaling"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["23"]["hex"] = "17"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["23"]["datatype"] = "uchar"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["23"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["description"] = "SOAMSubtype"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["hex"] = "18"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["datatype"] = "aggregate"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["description"] = "MEPConfiguration"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["datatype"] = "aggregate"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["01"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["01"]["description"] = "MDLevel"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["02"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["02"]["description"] = "MDName"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["02"]["datatype"] = "string"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["03"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["03"]["description"] = "MAName"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["03"]["datatype"] = "string"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["04"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["04"]["description"] = "MEPID"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["04"]["datatype"] = "ushort"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["description"] = "RemoteMEPConfiguration"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["datatype"] = "aggregate"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["01"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["01"]["description"] = "RemoteMDLevel"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["02"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["02"]["description"] = "RemoteMDName"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["02"]["datatype"] = "string"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["03"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["03"]["description"] = "RemoteMAName"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["03"]["datatype"] = "string"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["04"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["04"]["description"] = "RemoteMEPID"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["04"]["datatype"] = "ushort"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["description"] = "FaultManagementConfiguration"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["datatype"] = "aggregate"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["01"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["01"]["description"] = "ContinuityCheckMessages"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["02"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["02"]["description"] = "LoopbackFunction"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["03"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["03"]["description"] = "LinktraceFunction"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["03"]["datatype"] = "uchar"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["description"] = "PerformanceManagementConfiguration"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["datatype"] = "aggregate"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["description"] = "FrameDelayMeasurement"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["datatype"] = "aggregate"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["01"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["01"]["description"] = "FrameDelayMeasurementEnable"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["02"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["02"]["description"] = "FrameDelayMeasurementOneWayTwoWay"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["03"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["03"]["description"] = "FrameDelayMeasurementTransmissionPeriodicity"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["03"]["datatype"] = "ushort"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["description"] = "FrameLossMeasurement"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["datatype"] = "aggregate"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["01"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["01"]["description"] = "FrameLossMeasurementEnable"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["02"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["02"]["description"] = "FrameLossMeasurementTransmissionPeriodicity"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["26"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["26"]["description"] = "L2VPNDSID"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["26"]["hex"] = "1a"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["26"]["datatype"] = "uint24"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["26"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["43"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["43"]["description"] = "VendorSpecificL2VPNSubtype"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["43"]["hex"] = "2b"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["43"]["datatype"] = "aggregate"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["43"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["43"]["subTlvs"]["08"] = {}
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["43"]["subTlvs"]["08"]["description"] = "VendorIdentifier"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["43"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["43"]["subTlvs"]["08"]["datatype"] = "hexstr"
DocsisTlvs["43"]["subTlvs"]["05"]["subTlvs"]["43"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["06"] = {}
DocsisTlvs["43"]["subTlvs"]["06"]["description"] = "ExtendedCMTSMICConfiguration"
DocsisTlvs["43"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["43"]["subTlvs"]["06"]["datatype"] = "aggregate"
DocsisTlvs["43"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["06"]["subTlvs"]["01"] = {}
DocsisTlvs["43"]["subTlvs"]["06"]["subTlvs"]["01"]["description"] = "ExtendedCMTSMICHMACDigestType"
DocsisTlvs["43"]["subTlvs"]["06"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["43"]["subTlvs"]["06"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["43"]["subTlvs"]["06"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["06"]["subTlvs"]["02"] = {}
DocsisTlvs["43"]["subTlvs"]["06"]["subTlvs"]["02"]["description"] = "ExtendedCMTSMICHMACBitmap"
DocsisTlvs["43"]["subTlvs"]["06"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["43"]["subTlvs"]["06"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["43"]["subTlvs"]["06"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["06"]["subTlvs"]["03"] = {}
DocsisTlvs["43"]["subTlvs"]["06"]["subTlvs"]["03"]["description"] = "ExtendedCMTSMICHMACDigest"
DocsisTlvs["43"]["subTlvs"]["06"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["43"]["subTlvs"]["06"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["43"]["subTlvs"]["06"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["07"] = {}
DocsisTlvs["43"]["subTlvs"]["07"]["description"] = "SAVAuthorizationEncoding"
DocsisTlvs["43"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["43"]["subTlvs"]["07"]["datatype"] = "aggregate"
DocsisTlvs["43"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["07"]["subTlvs"]["01"] = {}
DocsisTlvs["43"]["subTlvs"]["07"]["subTlvs"]["01"]["description"] = "SAVGroupName"
DocsisTlvs["43"]["subTlvs"]["07"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["43"]["subTlvs"]["07"]["subTlvs"]["01"]["datatype"] = "string"
DocsisTlvs["43"]["subTlvs"]["07"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["07"]["subTlvs"]["02"] = {}
DocsisTlvs["43"]["subTlvs"]["07"]["subTlvs"]["02"]["description"] = "SAVStaticPrefixRule"
DocsisTlvs["43"]["subTlvs"]["07"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["43"]["subTlvs"]["07"]["subTlvs"]["02"]["datatype"] = "aggregate"
DocsisTlvs["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["01"] = {}
DocsisTlvs["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["01"]["description"] = "SAVStaticPrefixAddress"
DocsisTlvs["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["01"]["datatype"] = "ip_ip6"
DocsisTlvs["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["02"] = {}
DocsisTlvs["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["02"]["description"] = "SAVStaticPrefixLength"
DocsisTlvs["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["08"] = {}
DocsisTlvs["43"]["subTlvs"]["08"]["description"] = "VendorIdentifier"
DocsisTlvs["43"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["43"]["subTlvs"]["08"]["datatype"] = "hexstr"
DocsisTlvs["43"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["09"] = {}
DocsisTlvs["43"]["subTlvs"]["09"]["description"] = "CMAttributeMasks"
DocsisTlvs["43"]["subTlvs"]["09"]["hex"] = "09"
DocsisTlvs["43"]["subTlvs"]["09"]["datatype"] = "aggregate"
DocsisTlvs["43"]["subTlvs"]["09"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["09"]["subTlvs"]["01"] = {}
DocsisTlvs["43"]["subTlvs"]["09"]["subTlvs"]["01"]["description"] = "CMDownstreamRequiredAttributeMask"
DocsisTlvs["43"]["subTlvs"]["09"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["43"]["subTlvs"]["09"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["43"]["subTlvs"]["09"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["09"]["subTlvs"]["02"] = {}
DocsisTlvs["43"]["subTlvs"]["09"]["subTlvs"]["02"]["description"] = "CMDownstreamForbiddenAttributeMask"
DocsisTlvs["43"]["subTlvs"]["09"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["43"]["subTlvs"]["09"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["43"]["subTlvs"]["09"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["09"]["subTlvs"]["03"] = {}
DocsisTlvs["43"]["subTlvs"]["09"]["subTlvs"]["03"]["description"] = "CMUpstreamRequiredAttributeMask"
DocsisTlvs["43"]["subTlvs"]["09"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["43"]["subTlvs"]["09"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["43"]["subTlvs"]["09"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["09"]["subTlvs"]["04"] = {}
DocsisTlvs["43"]["subTlvs"]["09"]["subTlvs"]["04"]["description"] = "CMUpstreamForbiddenAttributeMask"
DocsisTlvs["43"]["subTlvs"]["09"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["43"]["subTlvs"]["09"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["43"]["subTlvs"]["09"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["09"]["subTlvs"]["05"] = {}
DocsisTlvs["43"]["subTlvs"]["09"]["subTlvs"]["05"]["description"] = "Unknown"
DocsisTlvs["43"]["subTlvs"]["09"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["43"]["subTlvs"]["09"]["subTlvs"]["05"]["datatype"] = "unknown"
DocsisTlvs["43"]["subTlvs"]["09"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["09"]["subTlvs"]["06"] = {}
DocsisTlvs["43"]["subTlvs"]["09"]["subTlvs"]["06"]["description"] = "Unknown"
DocsisTlvs["43"]["subTlvs"]["09"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["43"]["subTlvs"]["09"]["subTlvs"]["06"]["datatype"] = "unknown"
DocsisTlvs["43"]["subTlvs"]["09"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["09"]["subTlvs"]["07"] = {}
DocsisTlvs["43"]["subTlvs"]["09"]["subTlvs"]["07"]["description"] = "Unknown"
DocsisTlvs["43"]["subTlvs"]["09"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["43"]["subTlvs"]["09"]["subTlvs"]["07"]["datatype"] = "unknown"
DocsisTlvs["43"]["subTlvs"]["09"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["10"] = {}
DocsisTlvs["43"]["subTlvs"]["10"]["description"] = "IPMulticastJoinAuthorization"
DocsisTlvs["43"]["subTlvs"]["10"]["hex"] = "0a"
DocsisTlvs["43"]["subTlvs"]["10"]["datatype"] = "aggregate"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["01"] = {}
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["01"]["description"] = "IPMulticastProfileName"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["01"]["datatype"] = "string"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["02"] = {}
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["02"]["description"] = "IPMulticastJoinAuthStaticSessionRule"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["02"]["datatype"] = "aggregate"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["01"] = {}
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["01"]["description"] = "MulticastRulePriority"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["02"] = {}
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["02"]["description"] = "AuthorizationAction"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["03"] = {}
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["03"]["description"] = "SourcePrefixAddress"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["03"]["datatype"] = "ip_ip6"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["04"] = {}
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["04"]["description"] = "SourcePrefixLength"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["04"]["datatype"] = "uchar"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["05"] = {}
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["05"]["description"] = "GroupPrefixAddress"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["05"]["datatype"] = "ip_ip6"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["06"] = {}
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["06"]["description"] = "GroupPrefixLength"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["06"]["datatype"] = "uchar"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["03"] = {}
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["03"]["description"] = "MaximumMulticastSessions"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["03"]["datatype"] = "ushort"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["03"]["subTlvs"] = {}



DocsisTlvs["43"]["subTlvs"]["11"] = {}
DocsisTlvs["43"]["subTlvs"]["11"]["description"] = "ServiceTypeIdentifier"
DocsisTlvs["43"]["subTlvs"]["11"]["hex"] = "0b"
DocsisTlvs["43"]["subTlvs"]["11"]["datatype"] = "string"
DocsisTlvs["43"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["12"] = {}
DocsisTlvs["43"]["subTlvs"]["12"]["description"] = "DEMARCAutoConfiguration"
DocsisTlvs["43"]["subTlvs"]["12"]["hex"] = "0c"
DocsisTlvs["43"]["subTlvs"]["12"]["datatype"] = "aggregate"
DocsisTlvs["43"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["12"]["subTlvs"]["01"] = {}
DocsisTlvs["43"]["subTlvs"]["12"]["subTlvs"]["01"]["description"] = "DACDisableEnableConfig"
DocsisTlvs["43"]["subTlvs"]["12"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["43"]["subTlvs"]["12"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["43"]["subTlvs"]["12"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["12"]["subTlvs"]["02"] = {}
DocsisTlvs["43"]["subTlvs"]["12"]["subTlvs"]["02"]["description"] = "CMIMEncoding"
DocsisTlvs["43"]["subTlvs"]["12"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["43"]["subTlvs"]["12"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["43"]["subTlvs"]["12"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["12"]["subTlvs"]["03"] = {}
DocsisTlvs["43"]["subTlvs"]["12"]["subTlvs"]["03"]["description"] = "UpstreamServiceClassName"
DocsisTlvs["43"]["subTlvs"]["12"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["43"]["subTlvs"]["12"]["subTlvs"]["03"]["datatype"] = "strzero"
DocsisTlvs["43"]["subTlvs"]["12"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["12"]["subTlvs"]["04"] = {}
DocsisTlvs["43"]["subTlvs"]["12"]["subTlvs"]["04"]["description"] = "DownstreamServiceClassName"
DocsisTlvs["43"]["subTlvs"]["12"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["43"]["subTlvs"]["12"]["subTlvs"]["04"]["datatype"] = "strzero"
DocsisTlvs["43"]["subTlvs"]["12"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["65"] = {}
DocsisTlvs["43"]["subTlvs"]["65"]["description"] = "dunno"
DocsisTlvs["43"]["subTlvs"]["65"]["hex"] = "41"
DocsisTlvs["43"]["subTlvs"]["65"]["datatype"] = "unknown"
DocsisTlvs["43"]["subTlvs"]["65"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["161"] = {}
DocsisTlvs["43"]["subTlvs"]["161"]["description"] = "vendor specif"
DocsisTlvs["43"]["subTlvs"]["161"]["hex"] = "a1"
DocsisTlvs["43"]["subTlvs"]["161"]["datatype"] = "unknown"
DocsisTlvs["43"]["subTlvs"]["161"]["subTlvs"] = {}

DocsisTlvs["45"] = {}
DocsisTlvs["45"]["description"] = "DUTFiltering"
DocsisTlvs["45"]["hex"] = "2d"
DocsisTlvs["45"]["datatype"] = "aggregate"
DocsisTlvs["45"]["subTlvs"] = {}

DocsisTlvs["45"]["subTlvs"]["01"] = {}
DocsisTlvs["45"]["subTlvs"]["01"]["description"] = "DUTControl"
DocsisTlvs["45"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["45"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["45"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["45"]["subTlvs"]["02"] = {}
DocsisTlvs["45"]["subTlvs"]["02"]["description"] = "DUTCMIM"
DocsisTlvs["45"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["45"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["45"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["46"] = {}
DocsisTlvs["46"]["description"] = "unknown"
DocsisTlvs["46"]["hex"] = "2e"
DocsisTlvs["46"]["datatype"] = "unknown"
DocsisTlvs["46"]["subTlvs"] = {}

DocsisTlvs["48"] = {}
DocsisTlvs["48"]["description"] = "Receive Channel Profile"
DocsisTlvs["48"]["hex"] = "30"
DocsisTlvs["48"]["datatype"] = "aggregate"
DocsisTlvs["48"]["subTlvs"] = {}

DocsisTlvs["48"]["subTlvs"]["01"] = {}
DocsisTlvs["48"]["subTlvs"]["01"]["description"] = "RCP-ID"
DocsisTlvs["48"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["48"]["subTlvs"]["01"]["datatype"] = "(encode_uchar_list)"
DocsisTlvs["48"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["48"]["subTlvs"]["10"] = {}
DocsisTlvs["48"]["subTlvs"]["10"]["description"] = "Unknown"
DocsisTlvs["48"]["subTlvs"]["10"]["hex"] = "0a"
DocsisTlvs["48"]["subTlvs"]["10"]["datatype"] = "unknown"
DocsisTlvs["48"]["subTlvs"]["10"]["subTlvs"] = {}


DocsisTlvs["48"]["subTlvs"]["14"] = {}
DocsisTlvs["48"]["subTlvs"]["14"]["description"] = "Unknown"
DocsisTlvs["48"]["subTlvs"]["14"]["hex"] = "0e"
DocsisTlvs["48"]["subTlvs"]["14"]["datatype"] = "unknown"
DocsisTlvs["48"]["subTlvs"]["14"]["subTlvs"] = {}

DocsisTlvs["48"]["subTlvs"]["34"] = {}
DocsisTlvs["48"]["subTlvs"]["34"]["description"] = "Unknown"
DocsisTlvs["48"]["subTlvs"]["34"]["hex"] = "22"
DocsisTlvs["48"]["subTlvs"]["34"]["datatype"] = "unknown"
DocsisTlvs["48"]["subTlvs"]["34"]["subTlvs"] = {}


DocsisTlvs["48"]["subTlvs"]["48"] = {}
DocsisTlvs["48"]["subTlvs"]["48"]["description"] = "Unknown"
DocsisTlvs["48"]["subTlvs"]["48"]["hex"] = "30"
DocsisTlvs["48"]["subTlvs"]["48"]["datatype"] = "unknown"
DocsisTlvs["48"]["subTlvs"]["48"]["subTlvs"] = {}

DocsisTlvs["48"]["subTlvs"]["51"] = {}
DocsisTlvs["48"]["subTlvs"]["51"]["description"] = "Unknown"
DocsisTlvs["48"]["subTlvs"]["51"]["hex"] = "33"
DocsisTlvs["48"]["subTlvs"]["51"]["datatype"] = "unknown"
DocsisTlvs["48"]["subTlvs"]["51"]["subTlvs"] = {}

DocsisTlvs["48"]["subTlvs"]["54"] = {}
DocsisTlvs["48"]["subTlvs"]["54"]["description"] = "Unknown"
DocsisTlvs["48"]["subTlvs"]["54"]["hex"] = "36"
DocsisTlvs["48"]["subTlvs"]["54"]["datatype"] = "unknown"
DocsisTlvs["48"]["subTlvs"]["54"]["subTlvs"] = {}

DocsisTlvs["48"]["subTlvs"]["80"] = {}
DocsisTlvs["48"]["subTlvs"]["80"]["description"] = "Unknown"
DocsisTlvs["48"]["subTlvs"]["80"]["hex"] = "50"
DocsisTlvs["48"]["subTlvs"]["80"]["datatype"] = "unknown"
DocsisTlvs["48"]["subTlvs"]["80"]["subTlvs"] = {}

DocsisTlvs["48"]["subTlvs"]["83"] = {}
DocsisTlvs["48"]["subTlvs"]["83"]["description"] = "Unknown"
DocsisTlvs["48"]["subTlvs"]["83"]["hex"] = "53"
DocsisTlvs["48"]["subTlvs"]["83"]["datatype"] = "unknown"
DocsisTlvs["48"]["subTlvs"]["83"]["subTlvs"] = {}



DocsisTlvs["48"]["subTlvs"]["97"] = {}
DocsisTlvs["48"]["subTlvs"]["97"]["description"] = "Unknown"
DocsisTlvs["48"]["subTlvs"]["97"]["hex"] = "61"
DocsisTlvs["48"]["subTlvs"]["97"]["datatype"] = "unknown"
DocsisTlvs["48"]["subTlvs"]["97"]["subTlvs"] = {}

DocsisTlvs["48"]["subTlvs"]["118"] = {}
DocsisTlvs["48"]["subTlvs"]["118"]["description"] = "Unknown"
DocsisTlvs["48"]["subTlvs"]["118"]["hex"] = "76"
DocsisTlvs["48"]["subTlvs"]["118"]["datatype"] = "unknown"
DocsisTlvs["48"]["subTlvs"]["118"]["subTlvs"] = {}


DocsisTlvs["49"] = {}
DocsisTlvs["49"]["description"] = "unknown"
DocsisTlvs["49"]["hex"] = "31"
DocsisTlvs["49"]["datatype"] = "unknown"
DocsisTlvs["49"]["subTlvs"] = {}

DocsisTlvs["50"] = {}
DocsisTlvs["50"]["description"] = "unknown"
DocsisTlvs["50"]["hex"] = "32"
DocsisTlvs["50"]["datatype"] = "unknown"
DocsisTlvs["50"]["subTlvs"] = {}

DocsisTlvs["51"] = {}
DocsisTlvs["51"]["description"] = "unknown"
DocsisTlvs["51"]["hex"] = "33"
DocsisTlvs["51"]["datatype"] = "unknown"
DocsisTlvs["51"]["subTlvs"] = {}


DocsisTlvs["52"] = {}
DocsisTlvs["52"]["description"] = "unknown"
DocsisTlvs["52"]["hex"] = "34"
DocsisTlvs["52"]["datatype"] = "unknown"
DocsisTlvs["52"]["subTlvs"] = {}

DocsisTlvs["53"] = {}
DocsisTlvs["53"]["description"] = "SNMPv1v2cCoexistenceConfig"
DocsisTlvs["53"]["hex"] = "35"
DocsisTlvs["53"]["datatype"] = "aggregate"
DocsisTlvs["53"]["subTlvs"] = {}

DocsisTlvs["53"]["subTlvs"]["01"] = {}
DocsisTlvs["53"]["subTlvs"]["01"]["description"] = "SNMPv1v2cCommunityName"
DocsisTlvs["53"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["53"]["subTlvs"]["01"]["datatype"] = "string"
DocsisTlvs["53"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["53"]["subTlvs"]["02"] = {}
DocsisTlvs["53"]["subTlvs"]["02"]["description"] = "SNMPv1v2cTransportAddressAccess"
DocsisTlvs["53"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["53"]["subTlvs"]["02"]["datatype"] = "aggregate"
DocsisTlvs["53"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["53"]["subTlvs"]["02"]["subTlvs"]["01"] = {}
DocsisTlvs["53"]["subTlvs"]["02"]["subTlvs"]["01"]["description"] = "SNMPv1v2cTransportAddress"
DocsisTlvs["53"]["subTlvs"]["02"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["53"]["subTlvs"]["02"]["subTlvs"]["01"]["datatype"] = "(encode_ip_ip6_port)"
DocsisTlvs["53"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["53"]["subTlvs"]["02"]["subTlvs"]["02"] = {}
DocsisTlvs["53"]["subTlvs"]["02"]["subTlvs"]["02"]["description"] = "SNMPv1v2cTransportAddressMask"
DocsisTlvs["53"]["subTlvs"]["02"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["53"]["subTlvs"]["02"]["subTlvs"]["02"]["datatype"] = "(encode_ip_ip6_port)"
DocsisTlvs["53"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["53"]["subTlvs"]["03"] = {}
DocsisTlvs["53"]["subTlvs"]["03"]["description"] = "SNMPv1v2cAccessViewType"
DocsisTlvs["53"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["53"]["subTlvs"]["03"]["datatype"] = "uchar"
DocsisTlvs["53"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["53"]["subTlvs"]["04"] = {}
DocsisTlvs["53"]["subTlvs"]["04"]["description"] = "SNMPv1v2cAccessViewName"
DocsisTlvs["53"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["53"]["subTlvs"]["04"]["datatype"] = "string"
DocsisTlvs["53"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["53"]["subTlvs"]["50"] = {}
DocsisTlvs["53"]["subTlvs"]["50"]["description"] = "SNMPv1v2cAccessViewName"
DocsisTlvs["53"]["subTlvs"]["50"]["hex"] = "32"
DocsisTlvs["53"]["subTlvs"]["50"]["datatype"] = "string"
DocsisTlvs["53"]["subTlvs"]["50"]["subTlvs"] = {}

DocsisTlvs["54"] = {}
DocsisTlvs["54"]["description"] = "SNMPv3AccessViewConfiguration"
DocsisTlvs["54"]["hex"] = "36"
DocsisTlvs["54"]["datatype"] = "aggregate"
DocsisTlvs["54"]["subTlvs"] = {}

DocsisTlvs["54"]["subTlvs"]["01"] = {}
DocsisTlvs["54"]["subTlvs"]["01"]["description"] = "SNMPv3AccessViewName"
DocsisTlvs["54"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["54"]["subTlvs"]["01"]["datatype"] = "string"
DocsisTlvs["54"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["54"]["subTlvs"]["02"] = {}
DocsisTlvs["54"]["subTlvs"]["02"]["description"] = "SNMPv3AccessViewSubtree"
DocsisTlvs["54"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["54"]["subTlvs"]["02"]["datatype"] = "(encode_oid)"
DocsisTlvs["54"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["54"]["subTlvs"]["03"] = {}
DocsisTlvs["54"]["subTlvs"]["03"]["description"] = "SNMPv3AccessViewMask"
DocsisTlvs["54"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["54"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["54"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["54"]["subTlvs"]["04"] = {}
DocsisTlvs["54"]["subTlvs"]["04"]["description"] = "SNMPv3AccessViewType"
DocsisTlvs["54"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["54"]["subTlvs"]["04"]["datatype"] = "uchar"
DocsisTlvs["54"]["subTlvs"]["04"]["subTlvs"] = {}


DocsisTlvs["54"]["subTlvs"]["52"] = {}
DocsisTlvs["54"]["subTlvs"]["52"]["description"] = "unknown"
DocsisTlvs["54"]["subTlvs"]["52"]["hex"] = "34"
DocsisTlvs["54"]["subTlvs"]["52"]["datatype"] = "unknown"
DocsisTlvs["54"]["subTlvs"]["52"]["subTlvs"] = {}

DocsisTlvs["54"]["subTlvs"]["54"] = {}
DocsisTlvs["54"]["subTlvs"]["54"]["description"] = "unknown"
DocsisTlvs["54"]["subTlvs"]["54"]["hex"] = "36"
DocsisTlvs["54"]["subTlvs"]["54"]["datatype"] = "unknown"
DocsisTlvs["54"]["subTlvs"]["54"]["subTlvs"] = {}

DocsisTlvs["55"] = {}
DocsisTlvs["55"]["description"] = "SNMPCPEAccessControl"
DocsisTlvs["55"]["hex"] = "37"
DocsisTlvs["55"]["datatype"] = "uchar"
DocsisTlvs["55"]["subTlvs"] = {}

DocsisTlvs["56"] = {}
DocsisTlvs["56"]["description"] = "ChannelAssignmentConfig"
DocsisTlvs["56"]["hex"] = "38"
DocsisTlvs["56"]["datatype"] = "aggregate"
DocsisTlvs["56"]["subTlvs"] = {}

DocsisTlvs["56"]["subTlvs"]["01"] = {}
DocsisTlvs["56"]["subTlvs"]["01"]["description"] = "CaTransmit"
DocsisTlvs["56"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["56"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["56"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["56"]["subTlvs"]["02"] = {}
DocsisTlvs["56"]["subTlvs"]["02"]["description"] = "CaReceive"
DocsisTlvs["56"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["56"]["subTlvs"]["02"]["datatype"] = "uint"
DocsisTlvs["56"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["56"]["subTlvs"]["46"] = {}
DocsisTlvs["56"]["subTlvs"]["46"]["description"] = "Unknown"
DocsisTlvs["56"]["subTlvs"]["46"]["hex"] = "2e"
DocsisTlvs["56"]["subTlvs"]["46"]["datatype"] = "unknown"
DocsisTlvs["56"]["subTlvs"]["46"]["subTlvs"] = {}

DocsisTlvs["56"]["subTlvs"]["52"] = {}
DocsisTlvs["56"]["subTlvs"]["52"]["description"] = "Unknown"
DocsisTlvs["56"]["subTlvs"]["52"]["hex"] = "34"
DocsisTlvs["56"]["subTlvs"]["52"]["datatype"] = "unknown"
DocsisTlvs["56"]["subTlvs"]["52"]["subTlvs"] = {}

DocsisTlvs["56"]["subTlvs"]["67"] = {}
DocsisTlvs["56"]["subTlvs"]["67"]["description"] = "Unknown"
DocsisTlvs["56"]["subTlvs"]["67"]["hex"] = "43"
DocsisTlvs["56"]["subTlvs"]["67"]["datatype"] = "unknown"
DocsisTlvs["56"]["subTlvs"]["67"]["subTlvs"] = {}

DocsisTlvs["56"]["subTlvs"]["102"] = {}
DocsisTlvs["56"]["subTlvs"]["102"]["description"] = "Unknown"
DocsisTlvs["56"]["subTlvs"]["102"]["hex"] = "66"
DocsisTlvs["56"]["subTlvs"]["102"]["datatype"] = "unknown"
DocsisTlvs["56"]["subTlvs"]["102"]["subTlvs"] = {}


DocsisTlvs["57"] = {}
DocsisTlvs["57"]["description"] = "unknown"
DocsisTlvs["57"]["hex"] = "39"
DocsisTlvs["57"]["datatype"] = "unknown"
DocsisTlvs["57"]["subTlvs"] = {}

DocsisTlvs["58"] = {}
DocsisTlvs["58"]["description"] = "SwUpgradeServer6"
DocsisTlvs["58"]["hex"] = "3a"
DocsisTlvs["58"]["datatype"] = "encode_ip"
DocsisTlvs["58"]["subTlvs"] = {}

DocsisTlvs["59"] = {}
DocsisTlvs["59"]["description"] = "TFTPProvisionedModemIPv6Address"
DocsisTlvs["59"]["hex"] = "3b"
DocsisTlvs["59"]["datatype"] = "encode_ip"
DocsisTlvs["59"]["subTlvs"] = {}

DocsisTlvs["60"] = {}
DocsisTlvs["60"]["description"] = "UpstreamDropPacketClassification"
DocsisTlvs["60"]["hex"] = "3c"
DocsisTlvs["60"]["datatype"] = "aggregate"
DocsisTlvs["60"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["01"] = {}
DocsisTlvs["60"]["subTlvs"]["01"]["description"] = "ClassifierReference"
DocsisTlvs["60"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["60"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["60"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["02"] = {}
DocsisTlvs["60"]["subTlvs"]["02"]["description"] = "ClassifierIdentifier"
DocsisTlvs["60"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["60"]["subTlvs"]["02"]["datatype"] = "ushort"
DocsisTlvs["60"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["05"] = {}
DocsisTlvs["60"]["subTlvs"]["05"]["description"] = "RulePriority"
DocsisTlvs["60"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["60"]["subTlvs"]["05"]["datatype"] = "uchar"
DocsisTlvs["60"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["07"] = {}
DocsisTlvs["60"]["subTlvs"]["07"]["description"] = "DynamicServiceChangeAction"
DocsisTlvs["60"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["60"]["subTlvs"]["07"]["datatype"] = "uchar"
DocsisTlvs["60"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["09"] = {}
DocsisTlvs["60"]["subTlvs"]["09"]["description"] = "IPv4PacketClassification"
DocsisTlvs["60"]["subTlvs"]["09"]["hex"] = "09"
DocsisTlvs["60"]["subTlvs"]["09"]["datatype"] = "aggregate"
DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["01"] = {}
DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["01"]["description"] = "IPv4Tos"
DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["02"] = {}
DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["02"]["description"] = "IPProtocol"
DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["02"]["datatype"] = "ushort"
DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["03"] = {}
DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["03"]["description"] = "IPv4SourceAddress"
DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["03"]["datatype"] = "encode_ip"
DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["04"] = {}
DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["04"]["description"] = "IPv4SourceMask"
DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["04"]["datatype"] = "encode_ip"
DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["05"] = {}
DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["05"]["description"] = "IPv4DestinationAddress"
DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["05"]["datatype"] = "encode_ip"
DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["06"] = {}
DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["06"]["description"] = "IPv4DestinationMask"
DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["06"]["datatype"] = "encode_ip"
DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["07"] = {}
DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["07"]["description"] = "SourcePortStart"
DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["07"]["datatype"] = "ushort"
DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["08"] = {}
DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["08"]["description"] = "SourcePortEnd"
DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["08"]["datatype"] = "ushort"
DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["09"] = {}
DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["09"]["description"] = "DestinationPortStart"
DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["09"]["hex"] = "09"
DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["09"]["datatype"] = "ushort"
DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["09"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["10"] = {}
DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["10"]["description"] = "DestinationPortEnd"
DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["10"]["hex"] = "0a"
DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["10"]["datatype"] = "ushort"
DocsisTlvs["60"]["subTlvs"]["09"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["10"] = {}
DocsisTlvs["60"]["subTlvs"]["10"]["description"] = "EthernetLLCPacketClassification"
DocsisTlvs["60"]["subTlvs"]["10"]["hex"] = "0a"
DocsisTlvs["60"]["subTlvs"]["10"]["datatype"] = "aggregate"
DocsisTlvs["60"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["10"]["subTlvs"]["01"] = {}
DocsisTlvs["60"]["subTlvs"]["10"]["subTlvs"]["01"]["description"] = "DestinationMACAddress"
DocsisTlvs["60"]["subTlvs"]["10"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["60"]["subTlvs"]["10"]["subTlvs"]["01"]["datatype"] = "(encode_ethermask)"
DocsisTlvs["60"]["subTlvs"]["10"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["10"]["subTlvs"]["02"] = {}
DocsisTlvs["60"]["subTlvs"]["10"]["subTlvs"]["02"]["description"] = "SourceMACAddress"
DocsisTlvs["60"]["subTlvs"]["10"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["60"]["subTlvs"]["10"]["subTlvs"]["02"]["datatype"] = "ether"
DocsisTlvs["60"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["10"]["subTlvs"]["03"] = {}
DocsisTlvs["60"]["subTlvs"]["10"]["subTlvs"]["03"]["description"] = "EthertypeDSAPMacType"
DocsisTlvs["60"]["subTlvs"]["10"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["60"]["subTlvs"]["10"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["10"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["11"] = {}
DocsisTlvs["60"]["subTlvs"]["11"]["description"] = "IEEE8021PQPacketClassification"
DocsisTlvs["60"]["subTlvs"]["11"]["hex"] = "0b"
DocsisTlvs["60"]["subTlvs"]["11"]["datatype"] = "aggregate"
DocsisTlvs["60"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["11"]["subTlvs"]["01"] = {}
DocsisTlvs["60"]["subTlvs"]["11"]["subTlvs"]["01"]["description"] = "UserPriority"
DocsisTlvs["60"]["subTlvs"]["11"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["60"]["subTlvs"]["11"]["subTlvs"]["01"]["datatype"] = "char_list"
DocsisTlvs["60"]["subTlvs"]["11"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["11"]["subTlvs"]["02"] = {}
DocsisTlvs["60"]["subTlvs"]["11"]["subTlvs"]["02"]["description"] = "VlanID"
DocsisTlvs["60"]["subTlvs"]["11"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["60"]["subTlvs"]["11"]["subTlvs"]["02"]["datatype"] = "ushort"
DocsisTlvs["60"]["subTlvs"]["11"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["12"] = {}
DocsisTlvs["60"]["subTlvs"]["12"]["description"] = "IPv6PacketClassification"
DocsisTlvs["60"]["subTlvs"]["12"]["hex"] = "0c"
DocsisTlvs["60"]["subTlvs"]["12"]["datatype"] = "aggregate"
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["01"] = {}
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["01"]["description"] = "IPv6TrafficClassRangeandMask"
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["02"] = {}
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["02"]["description"] = "IPv6FlowLabel"
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["03"] = {}
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["03"]["description"] = "IPv6NextHeaderType"
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["03"]["datatype"] = "ushort"
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["04"] = {}
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["04"]["description"] = "IPv6SourceAddress"
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["04"]["datatype"] = "encode_ip"
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["05"] = {}
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["05"]["description"] = "IPv6SourcePrefixLength"
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["05"]["datatype"] = "uchar"
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["06"] = {}
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["06"]["description"] = "IPv6DestinationAddress"
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["06"]["datatype"] = "encode_ip"
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["07"] = {}
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["07"]["description"] = "IPv6DestinationPrefixLength"
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["07"]["datatype"] = "uchar"
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["13"] = {}
DocsisTlvs["60"]["subTlvs"]["13"]["description"] = "CMInterfaceMaskEncoding"
DocsisTlvs["60"]["subTlvs"]["13"]["hex"] = "0d"
DocsisTlvs["60"]["subTlvs"]["13"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["13"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["14"] = {}
DocsisTlvs["60"]["subTlvs"]["14"]["description"] = "STagCTagFrameClassification"
DocsisTlvs["60"]["subTlvs"]["14"]["hex"] = "0e"
DocsisTlvs["60"]["subTlvs"]["14"]["datatype"] = "aggregate"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["01"] = {}
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["01"]["description"] = "STPID"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["02"] = {}
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["02"]["description"] = "SVID"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["03"] = {}
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["03"]["description"] = "SPCP"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["04"] = {}
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["04"]["description"] = "SDEI"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["05"] = {}
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["05"]["description"] = "CTPID"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["05"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["06"] = {}
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["06"]["description"] = "CVID"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["06"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["07"] = {}
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["07"]["description"] = "CPCP"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["07"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["08"] = {}
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["08"]["description"] = "CCFI"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["08"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["09"] = {}
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["09"]["description"] = "STCI"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["09"]["hex"] = "09"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["09"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["09"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["10"] = {}
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["10"]["description"] = "CTCI"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["10"]["hex"] = "0a"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["10"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["15"] = {}
DocsisTlvs["60"]["subTlvs"]["15"]["description"] = "IEEE8021ahPacketClassification"
DocsisTlvs["60"]["subTlvs"]["15"]["hex"] = "0f"
DocsisTlvs["60"]["subTlvs"]["15"]["datatype"] = "aggregate"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["01"] = {}
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["01"]["description"] = "ITPID"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["02"] = {}
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["02"]["description"] = "ISID"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["03"] = {}
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["03"]["description"] = "ITCI"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["04"] = {}
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["04"]["description"] = "IPCP"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["05"] = {}
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["05"]["description"] = "IDEI"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["05"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["06"] = {}
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["06"]["description"] = "IUCA"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["06"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["07"] = {}
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["07"]["description"] = "BTPID"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["07"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["08"] = {}
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["08"]["description"] = "BTCI"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["08"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["09"] = {}
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["09"]["description"] = "BPCP"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["09"]["hex"] = "09"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["09"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["09"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["10"] = {}
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["10"]["description"] = "BDEI"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["10"]["hex"] = "0a"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["10"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["11"] = {}
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["11"]["description"] = "BVID"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["11"]["hex"] = "0b"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["11"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["12"] = {}
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["12"]["description"] = "BDA"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["12"]["hex"] = "0c"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["12"]["datatype"] = "ether"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["13"] = {}
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["13"]["description"] = "BSA"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["13"]["hex"] = "0d"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["13"]["datatype"] = "ether"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["13"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["16"] = {}
DocsisTlvs["60"]["subTlvs"]["16"]["description"] = "ICMPv4ICMPv6PacketClassification"
DocsisTlvs["60"]["subTlvs"]["16"]["hex"] = "10"
DocsisTlvs["60"]["subTlvs"]["16"]["datatype"] = "aggregate"
DocsisTlvs["60"]["subTlvs"]["16"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["16"]["subTlvs"]["01"] = {}
DocsisTlvs["60"]["subTlvs"]["16"]["subTlvs"]["01"]["description"] = "ICMPv4ICMPv6TypeStart"
DocsisTlvs["60"]["subTlvs"]["16"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["60"]["subTlvs"]["16"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["60"]["subTlvs"]["16"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["16"]["subTlvs"]["02"] = {}
DocsisTlvs["60"]["subTlvs"]["16"]["subTlvs"]["02"]["description"] = "ICMPv4ICMPv6TypeEnd"
DocsisTlvs["60"]["subTlvs"]["16"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["60"]["subTlvs"]["16"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["60"]["subTlvs"]["16"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["17"] = {}
DocsisTlvs["60"]["subTlvs"]["17"]["description"] = "MPLSClassificationEncoding"
DocsisTlvs["60"]["subTlvs"]["17"]["hex"] = "11"
DocsisTlvs["60"]["subTlvs"]["17"]["datatype"] = "aggregate"
DocsisTlvs["60"]["subTlvs"]["17"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["17"]["subTlvs"]["01"] = {}
DocsisTlvs["60"]["subTlvs"]["17"]["subTlvs"]["01"]["description"] = "MPLSTCbits"
DocsisTlvs["60"]["subTlvs"]["17"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["60"]["subTlvs"]["17"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["17"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["17"]["subTlvs"]["02"] = {}
DocsisTlvs["60"]["subTlvs"]["17"]["subTlvs"]["02"]["description"] = "MPLSLabel"
DocsisTlvs["60"]["subTlvs"]["17"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["60"]["subTlvs"]["17"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["17"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["description"] = "VendorSpecific"
DocsisTlvs["60"]["subTlvs"]["43"]["hex"] = "2b"
DocsisTlvs["60"]["subTlvs"]["43"]["datatype"] = "aggregate"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["01"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["01"]["description"] = "CMLoadBalancingPolicyID"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["01"]["datatype"] = "uint"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["02"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["02"]["description"] = "CMLoadBalancingPriority"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["02"]["datatype"] = "uint"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["03"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["03"]["description"] = "CMLoadBalancingGroupID"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["03"]["datatype"] = "uint"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["04"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["04"]["description"] = "CMRangingClassIDExtension"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["04"]["datatype"] = "ushort"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["description"] = "L2VPNEncoding"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["datatype"] = "aggregate"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["01"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["01"]["description"] = "VPNIdentifier"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["description"] = "NSIEncapsulation"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["datatype"] = "aggregate"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["01"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["01"]["description"] = "ServiceMultiplexingValueOther"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["01"]["datatype"] = "lenzero"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["02"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["02"]["description"] = "NSIEncapsulationSingleQTag"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["02"]["datatype"] = "ushort"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["03"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["03"]["description"] = "NSIEncapsulationDualQTag"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["03"]["datatype"] = "dual_qtag"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["description"] = "ServiceMultiplexingValueMPLSPW"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["datatype"] = "aggregate"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["01"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["01"]["description"] = "MPLSPseudowireID"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["01"]["datatype"] = "uint"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["02"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["02"]["description"] = "MPLSPeerIpAddress"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["02"]["datatype"] = "char_ip_ip6"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["03"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["03"]["description"] = "MPLSPseudowireType"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["03"]["datatype"] = "uchar"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["04"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["04"]["description"] = "MPLSBackupPseudowireID"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["04"]["datatype"] = "uint"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["05"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["05"]["description"] = "MPLSBackupPeerIpAddress"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["05"]["datatype"] = "char_ip_ip6"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["05"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["05"]["description"] = "ServiceMultiplexingValueL2TPv3Peer"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["05"]["datatype"] = "char_ip_ip6"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["description"] = "IEEE8021ahEncapsulation"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["datatype"] = "aggregate"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["01"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["01"]["description"] = "ITCIEncapsulation"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["02"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["02"]["description"] = "BDAEncapsulation"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["03"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["03"]["description"] = "BTCIEncapsulation"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["04"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["04"]["description"] = "ITPIDEncapsulation"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["05"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["05"]["description"] = "IPCPEncapsulation"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["05"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["06"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["06"]["description"] = "IDEIEncapsulation"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["06"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["07"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["07"]["description"] = "IUCAEncapsulation"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["07"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["08"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["08"]["description"] = "ISIDEncapsulation"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["08"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["09"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["09"]["description"] = "BTPIDEncapsulation"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["09"]["hex"] = "09"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["09"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["09"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["10"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["10"]["description"] = "BPCPEncapsulation"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["10"]["hex"] = "0a"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["10"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["11"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["11"]["description"] = "BDEIEncapsulation"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["11"]["hex"] = "0b"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["11"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["12"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["12"]["description"] = "BVIDEncapsulation"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["12"]["hex"] = "0c"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["12"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["08"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["08"]["description"] = "ServiceMultiplexingValueIEEE8021adSTPID"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["08"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["02"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["03"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["03"]["description"] = "eSAFEDHCPSnooping"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["04"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["04"]["description"] = "CMInterfaceMaskCMIMSubtype"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["05"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["05"]["description"] = "AttachmentGroupID"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["05"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["06"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["06"]["description"] = "SourceAttachmentIndividualID"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["06"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["07"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["07"]["description"] = "TargetAttachmentIndividualID"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["07"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["08"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["08"]["description"] = "IngressUserPriority"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["08"]["datatype"] = "uchar"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["09"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["09"]["description"] = "UserPriorityRange"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["09"]["hex"] = "09"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["09"]["datatype"] = "char_list"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["09"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["10"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["10"]["description"] = "L2VPNSADescriptorSubtype"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["10"]["hex"] = "0a"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["10"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["12"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["12"]["description"] = "PseudowireType"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["12"]["hex"] = "0c"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["12"]["datatype"] = "uchar"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["13"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["13"]["description"] = "L2VPNMode"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["13"]["hex"] = "0d"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["13"]["datatype"] = "uchar"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["13"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["description"] = "TPIDTranslation"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["hex"] = "0e"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["datatype"] = "aggregate"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["01"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["01"]["description"] = "UpstreamTPIDTranslation"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["02"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["02"]["description"] = "DownstreamTPIDTranslation"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["03"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["03"]["description"] = "UpstreamSTPIDTranslation"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["04"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["04"]["description"] = "DownstreamSTPIDTranslation"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["05"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["05"]["description"] = "UpstreamBTPIDTranslation"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["05"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["06"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["06"]["description"] = "DownstreamBTPIDTranslation"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["06"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["07"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["07"]["description"] = "UpstreamITPIDTranslation"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["07"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["08"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["08"]["description"] = "DownstreamITPIDTranslation"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["08"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["14"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["description"] = "L2CPProcessing"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["hex"] = "0f"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["datatype"] = "aggregate"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["01"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["01"]["description"] = "L2CPTunnelMode"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["02"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["02"]["description"] = "L2CPDMACAddress"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["02"]["datatype"] = "ether"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["03"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["03"]["description"] = "L2CPOverwrotingDMACAddress"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["03"]["datatype"] = "ether"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["15"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["16"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["16"]["description"] = "DACDisableEnableConfiguration"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["16"]["hex"] = "10"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["16"]["datatype"] = "uchar"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["16"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["18"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["18"]["description"] = "PseudowireClass"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["18"]["hex"] = "12"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["18"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["18"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["description"] = "ServiceDelimiter"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["hex"] = "13"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["datatype"] = "aggregate"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["01"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["01"]["description"] = "CVIDDelimiter"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["02"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["02"]["description"] = "SVIDDelimiter"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["03"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["03"]["description"] = "ISIDDelimiter"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["04"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["04"]["description"] = "BVIDDelimiter"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["19"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["description"] = "VirtualSwitchInstanceEncoding"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["hex"] = "14"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["datatype"] = "aggregate"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["01"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["01"]["description"] = "VPLSClass"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["02"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["02"]["description"] = "ETreeRole"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["03"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["03"]["description"] = "ETreeRootVID"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["04"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["04"]["description"] = "ETreeLeafVID"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["20"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["description"] = "BGPAttribute"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["hex"] = "15"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["datatype"] = "aggregate"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["01"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["01"]["description"] = "BGPVPNID"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["01"]["datatype"] = "uint"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["02"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["02"]["description"] = "RouteDistinguisher"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["03"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["03"]["description"] = "RouteTargetImport"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["04"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["04"]["description"] = "RouteTargetExport"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["05"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["05"]["description"] = "CEIDVEID"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["05"]["datatype"] = "ushort"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["21"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["23"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["23"]["description"] = "PseudowireSignaling"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["23"]["hex"] = "17"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["23"]["datatype"] = "uchar"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["23"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["description"] = "SOAMSubtype"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["hex"] = "18"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["datatype"] = "aggregate"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["description"] = "MEPConfiguration"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["datatype"] = "aggregate"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["01"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["01"]["description"] = "MDLevel"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["02"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["02"]["description"] = "MDName"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["02"]["datatype"] = "string"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["03"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["03"]["description"] = "MAName"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["03"]["datatype"] = "string"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["04"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["04"]["description"] = "MEPID"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["04"]["datatype"] = "ushort"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["01"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["description"] = "RemoteMEPConfiguration"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["datatype"] = "aggregate"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["01"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["01"]["description"] = "RemoteMDLevel"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["02"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["02"]["description"] = "RemoteMDName"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["02"]["datatype"] = "string"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["03"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["03"]["description"] = "RemoteMAName"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["03"]["datatype"] = "string"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["04"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["04"]["description"] = "RemoteMEPID"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["04"]["datatype"] = "ushort"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["description"] = "FaultManagementConfiguration"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["datatype"] = "aggregate"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["01"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["01"]["description"] = "ContinuityCheckMessages"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["02"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["02"]["description"] = "LoopbackFunction"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["03"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["03"]["description"] = "LinktraceFunction"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["03"]["datatype"] = "uchar"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["03"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["description"] = "PerformanceManagementConfiguration"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["datatype"] = "aggregate"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["description"] = "FrameDelayMeasurement"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["datatype"] = "aggregate"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["01"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["01"]["description"] = "FrameDelayMeasurementEnable"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["02"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["02"]["description"] = "FrameDelayMeasurementOneWayTwoWay"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["03"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["03"]["description"] = "FrameDelayMeasurementTransmissionPeriodicity"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["03"]["datatype"] = "ushort"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["01"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["description"] = "FrameLossMeasurement"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["datatype"] = "aggregate"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["01"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["01"]["description"] = "FrameLossMeasurementEnable"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["02"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["02"]["description"] = "FrameLossMeasurementTransmissionPeriodicity"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["24"]["subTlvs"]["04"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["26"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["26"]["description"] = "L2VPNDSID"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["26"]["hex"] = "1a"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["26"]["datatype"] = "uint24"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["26"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["description"] = "VendorSpecificL2VPNSubtype"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["hex"] = "2b"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["datatype"] = "aggregate"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["subTlvs"]["08"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["subTlvs"]["08"]["description"] = "VendorIdentifier"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["subTlvs"]["08"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["05"]["subTlvs"]["43"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["06"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["06"]["description"] = "ExtendedCMTSMICConfigurationSetting"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["06"]["datatype"] = "aggregate"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["01"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["01"]["description"] = "ExtendedCMTSMICHMACtype"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["02"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["02"]["description"] = "ExtendedCMTSMICBitmap"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["03"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["03"]["description"] = "ExplicitExtendedCMTSMICDigest"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["06"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["07"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["07"]["description"] = "SAVAuthorizationEncoding"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["07"]["datatype"] = "aggregate"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["01"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["01"]["description"] = "SAVGroupName"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["01"]["datatype"] = "string"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["description"] = "SAVStaticPrefixRule"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["datatype"] = "aggregate"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["01"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["01"]["description"] = "SAVStaticPrefixAddress"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["01"]["datatype"] = "ip_ip6"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["02"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["02"]["description"] = "SAVStaticPrefixLength"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["08"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["08"]["description"] = "VendorIdentifier"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["08"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["09"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["09"]["description"] = "CMAttributeMasks"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["09"]["hex"] = "09"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["09"]["datatype"] = "aggregate"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["01"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["01"]["description"] = "CMDownstreamRequiredAttributeMask"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["02"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["02"]["description"] = "CMDownstreamForbiddenAttributeMask"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["03"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["03"]["description"] = "CMUpstreamRequiredAttributeMask"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["04"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["04"]["description"] = "CMUpstreamForbiddenAttributeMask"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["04"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["09"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["description"] = "IPMulticastJoinAuthorization"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["hex"] = "0a"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["datatype"] = "aggregate"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["01"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["01"]["description"] = "IPMulticastProfileName"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["01"]["datatype"] = "string"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["description"] = "IPMulticastJoinAuthStaticSessionRule"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["datatype"] = "aggregate"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["01"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["01"]["description"] = "MulticastRulePriority"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["02"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["02"]["description"] = "AuthorizationAction"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["03"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["03"]["description"] = "SourcePrefixAddress"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["03"]["datatype"] = "ip_ip6"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["04"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["04"]["description"] = "SourcePrefixLength"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["04"]["datatype"] = "uchar"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["05"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["05"]["description"] = "GroupPrefixAddress"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["05"]["datatype"] = "ip_ip6"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["06"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["06"]["description"] = "GroupPrefixLength"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["06"]["datatype"] = "uchar"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["03"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["03"]["description"] = "MaximumMulticastSessions"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["03"]["datatype"] = "ushort"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["11"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["11"]["description"] = "ServiceTypeIdentifier"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["11"]["hex"] = "0b"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["11"]["datatype"] = "string"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"]["description"] = "DEMARCAutoConfiguration"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"]["hex"] = "0c"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"]["datatype"] = "aggregate"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["01"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["01"]["description"] = "DACDisableEnableConfig"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["02"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["02"]["description"] = "CMIMEncoding"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["03"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["03"]["description"] = "UpstreamServiceClassName"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["03"]["datatype"] = "strzero"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["04"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["04"]["description"] = "DownstreamServiceClassName"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["04"]["datatype"] = "strzero"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["61"] = {}
DocsisTlvs["61"]["description"] = "SubMgmtCPEIPv6PrefixList"
DocsisTlvs["61"]["hex"] = "3d"
DocsisTlvs["61"]["datatype"] = "(encode_ip6_prefix_list)"
DocsisTlvs["61"]["subTlvs"] = {}

DocsisTlvs["62"] = {}
DocsisTlvs["62"]["description"] = "UpstreamDropClassifierGroupID"
DocsisTlvs["62"]["hex"] = "3e"
DocsisTlvs["62"]["datatype"] = "char_list"
DocsisTlvs["62"]["subTlvs"] = {}

DocsisTlvs["63"] = {}
DocsisTlvs["63"]["description"] = "SubMgmtControl6"
DocsisTlvs["63"]["hex"] = "3f"
DocsisTlvs["63"]["datatype"] = "ushort"
DocsisTlvs["63"]["subTlvs"] = {}

DocsisTlvs["64"] = {}
DocsisTlvs["64"]["description"] = "CMTSStaticMulticastSessionEncodings"
DocsisTlvs["64"]["hex"] = "40"
DocsisTlvs["64"]["datatype"] = "aggregate"
DocsisTlvs["64"]["subTlvs"] = {}

DocsisTlvs["64"]["subTlvs"]["01"] = {}
DocsisTlvs["64"]["subTlvs"]["01"]["description"] = "CMTSStaticMulticastSessionGroup"
DocsisTlvs["64"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["64"]["subTlvs"]["01"]["datatype"] = "ip_ip6"
DocsisTlvs["64"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["64"]["subTlvs"]["02"] = {}
DocsisTlvs["64"]["subTlvs"]["02"]["description"] = "CMTSStaticMulticastSessionSource"
DocsisTlvs["64"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["64"]["subTlvs"]["02"]["datatype"] = "ip_ip6"
DocsisTlvs["64"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["64"]["subTlvs"]["03"] = {}
DocsisTlvs["64"]["subTlvs"]["03"]["description"] = "CMTSStaticMulticastSessionCMIM"
DocsisTlvs["64"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["64"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["64"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["64"]["subTlvs"]["107"] = {}
DocsisTlvs["64"]["subTlvs"]["107"]["description"] = "Technicolor thing"
DocsisTlvs["64"]["subTlvs"]["107"]["datatype"] = "unknown"
DocsisTlvs["64"]["subTlvs"]["107"]["subTlvs"] = {}
DocsisTlvs["64"]["subTlvs"]["107"]['hex'] = "6b"

DocsisTlvs["65"] = {}
DocsisTlvs["65"]["description"] = "L2VPNMACAgingEncoding"
DocsisTlvs["65"]["hex"] = "41"
DocsisTlvs["65"]["datatype"] = "aggregate"
DocsisTlvs["65"]["subTlvs"] = {}

DocsisTlvs["65"]["subTlvs"]["01"] = {}
DocsisTlvs["65"]["subTlvs"]["01"]["description"] = "L2VPNMACAgingMode"
DocsisTlvs["65"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["65"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["65"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["65"]["subTlvs"]["116"] = {}
DocsisTlvs["65"]["subTlvs"]["116"]["description"] = "unknown"
DocsisTlvs["65"]["subTlvs"]["116"]["hex"] = "74"
DocsisTlvs["65"]["subTlvs"]["116"]["datatype"] = "unknown"
DocsisTlvs["65"]["subTlvs"]["116"]["subTlvs"] = {}

DocsisTlvs["66"] = {}
DocsisTlvs["66"]["description"] = "ManagementEventControl"
DocsisTlvs["66"]["hex"] = "42"
DocsisTlvs["66"]["datatype"] = "uint"
DocsisTlvs["66"]["subTlvs"] = {}

DocsisTlvs["67"] = {}
DocsisTlvs["67"]["description"] = "SubscriberManagementCPEIPv6Table"
DocsisTlvs["67"]["hex"] = "43"
DocsisTlvs["67"]["datatype"] = "(encode_ip6_list)"
DocsisTlvs["67"]["subTlvs"] = {}

DocsisTlvs["68"] = {}
DocsisTlvs["68"]["description"] = "DefaultUpstreamTargetBuffer"
DocsisTlvs["68"]["hex"] = "44"
DocsisTlvs["68"]["datatype"] = "ushort"
DocsisTlvs["68"]["subTlvs"] = {}

DocsisTlvs["69"] = {}
DocsisTlvs["69"]["description"] = "MACAddressLearningControlEncoding"
DocsisTlvs["69"]["hex"] = "45"
DocsisTlvs["69"]["datatype"] = "aggregate"
DocsisTlvs["69"]["subTlvs"] = {}

DocsisTlvs["69"]["subTlvs"]["01"] = {}
DocsisTlvs["69"]["subTlvs"]["01"]["description"] = "MACAddressLearningControl"
DocsisTlvs["69"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["69"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["69"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["69"]["subTlvs"]["02"] = {}
DocsisTlvs["69"]["subTlvs"]["02"]["description"] = "MACAddressLearningHoldoffTimer"
DocsisTlvs["69"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["69"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["69"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["69"]["subTlvs"]["101"] = {}
DocsisTlvs["69"]["subTlvs"]["101"]["description"] = "Technicolor thing"
DocsisTlvs["69"]["subTlvs"]["101"]["hex"] = "65"
DocsisTlvs["69"]["subTlvs"]["101"]["datatype"] = "unknown"
DocsisTlvs["69"]["subTlvs"]["101"]["subTlvs"] = {}

DocsisTlvs["70"] = {}
DocsisTlvs["70"]["description"] = "UpstreamAggregateServiceFlow"
DocsisTlvs["70"]["hex"] = "46"
DocsisTlvs["70"]["datatype"] = "aggregate"
DocsisTlvs["70"]["subTlvs"] = {}

DocsisTlvs["70"]["subTlvs"]["01"] = {}
DocsisTlvs["70"]["subTlvs"]["01"]["description"] = "UpstreamServiceFlowReference"
DocsisTlvs["70"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["70"]["subTlvs"]["01"]["datatype"] = "ushort"
DocsisTlvs["70"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["70"]["subTlvs"]["36"] = {}
DocsisTlvs["70"]["subTlvs"]["36"]["description"] = "UpstreamAggregateServiceFlowReference"
DocsisTlvs["70"]["subTlvs"]["36"]["hex"] = "24"
DocsisTlvs["70"]["subTlvs"]["36"]["datatype"] = "aggregate"
DocsisTlvs["70"]["subTlvs"]["36"]["subTlvs"] = {}

DocsisTlvs["70"]["subTlvs"]["37"] = {}
DocsisTlvs["70"]["subTlvs"]["37"]["description"] = "UpstreamMESPReference"
DocsisTlvs["70"]["subTlvs"]["37"]["hex"] = "25"
DocsisTlvs["70"]["subTlvs"]["37"]["datatype"] = "ushort"
DocsisTlvs["70"]["subTlvs"]["37"]["subTlvs"] = {}

DocsisTlvs["71"] = {}
DocsisTlvs["71"]["description"] = "DownstreamAggregateServiceFlow"
DocsisTlvs["71"]["hex"] = "47"
DocsisTlvs["71"]["datatype"] = "aggregate"
DocsisTlvs["71"]["subTlvs"] = {}

DocsisTlvs["71"]["subTlvs"]["01"] = {}
DocsisTlvs["71"]["subTlvs"]["01"]["description"] = "DownstreamServiceFlowReference"
DocsisTlvs["71"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["71"]["subTlvs"]["01"]["datatype"] = "ushort"
DocsisTlvs["71"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["71"]["subTlvs"]["36"] = {}
DocsisTlvs["71"]["subTlvs"]["36"]["description"] = "DownstreamAggregateServiceFlowReference"
DocsisTlvs["71"]["subTlvs"]["36"]["hex"] = "24"
DocsisTlvs["71"]["subTlvs"]["36"]["datatype"] = "aggregate"
DocsisTlvs["71"]["subTlvs"]["36"]["subTlvs"] = {}

DocsisTlvs["71"]["subTlvs"]["37"] = {}
DocsisTlvs["71"]["subTlvs"]["37"]["description"] = "DownstreamMESPReference"
DocsisTlvs["71"]["subTlvs"]["37"]["hex"] = "25"
DocsisTlvs["71"]["subTlvs"]["37"]["datatype"] = "ushort"
DocsisTlvs["71"]["subTlvs"]["37"]["subTlvs"] = {}

DocsisTlvs["72"] = {}
DocsisTlvs["72"]["description"] = "MetroEthernetServiceProfile"
DocsisTlvs["72"]["hex"] = "48"
DocsisTlvs["72"]["datatype"] = "aggregate"
DocsisTlvs["72"]["subTlvs"] = {}

DocsisTlvs["72"]["subTlvs"]["01"] = {}
DocsisTlvs["72"]["subTlvs"]["01"]["description"] = "MESPReference"
DocsisTlvs["72"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["72"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["72"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["72"]["subTlvs"]["02"] = {}
DocsisTlvs["72"]["subTlvs"]["02"]["description"] = "MESPBandwidthProfile"
DocsisTlvs["72"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["72"]["subTlvs"]["02"]["datatype"] = "aggregate"
DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["01"] = {}
DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["01"]["description"] = "CIR"
DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["01"]["datatype"] = "uint"
DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["02"] = {}
DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["02"]["description"] = "CBR"
DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["02"]["datatype"] = "uint"
DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["03"] = {}
DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["03"]["description"] = "EIR"
DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["03"]["datatype"] = "uint"
DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["04"] = {}
DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["04"]["description"] = "EBS"
DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["04"]["datatype"] = "uint"
DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["05"] = {}
DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["05"]["description"] = "CouplingFlag"
DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["05"]["datatype"] = "uchar"
DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["06"] = {}
DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["06"]["description"] = "ColorMode"
DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["06"]["datatype"] = "aggregate"
DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["01"] = {}
DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["01"]["description"] = "ColorIdentificationField"
DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["02"] = {}
DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["02"]["description"] = "ColorIdentificationFieldValue"
DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["07"] = {}
DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["07"]["description"] = "ColorMarking"
DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["07"]["datatype"] = "aggregate"
DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["07"]["subTlvs"]["01"] = {}
DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["07"]["subTlvs"]["01"]["description"] = "ColorMarkingField"
DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["07"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["07"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["07"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["07"]["subTlvs"]["02"] = {}
DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["07"]["subTlvs"]["02"]["description"] = "ColorMarkingFieldValue"
DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["07"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["07"]["subTlvs"]["02"]["datatype"] = "hexstr"
DocsisTlvs["72"]["subTlvs"]["02"]["subTlvs"]["07"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["72"]["subTlvs"]["03"] = {}
DocsisTlvs["72"]["subTlvs"]["03"]["description"] = "MESPName"
DocsisTlvs["72"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["72"]["subTlvs"]["03"]["datatype"] = "strzero"
DocsisTlvs["72"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["73"] = {}
DocsisTlvs["73"]["description"] = "NetworkTimingProfile"
DocsisTlvs["73"]["hex"] = "49"
DocsisTlvs["73"]["datatype"] = "aggregate"
DocsisTlvs["73"]["subTlvs"] = {}

DocsisTlvs["73"]["subTlvs"]["01"] = {}
DocsisTlvs["73"]["subTlvs"]["01"]["description"] = "NetworkTimingProfileReference"
DocsisTlvs["73"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["73"]["subTlvs"]["01"]["datatype"] = "ushort"
DocsisTlvs["73"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["73"]["subTlvs"]["02"] = {}
DocsisTlvs["73"]["subTlvs"]["02"]["description"] = "NetworkTimingProfileName"
DocsisTlvs["73"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["73"]["subTlvs"]["02"]["datatype"] = "strzero"
DocsisTlvs["73"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["74"] = {}
DocsisTlvs["74"]["description"] = "EnergyManagementParameter"
DocsisTlvs["74"]["hex"] = "4a"
DocsisTlvs["74"]["datatype"] = "aggregate"
DocsisTlvs["74"]["subTlvs"] = {}

DocsisTlvs["74"]["subTlvs"]["01"] = {}
DocsisTlvs["74"]["subTlvs"]["01"]["description"] = "EnergyManagementFeatureControl"
DocsisTlvs["74"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["74"]["subTlvs"]["01"]["datatype"] = "uint"
DocsisTlvs["74"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["74"]["subTlvs"]["02"] = {}
DocsisTlvs["74"]["subTlvs"]["02"]["description"] = "EnergyManagement1x1Mode"
DocsisTlvs["74"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["74"]["subTlvs"]["02"]["datatype"] = "aggregate"
DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["01"] = {}
DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["01"]["description"] = "DownstreamActivityDetectionParameters"
DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["01"]["datatype"] = "aggregate"
DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"]["01"] = {}
DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"]["01"]["description"] = "DownstreamEntryBitrateThreshold"
DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"]["01"]["datatype"] = "uint"
DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"]["02"] = {}
DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"]["02"]["description"] = "DownstreamEntryTimeThreshold"
DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"]["02"]["datatype"] = "ushort"
DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"]["03"] = {}
DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"]["03"]["description"] = "DownstreamExitBitrateThreshold"
DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"]["03"]["datatype"] = "uint"
DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"]["04"] = {}
DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"]["04"]["description"] = "DownstreamExitTimeThreshold"
DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"]["04"]["datatype"] = "ushort"
DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["02"] = {}
DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["02"]["description"] = "UpstreamActivityDetectionParameters"
DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["02"]["datatype"] = "aggregate"
DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"]["01"] = {}
DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"]["01"]["description"] = "UpstreamEntryBitrateThreshold"
DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"]["01"]["datatype"] = "uint"
DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"]["02"] = {}
DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"]["02"]["description"] = "UpstreamEntryTimeThreshold"
DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"]["02"]["datatype"] = "ushort"
DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"]["03"] = {}
DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"]["03"]["description"] = "UpstreamExitBitrateThreshold"
DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"]["03"]["datatype"] = "uint"
DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"]["04"] = {}
DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"]["04"]["description"] = "UpstreamExitTimeThreshold"
DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"]["04"]["datatype"] = "ushort"
DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["03"] = {}
DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["03"]["description"] = "EnergyManagementCyclePeriod"
DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["03"]["datatype"] = "ushort"
DocsisTlvs["74"]["subTlvs"]["02"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["75"] = {}
DocsisTlvs["75"]["description"] = "EnergyManagement1x1ModeIndicator"
DocsisTlvs["75"]["hex"] = "4b"
DocsisTlvs["75"]["datatype"] = "uchar"
DocsisTlvs["75"]["subTlvs"] = {}

DocsisTlvs["76"] = {}
DocsisTlvs["76"]["description"] = "CMUpstreamAQMDisable"
DocsisTlvs["76"]["hex"] = "4c"
DocsisTlvs["76"]["datatype"] = "uchar"
DocsisTlvs["76"]["subTlvs"] = {}

DocsisTlvs["77"] = {}
DocsisTlvs["77"]["description"] = "unknown"
DocsisTlvs["77"]["hex"] = "4d"
DocsisTlvs["77"]["datatype"] = "unknown"
DocsisTlvs["77"]["subTlvs"] = {}

DocsisTlvs["79"] = {}
DocsisTlvs["79"]["description"] = "UNIControlEncodings"
DocsisTlvs["79"]["hex"] = "4f"
DocsisTlvs["79"]["datatype"] = "aggregate"
DocsisTlvs["79"]["subTlvs"] = {}

DocsisTlvs["79"]["subTlvs"]["01"] = {}
DocsisTlvs["79"]["subTlvs"]["01"]["description"] = "ContextCMIM"
DocsisTlvs["79"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["79"]["subTlvs"]["01"]["datatype"] = "hexstr"
DocsisTlvs["79"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["79"]["subTlvs"]["02"] = {}
DocsisTlvs["79"]["subTlvs"]["02"]["description"] = "UNIAdminStatus"
DocsisTlvs["79"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["79"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["79"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["79"]["subTlvs"]["03"] = {}
DocsisTlvs["79"]["subTlvs"]["03"]["description"] = "UNIAutoNegotiationStatus"
DocsisTlvs["79"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["79"]["subTlvs"]["03"]["datatype"] = "uchar"
DocsisTlvs["79"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["79"]["subTlvs"]["04"] = {}
DocsisTlvs["79"]["subTlvs"]["04"]["description"] = "UNIOperatingSpeed"
DocsisTlvs["79"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["79"]["subTlvs"]["04"]["datatype"] = "uchar"
DocsisTlvs["79"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["79"]["subTlvs"]["05"] = {}
DocsisTlvs["79"]["subTlvs"]["05"]["description"] = "UNIDuplex"
DocsisTlvs["79"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["79"]["subTlvs"]["05"]["datatype"] = "uchar"
DocsisTlvs["79"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["79"]["subTlvs"]["06"] = {}
DocsisTlvs["79"]["subTlvs"]["06"]["description"] = "EEEStatus"
DocsisTlvs["79"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["79"]["subTlvs"]["06"]["datatype"] = "uchar"
DocsisTlvs["79"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["79"]["subTlvs"]["07"] = {}
DocsisTlvs["79"]["subTlvs"]["07"]["description"] = "MaximumFrameSize"
DocsisTlvs["79"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["79"]["subTlvs"]["07"]["datatype"] = "ushort"
DocsisTlvs["79"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["79"]["subTlvs"]["08"] = {}
DocsisTlvs["79"]["subTlvs"]["08"]["description"] = "PowerOverEthernetStatus"
DocsisTlvs["79"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["79"]["subTlvs"]["08"]["datatype"] = "uchar"
DocsisTlvs["79"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["79"]["subTlvs"]["09"] = {}
DocsisTlvs["79"]["subTlvs"]["09"]["description"] = "MediaType"
DocsisTlvs["79"]["subTlvs"]["09"]["hex"] = "09"
DocsisTlvs["79"]["subTlvs"]["09"]["datatype"] = "uchar"
DocsisTlvs["79"]["subTlvs"]["09"]["subTlvs"] = {}

DocsisTlvs["79"]["subTlvs"]["106"] = {}
DocsisTlvs["79"]["subTlvs"]["106"]["description"] = "unknown"
DocsisTlvs["79"]["subTlvs"]["106"]["hex"] = "6a"
DocsisTlvs["79"]["subTlvs"]["106"]["datatype"] = "unknown"
DocsisTlvs["79"]["subTlvs"]["106"]["subTlvs"] = {}



DocsisTlvs["81"] = {}
DocsisTlvs["81"]["description"] = "ManufacturerCVCChain"
DocsisTlvs["81"]["hex"] = "51"
DocsisTlvs["81"]["datatype"] = "hexstr"
DocsisTlvs["81"]["subTlvs"] = {}

DocsisTlvs["82"] = {}
DocsisTlvs["82"]["description"] = "CoSignerCVCChain"
DocsisTlvs["82"]["hex"] = "52"
DocsisTlvs["82"]["datatype"] = "hexstr"
DocsisTlvs["82"]["subTlvs"] = {}

DocsisTlvs["83"] = {}
DocsisTlvs["83"]["description"] = "unknown"
DocsisTlvs["83"]["hex"] = "53"
DocsisTlvs["83"]["datatype"] = "unknown"
DocsisTlvs["83"]["subTlvs"] = {}

DocsisTlvs["84"] = {}
DocsisTlvs["84"]["description"] = "DiplexerBandEdge"
DocsisTlvs["84"]["hex"] = "54"
DocsisTlvs["84"]["datatype"] = "aggregate"
DocsisTlvs["84"]["subTlvs"] = {}

DocsisTlvs["84"]["subTlvs"]["01"] = {}
DocsisTlvs["84"]["subTlvs"]["01"]["description"] = "DiplexerUpstreamUpperBandEdge"
DocsisTlvs["84"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["84"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["84"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["84"]["subTlvs"]["02"] = {}
DocsisTlvs["84"]["subTlvs"]["02"]["description"] = "DiplexerDownstreamLowerBandEdge"
DocsisTlvs["84"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["84"]["subTlvs"]["02"]["datatype"] = "uchar"
DocsisTlvs["84"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["84"]["subTlvs"]["03"] = {}
DocsisTlvs["84"]["subTlvs"]["03"]["description"] = "DiplexerDownstreamUpperBandEdge"
DocsisTlvs["84"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["84"]["subTlvs"]["03"]["datatype"] = "uchar"
DocsisTlvs["84"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["93"] = {}
DocsisTlvs["93"]["description"] = "Upstream Enhanced HQoS ASF"
DocsisTlvs["93"]["hex"] = "5d"
DocsisTlvs["93"]["datatype"] = "unknown"
DocsisTlvs["93"]["subTlvs"] = {}

DocsisTlvs["97"] = {}
DocsisTlvs["97"]["description"] = "unknown"
DocsisTlvs["97"]["hex"] = "61"
DocsisTlvs["97"]["datatype"] = "unknown"
DocsisTlvs["97"]["subTlvs"] = {}

DocsisTlvs["98"] = {}
DocsisTlvs["98"]["description"] = "unknown"
DocsisTlvs["98"]["hex"] = "62"
DocsisTlvs["98"]["datatype"] = "unknown"
DocsisTlvs["98"]["subTlvs"] = {}

DocsisTlvs["99"] = {}
DocsisTlvs["99"]["description"] = "unknown"
DocsisTlvs["99"]["hex"] = "63"
DocsisTlvs["99"]["datatype"] = "unknown"
DocsisTlvs["99"]["subTlvs"] = {}

DocsisTlvs["100"] = {}
DocsisTlvs["100"]["description"] = "unknown Technicolor crap"
DocsisTlvs["100"]["hex"] = "64"
DocsisTlvs["100"]["datatype"] = "unknown"
DocsisTlvs["100"]["subTlvs"] = {}

DocsisTlvs["101"] = {}
DocsisTlvs["101"]["description"] = "unknown Technicolor crap"
DocsisTlvs["101"]["hex"] = "65"
DocsisTlvs["101"]["datatype"] = "unknown"
DocsisTlvs["101"]["subTlvs"] = {}

DocsisTlvs["102"] = {}
DocsisTlvs["102"]["description"] = "unknown Technicolor crap"
DocsisTlvs["102"]["hex"] = "66"
DocsisTlvs["102"]["datatype"] = "unknown"
DocsisTlvs["102"]["subTlvs"] = {}



DocsisTlvs["103"] = {}
DocsisTlvs["103"]["description"] = "unknown Technicolor crap"
DocsisTlvs["103"]["hex"] = "67"
DocsisTlvs["103"]["datatype"] = "unknown"
DocsisTlvs["103"]["subTlvs"] = {}

DocsisTlvs["105"] = {}
DocsisTlvs["105"]["description"] = "unknown"
DocsisTlvs["105"]["hex"] = "69"
DocsisTlvs["105"]["datatype"] = "unknown"
DocsisTlvs["105"]["subTlvs"] = {}

DocsisTlvs["106"] = {}
DocsisTlvs["106"]["description"] = "unknown"
DocsisTlvs["106"]["hex"] = "6a"
DocsisTlvs["106"]["datatype"] = "unknown"
DocsisTlvs["106"]["subTlvs"] = {}

DocsisTlvs["108"] = {}
DocsisTlvs["108"]["description"] = "unknown"
DocsisTlvs["108"]["hex"] = "6c"
DocsisTlvs["108"]["datatype"] = "unknown"
DocsisTlvs["108"]["subTlvs"] = {}


DocsisTlvs["110"] = {}
DocsisTlvs["110"]["description"] = "unknown"
DocsisTlvs["110"]["hex"] = "6e"
DocsisTlvs["110"]["datatype"] = "unknown"
DocsisTlvs["110"]["subTlvs"] = {}

DocsisTlvs["111"] = {}
DocsisTlvs["111"]["description"] = "unknown"
DocsisTlvs["111"]["hex"] = "6f"
DocsisTlvs["111"]["datatype"] = "unknown"
DocsisTlvs["111"]["subTlvs"] = {}

DocsisTlvs["112"] = {}
DocsisTlvs["112"]["description"] = "unknown Technicolor crap"
DocsisTlvs["112"]["hex"] = "70"
DocsisTlvs["112"]["datatype"] = "unknown"
DocsisTlvs["112"]["subTlvs"] = {}

DocsisTlvs["114"] = {}
DocsisTlvs["114"]["description"] = "unknown Technicolor crap"
DocsisTlvs["114"]["hex"] = "72"
DocsisTlvs["114"]["datatype"] = "unknown"
DocsisTlvs["114"]["subTlvs"] = {}

DocsisTlvs["115"] = {}
DocsisTlvs["115"]["description"] = "unknown Technicolor crap"
DocsisTlvs["115"]["hex"] = "73"
DocsisTlvs["115"]["datatype"] = "unknown"
DocsisTlvs["115"]["subTlvs"] = {}

DocsisTlvs["116"] = {}
DocsisTlvs["116"]["description"] = "unknown Technicolor crap"
DocsisTlvs["116"]["hex"] = "74"
DocsisTlvs["116"]["datatype"] = "unknown"
DocsisTlvs["116"]["subTlvs"] = {}

DocsisTlvs["117"] = {}
DocsisTlvs["117"]["description"] = "unknown Technicolor crap"
DocsisTlvs["117"]["hex"] = "75"
DocsisTlvs["117"]["datatype"] = "unknown"
DocsisTlvs["117"]["subTlvs"] = {}

DocsisTlvs["118"] = {}
DocsisTlvs["118"]["description"] = "unknown Technicolor crap"
DocsisTlvs["118"]["hex"] = "76"
DocsisTlvs["118"]["datatype"] = "unknown"
DocsisTlvs["118"]["subTlvs"] = {}

DocsisTlvs["119"] = {}
DocsisTlvs["119"]["description"] = "unknown Technicolor crap"
DocsisTlvs["119"]["hex"] = "77"
DocsisTlvs["119"]["datatype"] = "unknown"
DocsisTlvs["119"]["subTlvs"] = {}

DocsisTlvs["161"] = {}
DocsisTlvs["161"]["description"] = "unknown"
DocsisTlvs["161"]["hex"] = "A1"
DocsisTlvs["161"]["datatype"] = "unknown"
DocsisTlvs["161"]["subTlvs"] = {}

DocsisTlvs["202"] = {}
DocsisTlvs["202"]["description"] = "eRouter"
DocsisTlvs["202"]["hex"] = "ca"
DocsisTlvs["202"]["datatype"] = "aggregate"
DocsisTlvs["202"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["01"] = {}
DocsisTlvs["202"]["subTlvs"]["01"]["description"] = "InitializationMode"
DocsisTlvs["202"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["202"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["202"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["02"] = {}
DocsisTlvs["202"]["subTlvs"]["02"]["description"] = "TR69ManagementServer"
DocsisTlvs["202"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["202"]["subTlvs"]["02"]["datatype"] = "aggregate"
DocsisTlvs["202"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["02"]["subTlvs"]["01"] = {}
DocsisTlvs["202"]["subTlvs"]["02"]["subTlvs"]["01"]["description"] = "EnableCWMP"
DocsisTlvs["202"]["subTlvs"]["02"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["202"]["subTlvs"]["02"]["subTlvs"]["01"]["datatype"] = "uchar"
DocsisTlvs["202"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["02"]["subTlvs"]["02"] = {}
DocsisTlvs["202"]["subTlvs"]["02"]["subTlvs"]["02"]["description"] = "URL"
DocsisTlvs["202"]["subTlvs"]["02"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["202"]["subTlvs"]["02"]["subTlvs"]["02"]["datatype"] = "string"
DocsisTlvs["202"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["02"]["subTlvs"]["03"] = {}
DocsisTlvs["202"]["subTlvs"]["02"]["subTlvs"]["03"]["description"] = "Username"
DocsisTlvs["202"]["subTlvs"]["02"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["202"]["subTlvs"]["02"]["subTlvs"]["03"]["datatype"] = "string"
DocsisTlvs["202"]["subTlvs"]["02"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["02"]["subTlvs"]["04"] = {}
DocsisTlvs["202"]["subTlvs"]["02"]["subTlvs"]["04"]["description"] = "Password"
DocsisTlvs["202"]["subTlvs"]["02"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["202"]["subTlvs"]["02"]["subTlvs"]["04"]["datatype"] = "string"
DocsisTlvs["202"]["subTlvs"]["02"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["02"]["subTlvs"]["05"] = {}
DocsisTlvs["202"]["subTlvs"]["02"]["subTlvs"]["05"]["description"] = "ConnectionRequestUsername"
DocsisTlvs["202"]["subTlvs"]["02"]["subTlvs"]["05"]["hex"] = "05"
DocsisTlvs["202"]["subTlvs"]["02"]["subTlvs"]["05"]["datatype"] = "string"
DocsisTlvs["202"]["subTlvs"]["02"]["subTlvs"]["05"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["02"]["subTlvs"]["06"] = {}
DocsisTlvs["202"]["subTlvs"]["02"]["subTlvs"]["06"]["description"] = "ConnectionRequestPassword"
DocsisTlvs["202"]["subTlvs"]["02"]["subTlvs"]["06"]["hex"] = "06"
DocsisTlvs["202"]["subTlvs"]["02"]["subTlvs"]["06"]["datatype"] = "string"
DocsisTlvs["202"]["subTlvs"]["02"]["subTlvs"]["06"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["02"]["subTlvs"]["07"] = {}
DocsisTlvs["202"]["subTlvs"]["02"]["subTlvs"]["07"]["description"] = "ACSOverride"
DocsisTlvs["202"]["subTlvs"]["02"]["subTlvs"]["07"]["hex"] = "07"
DocsisTlvs["202"]["subTlvs"]["02"]["subTlvs"]["07"]["datatype"] = "uchar"
DocsisTlvs["202"]["subTlvs"]["02"]["subTlvs"]["07"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["03"] = {}
DocsisTlvs["202"]["subTlvs"]["03"]["description"] = "InitializationModeOverride"
DocsisTlvs["202"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["202"]["subTlvs"]["03"]["datatype"] = "uchar"
DocsisTlvs["202"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["10"] = {}
DocsisTlvs["202"]["subTlvs"]["10"]["description"] = "RATransmissionInterval"
DocsisTlvs["202"]["subTlvs"]["10"]["hex"] = "0a"
DocsisTlvs["202"]["subTlvs"]["10"]["datatype"] = "ushort"
DocsisTlvs["202"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["11"] = {}
DocsisTlvs["202"]["subTlvs"]["11"]["description"] = "SnmpMibObject"
DocsisTlvs["202"]["subTlvs"]["11"]["hex"] = "0b"
DocsisTlvs["202"]["subTlvs"]["11"]["datatype"] = "snmp_object"
DocsisTlvs["202"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["42"] = {}
DocsisTlvs["202"]["subTlvs"]["42"]["description"] = "TopologyModeEncoding"
DocsisTlvs["202"]["subTlvs"]["42"]["hex"] = "2a"
DocsisTlvs["202"]["subTlvs"]["42"]["datatype"] = "uchar"
DocsisTlvs["202"]["subTlvs"]["42"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["43"] = {}
DocsisTlvs["202"]["subTlvs"]["43"]["description"] = "VendorSpecific"
DocsisTlvs["202"]["subTlvs"]["43"]["hex"] = "2b"
DocsisTlvs["202"]["subTlvs"]["43"]["datatype"] = "aggregate"
DocsisTlvs["202"]["subTlvs"]["43"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["43"]["subTlvs"]["08"] = {}
DocsisTlvs["202"]["subTlvs"]["43"]["subTlvs"]["08"]["description"] = "VendorIdentifier"
DocsisTlvs["202"]["subTlvs"]["43"]["subTlvs"]["08"]["hex"] = "08"
DocsisTlvs["202"]["subTlvs"]["43"]["subTlvs"]["08"]["datatype"] = "hexstr"
DocsisTlvs["202"]["subTlvs"]["43"]["subTlvs"]["08"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["53"] = {}
DocsisTlvs["202"]["subTlvs"]["53"]["description"] = "SNMPv1v2cCoexistenceConfig"
DocsisTlvs["202"]["subTlvs"]["53"]["hex"] = "35"
DocsisTlvs["202"]["subTlvs"]["53"]["datatype"] = "aggregate"
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["01"] = {}
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["01"]["description"] = "SNMPv1v2cCommunityName"
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["01"]["datatype"] = "string"
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["02"] = {}
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["02"]["description"] = "SNMPv1v2cTransportAddressAccess"
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["02"]["datatype"] = "aggregate"
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["02"]["subTlvs"]["01"] = {}
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["02"]["subTlvs"]["01"]["description"] = "SNMPv1v2cTransportAddress"
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["02"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["02"]["subTlvs"]["01"]["datatype"] = "(encode_ip_ip6_port)"
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["02"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["02"]["subTlvs"]["02"] = {}
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["02"]["subTlvs"]["02"]["description"] = "SNMPv1v2cTransportAddressMask"
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["02"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["02"]["subTlvs"]["02"]["datatype"] = "(encode_ip_ip6_port)"
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["02"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["03"] = {}
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["03"]["description"] = "SNMPv1v2cAccessViewType"
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["03"]["datatype"] = "uchar"
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["04"] = {}
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["04"]["description"] = "SNMPv1v2cAccessViewName"
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["04"]["datatype"] = "string"
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["54"] = {}
DocsisTlvs["202"]["subTlvs"]["54"]["description"] = "SNMPv3AccessViewConfiguration"
DocsisTlvs["202"]["subTlvs"]["54"]["hex"] = "36"
DocsisTlvs["202"]["subTlvs"]["54"]["datatype"] = "aggregate"
DocsisTlvs["202"]["subTlvs"]["54"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["54"]["subTlvs"]["01"] = {}
DocsisTlvs["202"]["subTlvs"]["54"]["subTlvs"]["01"]["description"] = "SNMPv3AccessViewName"
DocsisTlvs["202"]["subTlvs"]["54"]["subTlvs"]["01"]["hex"] = "01"
DocsisTlvs["202"]["subTlvs"]["54"]["subTlvs"]["01"]["datatype"] = "string"
DocsisTlvs["202"]["subTlvs"]["54"]["subTlvs"]["01"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["54"]["subTlvs"]["02"] = {}
DocsisTlvs["202"]["subTlvs"]["54"]["subTlvs"]["02"]["description"] = "SNMPv3AccessViewSubtree"
DocsisTlvs["202"]["subTlvs"]["54"]["subTlvs"]["02"]["hex"] = "02"
DocsisTlvs["202"]["subTlvs"]["54"]["subTlvs"]["02"]["datatype"] = "(encode_oid)"
DocsisTlvs["202"]["subTlvs"]["54"]["subTlvs"]["02"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["54"]["subTlvs"]["03"] = {}
DocsisTlvs["202"]["subTlvs"]["54"]["subTlvs"]["03"]["description"] = "SNMPv3AccessViewMask"
DocsisTlvs["202"]["subTlvs"]["54"]["subTlvs"]["03"]["hex"] = "03"
DocsisTlvs["202"]["subTlvs"]["54"]["subTlvs"]["03"]["datatype"] = "hexstr"
DocsisTlvs["202"]["subTlvs"]["54"]["subTlvs"]["03"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["54"]["subTlvs"]["04"] = {}
DocsisTlvs["202"]["subTlvs"]["54"]["subTlvs"]["04"]["description"] = "SNMPv3AccessViewType"
DocsisTlvs["202"]["subTlvs"]["54"]["subTlvs"]["04"]["hex"] = "04"
DocsisTlvs["202"]["subTlvs"]["54"]["subTlvs"]["04"]["datatype"] = "uchar"
DocsisTlvs["202"]["subTlvs"]["54"]["subTlvs"]["04"]["subTlvs"] = {}

DocsisTlvs["217"] = {}
DocsisTlvs["217"]["description"] = "unknown"
DocsisTlvs["217"]["hex"] = "d9"
DocsisTlvs["217"]["datatype"] = "unknown"
DocsisTlvs["217"]["subTlvs"] = {}

DocsisTlvs["998"] = {}
DocsisTlvs["998"]["description"] = "GenericTLV"
DocsisTlvs["998"]["hex"] = "3e6"
DocsisTlvs["998"]["datatype"] = "special"
DocsisTlvs["998"]["subTlvs"] = {}

DocsisTlvs["254"] = {}
DocsisTlvs["254"]["description"] = "MtaConfigDelimiter"
DocsisTlvs["254"]["hex"] = "fe"
DocsisTlvs["254"]["datatype"] = "uchar"
DocsisTlvs["254"]["subTlvs"] = {}

DocsisTlvs["255"] = {}
DocsisTlvs["255"]["description"] = "/*EndOfDataMkr*/"
DocsisTlvs["255"]["datatype"] = "special"
DocsisTlvs["255"]["subTlvs"] = {}
DocsisTlvs["255"]['hex'] = "ff"




if __name__ == '__main__':
	def print_sub_tlvs(tlv, parent):
		for key in tlv:
			if tlv[key]["datatype"] == "aggregate":
				print("var tlv" + parent + key + " = TLVDefinitions(tag: " + key + ", dataType: ." + tlv[key]["datatype"] + ", description: \"" + tlv[key]["description"] + "\")")
			else:
				print("let tlv" + parent + key + " = TLVDefinitions(tag: " + key + ", dataType: ." + tlv[key]["datatype"] + ", description: \"" + tlv[key]["description"] + "\")")
			print_sub_tlvs(tlv[key]["subTlvs"], parent + key)
			print("tlv" + parent + ".subTLVs.append(tlv" + parent + key  + ")")

	endbits = "let DOCSIS :[TLVDefinitions] = [\n"
	#fp = open("outs.json", 'w')
	#json.dump(DocsisTlvs, fp)
	for key in DocsisTlvs.keys():
		endbits += "tlv" + key + ",\n"
		if DocsisTlvs[key]["datatype"] == "aggregate":
			print("var tlv" + key + " = TLVDefinitions(tag: " + key + ", dataType: ." + DocsisTlvs[key]["datatype"] + ", description: \"" + DocsisTlvs[key]["description"] + "\")")
		else:
			print("let tlv"  + key + " = TLVDefinitions(tag: " + key + ", dataType: ." + DocsisTlvs[key]["datatype"] + ", description: \"" + DocsisTlvs[key]["description"] + "\")")
		print_sub_tlvs(DocsisTlvs[key]["subTlvs"], key)
	endbits += "]"
	print(endbits)