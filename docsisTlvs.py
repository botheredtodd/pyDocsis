# For aesthetic reasons, the user is encouraged to put this in a database or something

DocsisTlvs = {}

DocsisTlvs["00"] = {}
DocsisTlvs["00"]["description"] = "/* Pad */"
DocsisTlvs["00"]["hex"] = "0"
DocsisTlvs["00"]["datatype"] = "(decode_special)"
DocsisTlvs["00"]["subTlvs"] = {}

DocsisTlvs["01"] = {}
DocsisTlvs["01"]["description"] = "DownstreamFrequency"
DocsisTlvs["01"]["hex"] = "1"
DocsisTlvs["01"]["datatype"] = "(encode_uint)"
DocsisTlvs["01"]["subTlvs"] = {}

DocsisTlvs["02"] = {}
DocsisTlvs["02"]["description"] = "UpstreamChannelId"
DocsisTlvs["02"]["hex"] = "2"
DocsisTlvs["02"]["datatype"] = "(encode_uchar)"
DocsisTlvs["02"]["subTlvs"] = {}

DocsisTlvs["03"] = {}
DocsisTlvs["03"]["description"] = "NetworkAccess"
DocsisTlvs["03"]["hex"] = "3"
DocsisTlvs["03"]["datatype"] = "(encode_uchar)"
DocsisTlvs["03"]["subTlvs"] = {}

DocsisTlvs["04"] = {}
DocsisTlvs["04"]["description"] = "ClassOfService"
DocsisTlvs["04"]["hex"] = "4"
DocsisTlvs["04"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["04"]["subTlvs"] = {}

DocsisTlvs["04"]["subTlvs"]["1"] = {}
DocsisTlvs["04"]["subTlvs"]["1"]["description"] = "ClassID"
DocsisTlvs["04"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["04"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["04"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["04"]["subTlvs"]["2"] = {}
DocsisTlvs["04"]["subTlvs"]["2"]["description"] = "MaxRateDown"
DocsisTlvs["04"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["04"]["subTlvs"]["2"]["datatype"] = "(encode_uint)"
DocsisTlvs["04"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["04"]["subTlvs"]["3"] = {}
DocsisTlvs["04"]["subTlvs"]["3"]["description"] = "MaxRateUp"
DocsisTlvs["04"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["04"]["subTlvs"]["3"]["datatype"] = "(encode_uint)"
DocsisTlvs["04"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["04"]["subTlvs"]["4"] = {}
DocsisTlvs["04"]["subTlvs"]["4"]["description"] = "PriorityUp"
DocsisTlvs["04"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["04"]["subTlvs"]["4"]["datatype"] = "(encode_uchar)"
DocsisTlvs["04"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["04"]["subTlvs"]["5"] = {}
DocsisTlvs["04"]["subTlvs"]["5"]["description"] = "GuaranteedUp"
DocsisTlvs["04"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["04"]["subTlvs"]["5"]["datatype"] = "(encode_uint)"
DocsisTlvs["04"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["04"]["subTlvs"]["6"] = {}
DocsisTlvs["04"]["subTlvs"]["6"]["description"] = "MaxBurstUp"
DocsisTlvs["04"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["04"]["subTlvs"]["6"]["datatype"] = "(encode_ushort)"
DocsisTlvs["04"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["04"]["subTlvs"]["7"] = {}
DocsisTlvs["04"]["subTlvs"]["7"]["description"] = "PrivacyEnable"
DocsisTlvs["04"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["04"]["subTlvs"]["7"]["datatype"] = "(encode_uchar)"
DocsisTlvs["04"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["05"] = {}
DocsisTlvs["05"]["description"] = "ModemCapabilities"
DocsisTlvs["05"]["hex"] = "5"
DocsisTlvs["05"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["05"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["1"] = {}
DocsisTlvs["05"]["subTlvs"]["1"]["description"] = "ConcatenationSupport"
DocsisTlvs["05"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["05"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["05"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["2"] = {}
DocsisTlvs["05"]["subTlvs"]["2"]["description"] = "ModemDocsisVersion"
DocsisTlvs["05"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["05"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["05"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["3"] = {}
DocsisTlvs["05"]["subTlvs"]["3"]["description"] = "FragmentationSupport"
DocsisTlvs["05"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["05"]["subTlvs"]["3"]["datatype"] = "(encode_uchar)"
DocsisTlvs["05"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["4"] = {}
DocsisTlvs["05"]["subTlvs"]["4"]["description"] = "PHSSupport"
DocsisTlvs["05"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["05"]["subTlvs"]["4"]["datatype"] = "(encode_uchar)"
DocsisTlvs["05"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["5"] = {}
DocsisTlvs["05"]["subTlvs"]["5"]["description"] = "IGMPSupport"
DocsisTlvs["05"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["05"]["subTlvs"]["5"]["datatype"] = "(encode_uchar)"
DocsisTlvs["05"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["6"] = {}
DocsisTlvs["05"]["subTlvs"]["6"]["description"] = "BaselinePrivacySupport"
DocsisTlvs["05"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["05"]["subTlvs"]["6"]["datatype"] = "(encode_uchar)"
DocsisTlvs["05"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["7"] = {}
DocsisTlvs["05"]["subTlvs"]["7"]["description"] = "DownstreamSAIDSupport"
DocsisTlvs["05"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["05"]["subTlvs"]["7"]["datatype"] = "(encode_uchar)"
DocsisTlvs["05"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["8"] = {}
DocsisTlvs["05"]["subTlvs"]["8"]["description"] = "UpstreamSIDSupport"
DocsisTlvs["05"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["05"]["subTlvs"]["8"]["datatype"] = "(encode_uchar)"
DocsisTlvs["05"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["9"] = {}
DocsisTlvs["05"]["subTlvs"]["9"]["description"] = "OptionalFilteringSupport"
DocsisTlvs["05"]["subTlvs"]["9"]["hex"] = "9"
DocsisTlvs["05"]["subTlvs"]["9"]["datatype"] = "(encode_uchar)"
DocsisTlvs["05"]["subTlvs"]["9"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["10"] = {}
DocsisTlvs["05"]["subTlvs"]["10"]["description"] = "TransmitPreEqualizerTapsPerModulationInterval"
DocsisTlvs["05"]["subTlvs"]["10"]["hex"] = "a"
DocsisTlvs["05"]["subTlvs"]["10"]["datatype"] = "(encode_uchar)"
DocsisTlvs["05"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["11"] = {}
DocsisTlvs["05"]["subTlvs"]["11"]["description"] = "NumberofTransmitEqualizerTaps"
DocsisTlvs["05"]["subTlvs"]["11"]["hex"] = "b"
DocsisTlvs["05"]["subTlvs"]["11"]["datatype"] = "(encode_uchar)"
DocsisTlvs["05"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["12"] = {}
DocsisTlvs["05"]["subTlvs"]["12"]["description"] = "DCCSupport"
DocsisTlvs["05"]["subTlvs"]["12"]["hex"] = "c"
DocsisTlvs["05"]["subTlvs"]["12"]["datatype"] = "(encode_uchar)"
DocsisTlvs["05"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["13"] = {}
DocsisTlvs["05"]["subTlvs"]["13"]["description"] = "IPFiltersSupport"
DocsisTlvs["05"]["subTlvs"]["13"]["hex"] = "d"
DocsisTlvs["05"]["subTlvs"]["13"]["datatype"] = "(encode_ushort)"
DocsisTlvs["05"]["subTlvs"]["13"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["14"] = {}
DocsisTlvs["05"]["subTlvs"]["14"]["description"] = "LLCFiltersSupport"
DocsisTlvs["05"]["subTlvs"]["14"]["hex"] = "e"
DocsisTlvs["05"]["subTlvs"]["14"]["datatype"] = "(encode_ushort)"
DocsisTlvs["05"]["subTlvs"]["14"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["15"] = {}
DocsisTlvs["05"]["subTlvs"]["15"]["description"] = "ExpandedUnicastSIDSpace"
DocsisTlvs["05"]["subTlvs"]["15"]["hex"] = "f"
DocsisTlvs["05"]["subTlvs"]["15"]["datatype"] = "(encode_uchar)"
DocsisTlvs["05"]["subTlvs"]["15"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["16"] = {}
DocsisTlvs["05"]["subTlvs"]["16"]["description"] = "RangingHoldOffSupport"
DocsisTlvs["05"]["subTlvs"]["16"]["hex"] = "10"
DocsisTlvs["05"]["subTlvs"]["16"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["05"]["subTlvs"]["16"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["17"] = {}
DocsisTlvs["05"]["subTlvs"]["17"]["description"] = "L2VPNCapability"
DocsisTlvs["05"]["subTlvs"]["17"]["hex"] = "11"
DocsisTlvs["05"]["subTlvs"]["17"]["datatype"] = "(encode_uchar)"
DocsisTlvs["05"]["subTlvs"]["17"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["18"] = {}
DocsisTlvs["05"]["subTlvs"]["18"]["description"] = "L2VPNeSAFEHostCapability"
DocsisTlvs["05"]["subTlvs"]["18"]["hex"] = "12"
DocsisTlvs["05"]["subTlvs"]["18"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["05"]["subTlvs"]["18"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["19"] = {}
DocsisTlvs["05"]["subTlvs"]["19"]["description"] = "DUTFilteringSupport"
DocsisTlvs["05"]["subTlvs"]["19"]["hex"] = "13"
DocsisTlvs["05"]["subTlvs"]["19"]["datatype"] = "(encode_uchar)"
DocsisTlvs["05"]["subTlvs"]["19"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["20"] = {}
DocsisTlvs["05"]["subTlvs"]["20"]["description"] = "UpstreamFrequencyRangeSupport"
DocsisTlvs["05"]["subTlvs"]["20"]["hex"] = "14"
DocsisTlvs["05"]["subTlvs"]["20"]["datatype"] = "(encode_uchar)"
DocsisTlvs["05"]["subTlvs"]["20"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["21"] = {}
DocsisTlvs["05"]["subTlvs"]["21"]["description"] = "UpstreamSymbolRateSupport"
DocsisTlvs["05"]["subTlvs"]["21"]["hex"] = "15"
DocsisTlvs["05"]["subTlvs"]["21"]["datatype"] = "(encode_uchar)"
DocsisTlvs["05"]["subTlvs"]["21"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["22"] = {}
DocsisTlvs["05"]["subTlvs"]["22"]["description"] = "SelectableActiveCodeMode2Support"
DocsisTlvs["05"]["subTlvs"]["22"]["hex"] = "16"
DocsisTlvs["05"]["subTlvs"]["22"]["datatype"] = "(encode_uchar)"
DocsisTlvs["05"]["subTlvs"]["22"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["23"] = {}
DocsisTlvs["05"]["subTlvs"]["23"]["description"] = "CodeHoppingMode2Support"
DocsisTlvs["05"]["subTlvs"]["23"]["hex"] = "17"
DocsisTlvs["05"]["subTlvs"]["23"]["datatype"] = "(encode_uchar)"
DocsisTlvs["05"]["subTlvs"]["23"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["24"] = {}
DocsisTlvs["05"]["subTlvs"]["24"]["description"] = "MultipleTransmitChannelSupport"
DocsisTlvs["05"]["subTlvs"]["24"]["hex"] = "18"
DocsisTlvs["05"]["subTlvs"]["24"]["datatype"] = "(encode_uchar)"
DocsisTlvs["05"]["subTlvs"]["24"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["25"] = {}
DocsisTlvs["05"]["subTlvs"]["25"]["description"] = "M512MspsUpstreamTransmitChannel"
DocsisTlvs["05"]["subTlvs"]["25"]["hex"] = "19"
DocsisTlvs["05"]["subTlvs"]["25"]["datatype"] = "(encode_uchar)"
DocsisTlvs["05"]["subTlvs"]["25"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["26"] = {}
DocsisTlvs["05"]["subTlvs"]["26"]["description"] = "M256MspsUpstreamTransmitChannel"
DocsisTlvs["05"]["subTlvs"]["26"]["hex"] = "1a"
DocsisTlvs["05"]["subTlvs"]["26"]["datatype"] = "(encode_uchar)"
DocsisTlvs["05"]["subTlvs"]["26"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["27"] = {}
DocsisTlvs["05"]["subTlvs"]["27"]["description"] = "TotalSIDClusterSupport"
DocsisTlvs["05"]["subTlvs"]["27"]["hex"] = "1b"
DocsisTlvs["05"]["subTlvs"]["27"]["datatype"] = "(encode_uchar)"
DocsisTlvs["05"]["subTlvs"]["27"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["28"] = {}
DocsisTlvs["05"]["subTlvs"]["28"]["description"] = "SIDClustersPerServiceFlow"
DocsisTlvs["05"]["subTlvs"]["28"]["hex"] = "1c"
DocsisTlvs["05"]["subTlvs"]["28"]["datatype"] = "(encode_uchar)"
DocsisTlvs["05"]["subTlvs"]["28"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["29"] = {}
DocsisTlvs["05"]["subTlvs"]["29"]["description"] = "MultipleReceiveChannelSupport"
DocsisTlvs["05"]["subTlvs"]["29"]["hex"] = "1d"
DocsisTlvs["05"]["subTlvs"]["29"]["datatype"] = "(encode_uchar)"
DocsisTlvs["05"]["subTlvs"]["29"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["30"] = {}
DocsisTlvs["05"]["subTlvs"]["30"]["description"] = "TotalDownstreamServiceIDSupport"
DocsisTlvs["05"]["subTlvs"]["30"]["hex"] = "1e"
DocsisTlvs["05"]["subTlvs"]["30"]["datatype"] = "(encode_uchar)"
DocsisTlvs["05"]["subTlvs"]["30"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["31"] = {}
DocsisTlvs["05"]["subTlvs"]["31"]["description"] = "ResequencingDownstreamServiceID"
DocsisTlvs["05"]["subTlvs"]["31"]["hex"] = "1f"
DocsisTlvs["05"]["subTlvs"]["31"]["datatype"] = "(encode_uchar)"
DocsisTlvs["05"]["subTlvs"]["31"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["32"] = {}
DocsisTlvs["05"]["subTlvs"]["32"]["description"] = "MulticastDownstreamServiceID"
DocsisTlvs["05"]["subTlvs"]["32"]["hex"] = "20"
DocsisTlvs["05"]["subTlvs"]["32"]["datatype"] = "(encode_uchar)"
DocsisTlvs["05"]["subTlvs"]["32"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["33"] = {}
DocsisTlvs["05"]["subTlvs"]["33"]["description"] = "MulticastDSIDForwarding"
DocsisTlvs["05"]["subTlvs"]["33"]["hex"] = "21"
DocsisTlvs["05"]["subTlvs"]["33"]["datatype"] = "(encode_uchar)"
DocsisTlvs["05"]["subTlvs"]["33"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["34"] = {}
DocsisTlvs["05"]["subTlvs"]["34"]["description"] = "FrameControlTypeForwarding"
DocsisTlvs["05"]["subTlvs"]["34"]["hex"] = "22"
DocsisTlvs["05"]["subTlvs"]["34"]["datatype"] = "(encode_uchar)"
DocsisTlvs["05"]["subTlvs"]["34"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["35"] = {}
DocsisTlvs["05"]["subTlvs"]["35"]["description"] = "DPVCapability"
DocsisTlvs["05"]["subTlvs"]["35"]["hex"] = "23"
DocsisTlvs["05"]["subTlvs"]["35"]["datatype"] = "(encode_uchar)"
DocsisTlvs["05"]["subTlvs"]["35"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["36"] = {}
DocsisTlvs["05"]["subTlvs"]["36"]["description"] = "UnsolicitedGrantServiceSupport"
DocsisTlvs["05"]["subTlvs"]["36"]["hex"] = "24"
DocsisTlvs["05"]["subTlvs"]["36"]["datatype"] = "(encode_uchar)"
DocsisTlvs["05"]["subTlvs"]["36"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["37"] = {}
DocsisTlvs["05"]["subTlvs"]["37"]["description"] = "MAPandUCDReceiptSupport"
DocsisTlvs["05"]["subTlvs"]["37"]["hex"] = "25"
DocsisTlvs["05"]["subTlvs"]["37"]["datatype"] = "(encode_uchar)"
DocsisTlvs["05"]["subTlvs"]["37"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["38"] = {}
DocsisTlvs["05"]["subTlvs"]["38"]["description"] = "UpstreamDropClassifierSupport"
DocsisTlvs["05"]["subTlvs"]["38"]["hex"] = "26"
DocsisTlvs["05"]["subTlvs"]["38"]["datatype"] = "(encode_ushort)"
DocsisTlvs["05"]["subTlvs"]["38"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["39"] = {}
DocsisTlvs["05"]["subTlvs"]["39"]["description"] = "IPv6Support"
DocsisTlvs["05"]["subTlvs"]["39"]["hex"] = "27"
DocsisTlvs["05"]["subTlvs"]["39"]["datatype"] = "(encode_uchar)"
DocsisTlvs["05"]["subTlvs"]["39"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["40"] = {}
DocsisTlvs["05"]["subTlvs"]["40"]["description"] = "ExtendedUpstreamTransmitPower"
DocsisTlvs["05"]["subTlvs"]["40"]["hex"] = "28"
DocsisTlvs["05"]["subTlvs"]["40"]["datatype"] = "(encode_uchar)"
DocsisTlvs["05"]["subTlvs"]["40"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["41"] = {}
DocsisTlvs["05"]["subTlvs"]["41"]["description"] = "MPLSClassificationSupport"
DocsisTlvs["05"]["subTlvs"]["41"]["hex"] = "29"
DocsisTlvs["05"]["subTlvs"]["41"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["05"]["subTlvs"]["41"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["42"] = {}
DocsisTlvs["05"]["subTlvs"]["42"]["description"] = "DONUCapabilitiesEncoding"
DocsisTlvs["05"]["subTlvs"]["42"]["hex"] = "2a"
DocsisTlvs["05"]["subTlvs"]["42"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["05"]["subTlvs"]["42"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["44"] = {}
DocsisTlvs["05"]["subTlvs"]["44"]["description"] = "EnergyManagementCapabilities"
DocsisTlvs["05"]["subTlvs"]["44"]["hex"] = "2c"
DocsisTlvs["05"]["subTlvs"]["44"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["05"]["subTlvs"]["44"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["45"] = {}
DocsisTlvs["05"]["subTlvs"]["45"]["description"] = "CDOCSISCapabilityEncoding"
DocsisTlvs["05"]["subTlvs"]["45"]["hex"] = "2d"
DocsisTlvs["05"]["subTlvs"]["45"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["05"]["subTlvs"]["45"]["subTlvs"] = {}

DocsisTlvs["05"]["subTlvs"]["46"] = {}
DocsisTlvs["05"]["subTlvs"]["46"]["description"] = "CMSTATUSACK"
DocsisTlvs["05"]["subTlvs"]["46"]["hex"] = "2e"
DocsisTlvs["05"]["subTlvs"]["46"]["datatype"] = "(encode_uchar)"
DocsisTlvs["05"]["subTlvs"]["46"]["subTlvs"] = {}

DocsisTlvs["06"] = {}
DocsisTlvs["06"]["description"] = "CmMic"
DocsisTlvs["06"]["hex"] = "6"
DocsisTlvs["06"]["datatype"] = "(decode_md5)"
DocsisTlvs["06"]["subTlvs"] = {}

DocsisTlvs["07"] = {}
DocsisTlvs["07"]["description"] = "CmtsMic"
DocsisTlvs["07"]["hex"] = "7"
DocsisTlvs["07"]["datatype"] = "(decode_md5)"
DocsisTlvs["07"]["subTlvs"] = {}

DocsisTlvs["09"] = {}
DocsisTlvs["09"]["description"] = "SwUpgradeFilename"
DocsisTlvs["09"]["hex"] = "9"
DocsisTlvs["09"]["datatype"] = "(encode_string)"
DocsisTlvs["09"]["subTlvs"] = {}

DocsisTlvs["10"] = {}
DocsisTlvs["10"]["description"] = "SnmpWriteControl"
DocsisTlvs["10"]["hex"] = "a"
DocsisTlvs["10"]["datatype"] = "(decode_snmp_wd)"
DocsisTlvs["10"]["subTlvs"] = {}

DocsisTlvs["11"] = {}
DocsisTlvs["11"]["description"] = "SnmpMibObject"
DocsisTlvs["11"]["hex"] = "b"
DocsisTlvs["11"]["datatype"] = "(decode_snmp_object)"
DocsisTlvs["11"]["subTlvs"] = {}

DocsisTlvs["12"] = {}
DocsisTlvs["12"]["description"] = "ModemIPAddress"
DocsisTlvs["12"]["hex"] = "c"
DocsisTlvs["12"]["datatype"] = "(encode_ip)"
DocsisTlvs["12"]["subTlvs"] = {}

DocsisTlvs["14"] = {}
DocsisTlvs["14"]["description"] = "CpeMacAddress"
DocsisTlvs["14"]["hex"] = "e"
DocsisTlvs["14"]["datatype"] = "(encode_ether)"
DocsisTlvs["14"]["subTlvs"] = {}

DocsisTlvs["17"] = {}
DocsisTlvs["17"]["description"] = "BaselinePrivacy"
DocsisTlvs["17"]["hex"] = "11"
DocsisTlvs["17"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["17"]["subTlvs"] = {}

DocsisTlvs["17"]["subTlvs"]["1"] = {}
DocsisTlvs["17"]["subTlvs"]["1"]["description"] = "AuthTimeout"
DocsisTlvs["17"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["17"]["subTlvs"]["1"]["datatype"] = "(encode_uint)"
DocsisTlvs["17"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["17"]["subTlvs"]["2"] = {}
DocsisTlvs["17"]["subTlvs"]["2"]["description"] = "ReAuthTimeout"
DocsisTlvs["17"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["17"]["subTlvs"]["2"]["datatype"] = "(encode_uint)"
DocsisTlvs["17"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["17"]["subTlvs"]["3"] = {}
DocsisTlvs["17"]["subTlvs"]["3"]["description"] = "AuthGraceTime"
DocsisTlvs["17"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["17"]["subTlvs"]["3"]["datatype"] = "(encode_uint)"
DocsisTlvs["17"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["17"]["subTlvs"]["4"] = {}
DocsisTlvs["17"]["subTlvs"]["4"]["description"] = "OperTimeout"
DocsisTlvs["17"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["17"]["subTlvs"]["4"]["datatype"] = "(encode_uint)"
DocsisTlvs["17"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["17"]["subTlvs"]["5"] = {}
DocsisTlvs["17"]["subTlvs"]["5"]["description"] = "ReKeyTimeout"
DocsisTlvs["17"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["17"]["subTlvs"]["5"]["datatype"] = "(encode_uint)"
DocsisTlvs["17"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["17"]["subTlvs"]["6"] = {}
DocsisTlvs["17"]["subTlvs"]["6"]["description"] = "TEKGraceTime"
DocsisTlvs["17"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["17"]["subTlvs"]["6"]["datatype"] = "(encode_uint)"
DocsisTlvs["17"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["17"]["subTlvs"]["7"] = {}
DocsisTlvs["17"]["subTlvs"]["7"]["description"] = "AuthRejectTimeout"
DocsisTlvs["17"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["17"]["subTlvs"]["7"]["datatype"] = "(encode_uint)"
DocsisTlvs["17"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["17"]["subTlvs"]["8"] = {}
DocsisTlvs["17"]["subTlvs"]["8"]["description"] = "SAMapWaitTimeout"
DocsisTlvs["17"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["17"]["subTlvs"]["8"]["datatype"] = "(encode_uint)"
DocsisTlvs["17"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["17"]["subTlvs"]["9"] = {}
DocsisTlvs["17"]["subTlvs"]["9"]["description"] = "SAMapMaxRetries"
DocsisTlvs["17"]["subTlvs"]["9"]["hex"] = "9"
DocsisTlvs["17"]["subTlvs"]["9"]["datatype"] = "(encode_uint)"
DocsisTlvs["17"]["subTlvs"]["9"]["subTlvs"] = {}

DocsisTlvs["18"] = {}
DocsisTlvs["18"]["description"] = "MaxCPE"
DocsisTlvs["18"]["hex"] = "12"
DocsisTlvs["18"]["datatype"] = "(encode_uchar)"
DocsisTlvs["18"]["subTlvs"] = {}

DocsisTlvs["19"] = {}
DocsisTlvs["19"]["description"] = "TftpTimestamp"
DocsisTlvs["19"]["hex"] = "13"
DocsisTlvs["19"]["datatype"] = "(encode_uint)"
DocsisTlvs["19"]["subTlvs"] = {}

DocsisTlvs["20"] = {}
DocsisTlvs["20"]["description"] = "TftpModemAddress"
DocsisTlvs["20"]["hex"] = "14"
DocsisTlvs["20"]["datatype"] = "(encode_ip)"
DocsisTlvs["20"]["subTlvs"] = {}

DocsisTlvs["21"] = {}
DocsisTlvs["21"]["description"] = "SwUpgradeServer"
DocsisTlvs["21"]["hex"] = "15"
DocsisTlvs["21"]["datatype"] = "(encode_ip)"
DocsisTlvs["21"]["subTlvs"] = {}

DocsisTlvs["22"] = {}
DocsisTlvs["22"]["description"] = "UsPacketClass"
DocsisTlvs["22"]["hex"] = "16"
DocsisTlvs["22"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["22"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["1"] = {}
DocsisTlvs["22"]["subTlvs"]["1"]["description"] = "ClassifierRef"
DocsisTlvs["22"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["22"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["22"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["2"] = {}
DocsisTlvs["22"]["subTlvs"]["2"]["description"] = "ClassifierId"
DocsisTlvs["22"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["22"]["subTlvs"]["2"]["datatype"] = "(encode_ushort)"
DocsisTlvs["22"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["3"] = {}
DocsisTlvs["22"]["subTlvs"]["3"]["description"] = "ServiceFlowRef"
DocsisTlvs["22"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["22"]["subTlvs"]["3"]["datatype"] = "(encode_ushort)"
DocsisTlvs["22"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["4"] = {}
DocsisTlvs["22"]["subTlvs"]["4"]["description"] = "ServiceFlowId"
DocsisTlvs["22"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["22"]["subTlvs"]["4"]["datatype"] = "(encode_uint)"
DocsisTlvs["22"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["5"] = {}
DocsisTlvs["22"]["subTlvs"]["5"]["description"] = "RulePriority"
DocsisTlvs["22"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["22"]["subTlvs"]["5"]["datatype"] = "(encode_uchar)"
DocsisTlvs["22"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["6"] = {}
DocsisTlvs["22"]["subTlvs"]["6"]["description"] = "ActivationState"
DocsisTlvs["22"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["22"]["subTlvs"]["6"]["datatype"] = "(encode_uchar)"
DocsisTlvs["22"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["7"] = {}
DocsisTlvs["22"]["subTlvs"]["7"]["description"] = "DscAction"
DocsisTlvs["22"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["22"]["subTlvs"]["7"]["datatype"] = "(encode_uchar)"
DocsisTlvs["22"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["9"] = {}
DocsisTlvs["22"]["subTlvs"]["9"]["description"] = "IpPacketClassifier"
DocsisTlvs["22"]["subTlvs"]["9"]["hex"] = "9"
DocsisTlvs["22"]["subTlvs"]["9"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["1"] = {}
DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["1"]["description"] = "IpTos"
DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["2"] = {}
DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["2"]["description"] = "IpProto"
DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["2"]["datatype"] = "(encode_ushort)"
DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["3"] = {}
DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["3"]["description"] = "IpSrcAddr"
DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["3"]["datatype"] = "(encode_ip)"
DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["4"] = {}
DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["4"]["description"] = "IpSrcMask"
DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["4"]["datatype"] = "(encode_ip)"
DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["5"] = {}
DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["5"]["description"] = "IpDstAddr"
DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["5"]["datatype"] = "(encode_ip)"
DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["6"] = {}
DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["6"]["description"] = "IpDstMask"
DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["6"]["datatype"] = "(encode_ip)"
DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["7"] = {}
DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["7"]["description"] = "SrcPortStart"
DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["7"]["datatype"] = "(encode_ushort)"
DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["8"] = {}
DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["8"]["description"] = "SrcPortEnd"
DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["8"]["datatype"] = "(encode_ushort)"
DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["9"] = {}
DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["9"]["description"] = "DstPortStart"
DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["9"]["hex"] = "9"
DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["9"]["datatype"] = "(encode_ushort)"
DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["9"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["10"] = {}
DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["10"]["description"] = "DstPortEnd"
DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["10"]["hex"] = "a"
DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["10"]["datatype"] = "(encode_ushort)"
DocsisTlvs["22"]["subTlvs"]["9"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["10"] = {}
DocsisTlvs["22"]["subTlvs"]["10"]["description"] = "LLCPacketClassifier"
DocsisTlvs["22"]["subTlvs"]["10"]["hex"] = "a"
DocsisTlvs["22"]["subTlvs"]["10"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["22"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["10"]["subTlvs"]["1"] = {}
DocsisTlvs["22"]["subTlvs"]["10"]["subTlvs"]["1"]["description"] = "DstMacAddress"
DocsisTlvs["22"]["subTlvs"]["10"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["22"]["subTlvs"]["10"]["subTlvs"]["1"]["datatype"] = "(encode_ethermask)"
DocsisTlvs["22"]["subTlvs"]["10"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["10"]["subTlvs"]["2"] = {}
DocsisTlvs["22"]["subTlvs"]["10"]["subTlvs"]["2"]["description"] = "SrcMacAddress"
DocsisTlvs["22"]["subTlvs"]["10"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["22"]["subTlvs"]["10"]["subTlvs"]["2"]["datatype"] = "(encode_ether)"
DocsisTlvs["22"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["10"]["subTlvs"]["3"] = {}
DocsisTlvs["22"]["subTlvs"]["10"]["subTlvs"]["3"]["description"] = "EtherType"
DocsisTlvs["22"]["subTlvs"]["10"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["22"]["subTlvs"]["10"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["10"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["11"] = {}
DocsisTlvs["22"]["subTlvs"]["11"]["description"] = "IEEE802Classifier"
DocsisTlvs["22"]["subTlvs"]["11"]["hex"] = "b"
DocsisTlvs["22"]["subTlvs"]["11"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["22"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["11"]["subTlvs"]["1"] = {}
DocsisTlvs["22"]["subTlvs"]["11"]["subTlvs"]["1"]["description"] = "UserPriority"
DocsisTlvs["22"]["subTlvs"]["11"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["22"]["subTlvs"]["11"]["subTlvs"]["1"]["datatype"] = "(encode_char_list)"
DocsisTlvs["22"]["subTlvs"]["11"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["11"]["subTlvs"]["2"] = {}
DocsisTlvs["22"]["subTlvs"]["11"]["subTlvs"]["2"]["description"] = "VlanID"
DocsisTlvs["22"]["subTlvs"]["11"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["22"]["subTlvs"]["11"]["subTlvs"]["2"]["datatype"] = "(encode_ushort)"
DocsisTlvs["22"]["subTlvs"]["11"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["12"] = {}
DocsisTlvs["22"]["subTlvs"]["12"]["description"] = "PcIPv6PacketClassification"
DocsisTlvs["22"]["subTlvs"]["12"]["hex"] = "c"
DocsisTlvs["22"]["subTlvs"]["12"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["1"] = {}
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["1"]["description"] = "PcIPv6TrafficClassRangeAndMask"
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["2"] = {}
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["2"]["description"] = "PcIPv6FlowLabel"
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["3"] = {}
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["3"]["description"] = "PcIPv6NextHeaderType"
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["3"]["datatype"] = "(encode_ushort)"
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["4"] = {}
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["4"]["description"] = "PcIPv6SourceAddress"
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["4"]["datatype"] = "(encode_ip6)"
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["5"] = {}
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["5"]["description"] = "PcIPv6SourcePrefixLength"
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["5"]["datatype"] = "(encode_uchar)"
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["6"] = {}
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["6"]["description"] = "PcIPv6DestAddress"
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["6"]["datatype"] = "(encode_ip6)"
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["7"] = {}
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["7"]["description"] = "PcIPv6DestPrefixLength"
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["7"]["datatype"] = "(encode_uchar)"
DocsisTlvs["22"]["subTlvs"]["12"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["13"] = {}
DocsisTlvs["22"]["subTlvs"]["13"]["description"] = "PcCMIMEncoding"
DocsisTlvs["22"]["subTlvs"]["13"]["hex"] = "d"
DocsisTlvs["22"]["subTlvs"]["13"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["13"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["14"] = {}
DocsisTlvs["22"]["subTlvs"]["14"]["description"] = "STagCTagFrameClassification"
DocsisTlvs["22"]["subTlvs"]["14"]["hex"] = "e"
DocsisTlvs["22"]["subTlvs"]["14"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["1"] = {}
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["1"]["description"] = "STPID"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["2"] = {}
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["2"]["description"] = "SVID"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["3"] = {}
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["3"]["description"] = "SPCP"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["4"] = {}
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["4"]["description"] = "SDEI"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["5"] = {}
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["5"]["description"] = "CTPID"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["5"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["6"] = {}
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["6"]["description"] = "CVID"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["6"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["7"] = {}
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["7"]["description"] = "CPCP"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["7"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["8"] = {}
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["8"]["description"] = "CCFI"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["8"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["9"] = {}
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["9"]["description"] = "STCI"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["9"]["hex"] = "9"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["9"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["9"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["10"] = {}
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["10"]["description"] = "CTCI"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["10"]["hex"] = "a"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["10"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["14"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["15"] = {}
DocsisTlvs["22"]["subTlvs"]["15"]["description"] = "IEEE8021ahPacketClassification"
DocsisTlvs["22"]["subTlvs"]["15"]["hex"] = "f"
DocsisTlvs["22"]["subTlvs"]["15"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["1"] = {}
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["1"]["description"] = "ITPID"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["2"] = {}
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["2"]["description"] = "ISID"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["3"] = {}
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["3"]["description"] = "ITCI"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["4"] = {}
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["4"]["description"] = "IPCP"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["5"] = {}
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["5"]["description"] = "IDEI"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["5"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["6"] = {}
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["6"]["description"] = "IUCA"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["6"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["7"] = {}
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["7"]["description"] = "BTPID"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["7"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["8"] = {}
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["8"]["description"] = "BTCI"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["8"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["9"] = {}
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["9"]["description"] = "BPCP"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["9"]["hex"] = "9"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["9"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["9"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["10"] = {}
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["10"]["description"] = "BDEI"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["10"]["hex"] = "a"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["10"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["11"] = {}
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["11"]["description"] = "BVID"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["11"]["hex"] = "b"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["11"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["12"] = {}
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["12"]["description"] = "BDA"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["12"]["hex"] = "c"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["12"]["datatype"] = "(encode_ether)"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["13"] = {}
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["13"]["description"] = "BSA"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["13"]["hex"] = "d"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["13"]["datatype"] = "(encode_ether)"
DocsisTlvs["22"]["subTlvs"]["15"]["subTlvs"]["13"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["16"] = {}
DocsisTlvs["22"]["subTlvs"]["16"]["description"] = "ICMPv4ICMPv6PacketClassification"
DocsisTlvs["22"]["subTlvs"]["16"]["hex"] = "10"
DocsisTlvs["22"]["subTlvs"]["16"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["22"]["subTlvs"]["16"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["16"]["subTlvs"]["1"] = {}
DocsisTlvs["22"]["subTlvs"]["16"]["subTlvs"]["1"]["description"] = "ICMPv4ICMPv6TypeStart"
DocsisTlvs["22"]["subTlvs"]["16"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["22"]["subTlvs"]["16"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["22"]["subTlvs"]["16"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["16"]["subTlvs"]["2"] = {}
DocsisTlvs["22"]["subTlvs"]["16"]["subTlvs"]["2"]["description"] = "ICMPv4ICMPv6TypeEnd"
DocsisTlvs["22"]["subTlvs"]["16"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["22"]["subTlvs"]["16"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["22"]["subTlvs"]["16"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["17"] = {}
DocsisTlvs["22"]["subTlvs"]["17"]["description"] = "MPLSClassificationEncoding"
DocsisTlvs["22"]["subTlvs"]["17"]["hex"] = "11"
DocsisTlvs["22"]["subTlvs"]["17"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["22"]["subTlvs"]["17"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["17"]["subTlvs"]["1"] = {}
DocsisTlvs["22"]["subTlvs"]["17"]["subTlvs"]["1"]["description"] = "MPLSTCbits"
DocsisTlvs["22"]["subTlvs"]["17"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["22"]["subTlvs"]["17"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["17"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["17"]["subTlvs"]["2"] = {}
DocsisTlvs["22"]["subTlvs"]["17"]["subTlvs"]["2"]["description"] = "MPLSLabel"
DocsisTlvs["22"]["subTlvs"]["17"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["22"]["subTlvs"]["17"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["17"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["description"] = "VendorSpecific"
DocsisTlvs["22"]["subTlvs"]["43"]["hex"] = "2b"
DocsisTlvs["22"]["subTlvs"]["43"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["1"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["1"]["description"] = "CMLoadBalancingPolicyID"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["1"]["datatype"] = "(encode_uint)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["2"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["2"]["description"] = "CMLoadBalancingPriority"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["2"]["datatype"] = "(encode_uint)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["3"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["3"]["description"] = "CMLoadBalancingGroupID"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["3"]["datatype"] = "(encode_uint)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["4"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["4"]["description"] = "CMRangingClassIDExtension"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["4"]["datatype"] = "(encode_ushort)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["description"] = "L2VPNEncoding"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["1"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["1"]["description"] = "VPNIdentifier"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["description"] = "NSIEncapsulation"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["1"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["1"]["description"] = "ServiceMultiplexingValueOther"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["1"]["datatype"] = "(encode_lenzero)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["2"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["2"]["description"] = "NSIEncapsulationSingleQTag"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["2"]["datatype"] = "(encode_ushort)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["3"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["3"]["description"] = "NSIEncapsulationDualQTag"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["3"]["datatype"] = "(encode_dual_qtag)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["description"] = "ServiceMultiplexingValueMPLSPW"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["1"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["1"]["description"] = "MPLSPseudowireID"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["1"]["datatype"] = "(encode_uint)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["2"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["2"]["description"] = "MPLSPeerIpAddress"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["2"]["datatype"] = "(encode_char_ip_ip6)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["3"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["3"]["description"] = "MPLSPseudowireType"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["3"]["datatype"] = "(encode_uchar)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["4"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["4"]["description"] = "MPLSBackupPseudowireID"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["4"]["datatype"] = "(encode_uint)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["5"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["5"]["description"] = "MPLSBackupPeerIpAddress"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["5"]["datatype"] = "(encode_char_ip_ip6)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["5"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["5"]["description"] = "ServiceMultiplexingValueL2TPv3Peer"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["5"]["datatype"] = "(encode_char_ip_ip6)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["description"] = "IEEE8021ahEncapsulation"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["1"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["1"]["description"] = "ITCIEncapsulation"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["2"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["2"]["description"] = "BDAEncapsulation"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["3"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["3"]["description"] = "BTCIEncapsulation"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["4"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["4"]["description"] = "ITPIDEncapsulation"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["5"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["5"]["description"] = "IPCPEncapsulation"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["5"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["6"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["6"]["description"] = "IDEIEncapsulation"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["6"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["7"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["7"]["description"] = "IUCAEncapsulation"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["7"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["8"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["8"]["description"] = "ISIDEncapsulation"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["8"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["9"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["9"]["description"] = "BTPIDEncapsulation"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["9"]["hex"] = "9"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["9"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["9"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["10"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["10"]["description"] = "BPCPEncapsulation"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["10"]["hex"] = "a"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["10"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["11"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["11"]["description"] = "BDEIEncapsulation"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["11"]["hex"] = "b"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["11"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["12"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["12"]["description"] = "BVIDEncapsulation"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["12"]["hex"] = "c"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["12"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["8"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["8"]["description"] = "ServiceMultiplexingValueIEEE8021adSTPID"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["8"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["3"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["3"]["description"] = "eSAFEDHCPSnooping"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["4"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["4"]["description"] = "CMInterfaceMaskCMIMSubtype"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["5"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["5"]["description"] = "AttachmentGroupID"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["5"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["6"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["6"]["description"] = "SourceAttachmentIndividualID"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["6"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["7"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["7"]["description"] = "TargetAttachmentIndividualID"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["7"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["8"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["8"]["description"] = "IngressUserPriority"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["8"]["datatype"] = "(encode_uchar)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["9"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["9"]["description"] = "UserPriorityRange"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["9"]["hex"] = "9"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["9"]["datatype"] = "(encode_char_list)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["9"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["10"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["10"]["description"] = "L2VPNSADescriptorSubtype"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["10"]["hex"] = "a"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["10"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["12"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["12"]["description"] = "PseudowireType"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["12"]["hex"] = "c"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["12"]["datatype"] = "(encode_uchar)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["13"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["13"]["description"] = "L2VPNMode"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["13"]["hex"] = "d"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["13"]["datatype"] = "(encode_uchar)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["13"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["description"] = "TPIDTranslation"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["hex"] = "e"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["1"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["1"]["description"] = "UpstreamTPIDTranslation"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["2"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["2"]["description"] = "DownstreamTPIDTranslation"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["3"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["3"]["description"] = "UpstreamSTPIDTranslation"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["4"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["4"]["description"] = "DownstreamSTPIDTranslation"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["5"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["5"]["description"] = "UpstreamBTPIDTranslation"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["5"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["6"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["6"]["description"] = "DownstreamBTPIDTranslation"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["6"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["7"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["7"]["description"] = "UpstreamITPIDTranslation"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["7"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["8"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["8"]["description"] = "DownstreamITPIDTranslation"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["8"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["description"] = "L2CPProcessing"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["hex"] = "f"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["1"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["1"]["description"] = "L2CPTunnelMode"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["2"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["2"]["description"] = "L2CPDMACAddress"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["2"]["datatype"] = "(encode_ether)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["3"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["3"]["description"] = "L2CPOverwrotingDMACAddress"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["3"]["datatype"] = "(encode_ether)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["16"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["16"]["description"] = "DACDisableEnableConfiguration"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["16"]["hex"] = "10"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["16"]["datatype"] = "(encode_uchar)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["16"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["18"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["18"]["description"] = "PseudowireClass"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["18"]["hex"] = "12"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["18"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["18"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["description"] = "ServiceDelimiter"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["hex"] = "13"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["1"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["1"]["description"] = "CVIDDelimiter"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["2"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["2"]["description"] = "SVIDDelimiter"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["3"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["3"]["description"] = "ISIDDelimiter"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["4"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["4"]["description"] = "BVIDDelimiter"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["description"] = "VirtualSwitchInstanceEncoding"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["hex"] = "14"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["1"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["1"]["description"] = "VPLSClass"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["2"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["2"]["description"] = "ETreeRole"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["3"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["3"]["description"] = "ETreeRootVID"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["4"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["4"]["description"] = "ETreeLeafVID"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["description"] = "BGPAttribute"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["hex"] = "15"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["1"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["1"]["description"] = "BGPVPNID"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["1"]["datatype"] = "(encode_uint)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["2"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["2"]["description"] = "RouteDistinguisher"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["3"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["3"]["description"] = "RouteTargetImport"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["4"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["4"]["description"] = "RouteTargetExport"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["5"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["5"]["description"] = "CEIDVEID"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["5"]["datatype"] = "(encode_ushort)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["23"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["23"]["description"] = "PseudowireSignaling"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["23"]["hex"] = "17"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["23"]["datatype"] = "(encode_uchar)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["23"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["description"] = "SOAMSubtype"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["hex"] = "18"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["description"] = "MEPConfiguration"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["1"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["1"]["description"] = "MDLevel"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["2"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["2"]["description"] = "MDName"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["2"]["datatype"] = "(encode_string)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["3"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["3"]["description"] = "MAName"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["3"]["datatype"] = "(encode_string)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["4"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["4"]["description"] = "MEPID"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["4"]["datatype"] = "(encode_ushort)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["description"] = "RemoteMEPConfiguration"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["1"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["1"]["description"] = "RemoteMDLevel"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["2"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["2"]["description"] = "RemoteMDName"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["2"]["datatype"] = "(encode_string)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["3"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["3"]["description"] = "RemoteMAName"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["3"]["datatype"] = "(encode_string)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["4"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["4"]["description"] = "RemoteMEPID"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["4"]["datatype"] = "(encode_ushort)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["description"] = "FaultManagementConfiguration"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["1"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["1"]["description"] = "ContinuityCheckMessages"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["2"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["2"]["description"] = "LoopbackFunction"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["3"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["3"]["description"] = "LinktraceFunction"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["3"]["datatype"] = "(encode_uchar)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["description"] = "PerformanceManagementConfiguration"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["description"] = "FrameDelayMeasurement"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["1"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["1"]["description"] = "FrameDelayMeasurementEnable"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["2"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["2"]["description"] = "FrameDelayMeasurementOneWayTwoWay"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["3"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["3"]["description"] = "FrameDelayMeasurementTransmissionPeriodicity"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["3"]["datatype"] = "(encode_ushort)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["description"] = "FrameLossMeasurement"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["1"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["1"]["description"] = "FrameLossMeasurementEnable"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["2"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["2"]["description"] = "FrameLossMeasurementTransmissionPeriodicity"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["26"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["26"]["description"] = "L2VPNDSID"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["26"]["hex"] = "1a"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["26"]["datatype"] = "(encode_uint24)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["26"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["description"] = "VendorSpecificL2VPNSubtype"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["hex"] = "2b"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["subTlvs"]["8"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["subTlvs"]["8"]["description"] = "VendorIdentifier"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["subTlvs"]["8"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["6"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["6"]["description"] = "ExtendedCMTSMICConfigurationSetting"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["6"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["1"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["1"]["description"] = "ExtendedCMTSMICHMACtype"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["2"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["2"]["description"] = "ExtendedCMTSMICBitmap"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["3"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["3"]["description"] = "ExplicitExtendedCMTSMICDigest"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["7"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["7"]["description"] = "SAVAuthorizationEncoding"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["7"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["1"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["1"]["description"] = "SAVGroupName"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["1"]["datatype"] = "(encode_string)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["description"] = "SAVStaticPrefixRule"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["1"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["1"]["description"] = "SAVStaticPrefixAddress"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["1"]["datatype"] = "(encode_ip_ip6)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["2"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["2"]["description"] = "SAVStaticPrefixLength"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["8"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["8"]["description"] = "VendorIdentifier"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["8"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["9"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["9"]["description"] = "CMAttributeMasks"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["9"]["hex"] = "9"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["9"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["1"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["1"]["description"] = "CMDownstreamRequiredAttributeMask"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["2"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["2"]["description"] = "CMDownstreamForbiddenAttributeMask"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["3"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["3"]["description"] = "CMUpstreamRequiredAttributeMask"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["4"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["4"]["description"] = "CMUpstreamForbiddenAttributeMask"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["description"] = "IPMulticastJoinAuthorization"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["hex"] = "a"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["1"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["1"]["description"] = "IPMulticastProfileName"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["1"]["datatype"] = "(encode_string)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["description"] = "IPMulticastJoinAuthStaticSessionRule"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["1"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["1"]["description"] = "MulticastRulePriority"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["2"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["2"]["description"] = "AuthorizationAction"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["3"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["3"]["description"] = "SourcePrefixAddress"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["3"]["datatype"] = "(encode_ip_ip6)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["4"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["4"]["description"] = "SourcePrefixLength"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["4"]["datatype"] = "(encode_uchar)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["5"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["5"]["description"] = "GroupPrefixAddress"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["5"]["datatype"] = "(encode_ip_ip6)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["6"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["6"]["description"] = "GroupPrefixLength"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["6"]["datatype"] = "(encode_uchar)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["3"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["3"]["description"] = "MaximumMulticastSessions"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["3"]["datatype"] = "(encode_ushort)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["11"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["11"]["description"] = "ServiceTypeIdentifier"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["11"]["hex"] = "b"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["11"]["datatype"] = "(encode_string)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"]["description"] = "DEMARCAutoConfiguration"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"]["hex"] = "c"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["1"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["1"]["description"] = "DACDisableEnableConfig"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["2"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["2"]["description"] = "CMIMEncoding"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["3"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["3"]["description"] = "UpstreamServiceClassName"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["3"]["datatype"] = "(encode_strzero)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["4"] = {}
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["4"]["description"] = "DownstreamServiceClassName"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["4"]["datatype"] = "(encode_strzero)"
DocsisTlvs["22"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["23"] = {}
DocsisTlvs["23"]["description"] = "DsPacketClass"
DocsisTlvs["23"]["hex"] = "17"
DocsisTlvs["23"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["23"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["1"] = {}
DocsisTlvs["23"]["subTlvs"]["1"]["description"] = "ClassifierRef"
DocsisTlvs["23"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["23"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["23"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["2"] = {}
DocsisTlvs["23"]["subTlvs"]["2"]["description"] = "ClassifierId"
DocsisTlvs["23"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["23"]["subTlvs"]["2"]["datatype"] = "(encode_ushort)"
DocsisTlvs["23"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["3"] = {}
DocsisTlvs["23"]["subTlvs"]["3"]["description"] = "ServiceFlowRef"
DocsisTlvs["23"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["23"]["subTlvs"]["3"]["datatype"] = "(encode_ushort)"
DocsisTlvs["23"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["4"] = {}
DocsisTlvs["23"]["subTlvs"]["4"]["description"] = "ServiceFlowId"
DocsisTlvs["23"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["23"]["subTlvs"]["4"]["datatype"] = "(encode_uint)"
DocsisTlvs["23"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["5"] = {}
DocsisTlvs["23"]["subTlvs"]["5"]["description"] = "RulePriority"
DocsisTlvs["23"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["23"]["subTlvs"]["5"]["datatype"] = "(encode_uchar)"
DocsisTlvs["23"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["6"] = {}
DocsisTlvs["23"]["subTlvs"]["6"]["description"] = "ActivationState"
DocsisTlvs["23"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["23"]["subTlvs"]["6"]["datatype"] = "(encode_uchar)"
DocsisTlvs["23"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["7"] = {}
DocsisTlvs["23"]["subTlvs"]["7"]["description"] = "DscAction"
DocsisTlvs["23"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["23"]["subTlvs"]["7"]["datatype"] = "(encode_uchar)"
DocsisTlvs["23"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["9"] = {}
DocsisTlvs["23"]["subTlvs"]["9"]["description"] = "IpPacketClassifier"
DocsisTlvs["23"]["subTlvs"]["9"]["hex"] = "9"
DocsisTlvs["23"]["subTlvs"]["9"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["1"] = {}
DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["1"]["description"] = "IpTos"
DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["2"] = {}
DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["2"]["description"] = "IpProto"
DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["2"]["datatype"] = "(encode_ushort)"
DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["3"] = {}
DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["3"]["description"] = "IpSrcAddr"
DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["3"]["datatype"] = "(encode_ip)"
DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["4"] = {}
DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["4"]["description"] = "IpSrcMask"
DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["4"]["datatype"] = "(encode_ip)"
DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["5"] = {}
DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["5"]["description"] = "IpDstAddr"
DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["5"]["datatype"] = "(encode_ip)"
DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["6"] = {}
DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["6"]["description"] = "IpDstMask"
DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["6"]["datatype"] = "(encode_ip)"
DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["7"] = {}
DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["7"]["description"] = "SrcPortStart"
DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["7"]["datatype"] = "(encode_ushort)"
DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["8"] = {}
DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["8"]["description"] = "SrcPortEnd"
DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["8"]["datatype"] = "(encode_ushort)"
DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["9"] = {}
DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["9"]["description"] = "DstPortStart"
DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["9"]["hex"] = "9"
DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["9"]["datatype"] = "(encode_ushort)"
DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["9"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["10"] = {}
DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["10"]["description"] = "DstPortEnd"
DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["10"]["hex"] = "a"
DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["10"]["datatype"] = "(encode_ushort)"
DocsisTlvs["23"]["subTlvs"]["9"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["10"] = {}
DocsisTlvs["23"]["subTlvs"]["10"]["description"] = "LLCPacketClassifier"
DocsisTlvs["23"]["subTlvs"]["10"]["hex"] = "a"
DocsisTlvs["23"]["subTlvs"]["10"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["23"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["10"]["subTlvs"]["1"] = {}
DocsisTlvs["23"]["subTlvs"]["10"]["subTlvs"]["1"]["description"] = "DstMacAddress"
DocsisTlvs["23"]["subTlvs"]["10"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["23"]["subTlvs"]["10"]["subTlvs"]["1"]["datatype"] = "(encode_ethermask)"
DocsisTlvs["23"]["subTlvs"]["10"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["10"]["subTlvs"]["2"] = {}
DocsisTlvs["23"]["subTlvs"]["10"]["subTlvs"]["2"]["description"] = "SrcMacAddress"
DocsisTlvs["23"]["subTlvs"]["10"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["23"]["subTlvs"]["10"]["subTlvs"]["2"]["datatype"] = "(encode_ether)"
DocsisTlvs["23"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["10"]["subTlvs"]["3"] = {}
DocsisTlvs["23"]["subTlvs"]["10"]["subTlvs"]["3"]["description"] = "EtherType"
DocsisTlvs["23"]["subTlvs"]["10"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["23"]["subTlvs"]["10"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["10"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["11"] = {}
DocsisTlvs["23"]["subTlvs"]["11"]["description"] = "IEEE802Classifier"
DocsisTlvs["23"]["subTlvs"]["11"]["hex"] = "b"
DocsisTlvs["23"]["subTlvs"]["11"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["23"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["11"]["subTlvs"]["1"] = {}
DocsisTlvs["23"]["subTlvs"]["11"]["subTlvs"]["1"]["description"] = "UserPriority"
DocsisTlvs["23"]["subTlvs"]["11"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["23"]["subTlvs"]["11"]["subTlvs"]["1"]["datatype"] = "(encode_char_list)"
DocsisTlvs["23"]["subTlvs"]["11"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["11"]["subTlvs"]["2"] = {}
DocsisTlvs["23"]["subTlvs"]["11"]["subTlvs"]["2"]["description"] = "VlanID"
DocsisTlvs["23"]["subTlvs"]["11"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["23"]["subTlvs"]["11"]["subTlvs"]["2"]["datatype"] = "(encode_ushort)"
DocsisTlvs["23"]["subTlvs"]["11"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["12"] = {}
DocsisTlvs["23"]["subTlvs"]["12"]["description"] = "PcIPv6PacketClassification"
DocsisTlvs["23"]["subTlvs"]["12"]["hex"] = "c"
DocsisTlvs["23"]["subTlvs"]["12"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["1"] = {}
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["1"]["description"] = "PcIPv6TrafficClassRangeAndMask"
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["2"] = {}
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["2"]["description"] = "PcIPv6FlowLabel"
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["3"] = {}
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["3"]["description"] = "PcIPv6NextHeaderType"
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["3"]["datatype"] = "(encode_ushort)"
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["4"] = {}
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["4"]["description"] = "PcIPv6SourceAddress"
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["4"]["datatype"] = "(encode_ip6)"
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["5"] = {}
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["5"]["description"] = "PcIPv6SourcePrefixLength"
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["5"]["datatype"] = "(encode_uchar)"
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["6"] = {}
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["6"]["description"] = "PcIPv6DestAddress"
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["6"]["datatype"] = "(encode_ip6)"
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["7"] = {}
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["7"]["description"] = "PcIPv6DestPrefixLength"
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["7"]["datatype"] = "(encode_uchar)"
DocsisTlvs["23"]["subTlvs"]["12"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["13"] = {}
DocsisTlvs["23"]["subTlvs"]["13"]["description"] = "PcCMIMEncoding"
DocsisTlvs["23"]["subTlvs"]["13"]["hex"] = "d"
DocsisTlvs["23"]["subTlvs"]["13"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["13"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["14"] = {}
DocsisTlvs["23"]["subTlvs"]["14"]["description"] = "STagCTagFrameClassification"
DocsisTlvs["23"]["subTlvs"]["14"]["hex"] = "e"
DocsisTlvs["23"]["subTlvs"]["14"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["1"] = {}
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["1"]["description"] = "STPID"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["2"] = {}
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["2"]["description"] = "SVID"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["3"] = {}
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["3"]["description"] = "SPCP"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["4"] = {}
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["4"]["description"] = "SDEI"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["5"] = {}
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["5"]["description"] = "CTPID"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["5"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["6"] = {}
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["6"]["description"] = "CVID"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["6"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["7"] = {}
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["7"]["description"] = "CPCP"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["7"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["8"] = {}
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["8"]["description"] = "CCFI"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["8"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["9"] = {}
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["9"]["description"] = "STCI"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["9"]["hex"] = "9"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["9"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["9"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["10"] = {}
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["10"]["description"] = "CTCI"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["10"]["hex"] = "a"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["10"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["14"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["15"] = {}
DocsisTlvs["23"]["subTlvs"]["15"]["description"] = "IEEE8021ahPacketClassification"
DocsisTlvs["23"]["subTlvs"]["15"]["hex"] = "f"
DocsisTlvs["23"]["subTlvs"]["15"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["1"] = {}
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["1"]["description"] = "ITPID"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["2"] = {}
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["2"]["description"] = "ISID"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["3"] = {}
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["3"]["description"] = "ITCI"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["4"] = {}
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["4"]["description"] = "IPCP"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["5"] = {}
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["5"]["description"] = "IDEI"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["5"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["6"] = {}
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["6"]["description"] = "IUCA"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["6"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["7"] = {}
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["7"]["description"] = "BTPID"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["7"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["8"] = {}
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["8"]["description"] = "BTCI"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["8"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["9"] = {}
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["9"]["description"] = "BPCP"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["9"]["hex"] = "9"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["9"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["9"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["10"] = {}
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["10"]["description"] = "BDEI"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["10"]["hex"] = "a"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["10"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["11"] = {}
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["11"]["description"] = "BVID"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["11"]["hex"] = "b"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["11"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["12"] = {}
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["12"]["description"] = "BDA"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["12"]["hex"] = "c"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["12"]["datatype"] = "(encode_ether)"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["13"] = {}
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["13"]["description"] = "BSA"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["13"]["hex"] = "d"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["13"]["datatype"] = "(encode_ether)"
DocsisTlvs["23"]["subTlvs"]["15"]["subTlvs"]["13"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["16"] = {}
DocsisTlvs["23"]["subTlvs"]["16"]["description"] = "ICMPv4ICMPv6PacketClassification"
DocsisTlvs["23"]["subTlvs"]["16"]["hex"] = "10"
DocsisTlvs["23"]["subTlvs"]["16"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["23"]["subTlvs"]["16"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["16"]["subTlvs"]["1"] = {}
DocsisTlvs["23"]["subTlvs"]["16"]["subTlvs"]["1"]["description"] = "ICMPv4ICMPv6TypeStart"
DocsisTlvs["23"]["subTlvs"]["16"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["23"]["subTlvs"]["16"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["23"]["subTlvs"]["16"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["16"]["subTlvs"]["2"] = {}
DocsisTlvs["23"]["subTlvs"]["16"]["subTlvs"]["2"]["description"] = "ICMPv4ICMPv6TypeEnd"
DocsisTlvs["23"]["subTlvs"]["16"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["23"]["subTlvs"]["16"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["23"]["subTlvs"]["16"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["17"] = {}
DocsisTlvs["23"]["subTlvs"]["17"]["description"] = "MPLSClassificationEncoding"
DocsisTlvs["23"]["subTlvs"]["17"]["hex"] = "11"
DocsisTlvs["23"]["subTlvs"]["17"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["23"]["subTlvs"]["17"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["17"]["subTlvs"]["1"] = {}
DocsisTlvs["23"]["subTlvs"]["17"]["subTlvs"]["1"]["description"] = "MPLSTCbits"
DocsisTlvs["23"]["subTlvs"]["17"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["23"]["subTlvs"]["17"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["17"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["17"]["subTlvs"]["2"] = {}
DocsisTlvs["23"]["subTlvs"]["17"]["subTlvs"]["2"]["description"] = "MPLSLabel"
DocsisTlvs["23"]["subTlvs"]["17"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["23"]["subTlvs"]["17"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["17"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["description"] = "VendorSpecific"
DocsisTlvs["23"]["subTlvs"]["43"]["hex"] = "2b"
DocsisTlvs["23"]["subTlvs"]["43"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["1"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["1"]["description"] = "CMLoadBalancingPolicyID"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["1"]["datatype"] = "(encode_uint)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["2"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["2"]["description"] = "CMLoadBalancingPriority"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["2"]["datatype"] = "(encode_uint)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["3"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["3"]["description"] = "CMLoadBalancingGroupID"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["3"]["datatype"] = "(encode_uint)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["4"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["4"]["description"] = "CMRangingClassIDExtension"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["4"]["datatype"] = "(encode_ushort)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["description"] = "L2VPNEncoding"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["1"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["1"]["description"] = "VPNIdentifier"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["description"] = "NSIEncapsulation"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["1"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["1"]["description"] = "ServiceMultiplexingValueOther"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["1"]["datatype"] = "(encode_lenzero)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["2"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["2"]["description"] = "NSIEncapsulationSingleQTag"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["2"]["datatype"] = "(encode_ushort)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["3"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["3"]["description"] = "NSIEncapsulationDualQTag"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["3"]["datatype"] = "(encode_dual_qtag)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["description"] = "ServiceMultiplexingValueMPLSPW"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["1"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["1"]["description"] = "MPLSPseudowireID"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["1"]["datatype"] = "(encode_uint)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["2"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["2"]["description"] = "MPLSPeerIpAddress"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["2"]["datatype"] = "(encode_char_ip_ip6)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["3"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["3"]["description"] = "MPLSPseudowireType"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["3"]["datatype"] = "(encode_uchar)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["4"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["4"]["description"] = "MPLSBackupPseudowireID"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["4"]["datatype"] = "(encode_uint)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["5"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["5"]["description"] = "MPLSBackupPeerIpAddress"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["5"]["datatype"] = "(encode_char_ip_ip6)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["5"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["5"]["description"] = "ServiceMultiplexingValueL2TPv3Peer"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["5"]["datatype"] = "(encode_char_ip_ip6)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["description"] = "IEEE8021ahEncapsulation"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["1"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["1"]["description"] = "ITCIEncapsulation"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["2"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["2"]["description"] = "BDAEncapsulation"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["3"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["3"]["description"] = "BTCIEncapsulation"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["4"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["4"]["description"] = "ITPIDEncapsulation"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["5"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["5"]["description"] = "IPCPEncapsulation"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["5"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["6"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["6"]["description"] = "IDEIEncapsulation"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["6"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["7"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["7"]["description"] = "IUCAEncapsulation"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["7"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["8"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["8"]["description"] = "ISIDEncapsulation"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["8"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["9"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["9"]["description"] = "BTPIDEncapsulation"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["9"]["hex"] = "9"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["9"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["9"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["10"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["10"]["description"] = "BPCPEncapsulation"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["10"]["hex"] = "a"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["10"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["11"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["11"]["description"] = "BDEIEncapsulation"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["11"]["hex"] = "b"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["11"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["12"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["12"]["description"] = "BVIDEncapsulation"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["12"]["hex"] = "c"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["12"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["8"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["8"]["description"] = "ServiceMultiplexingValueIEEE8021adSTPID"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["8"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["3"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["3"]["description"] = "eSAFEDHCPSnooping"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["4"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["4"]["description"] = "CMInterfaceMaskCMIMSubtype"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["5"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["5"]["description"] = "AttachmentGroupID"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["5"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["6"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["6"]["description"] = "SourceAttachmentIndividualID"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["6"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["7"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["7"]["description"] = "TargetAttachmentIndividualID"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["7"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["8"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["8"]["description"] = "IngressUserPriority"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["8"]["datatype"] = "(encode_uchar)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["9"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["9"]["description"] = "UserPriorityRange"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["9"]["hex"] = "9"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["9"]["datatype"] = "(encode_char_list)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["9"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["10"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["10"]["description"] = "L2VPNSADescriptorSubtype"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["10"]["hex"] = "a"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["10"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["12"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["12"]["description"] = "PseudowireType"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["12"]["hex"] = "c"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["12"]["datatype"] = "(encode_uchar)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["13"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["13"]["description"] = "L2VPNMode"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["13"]["hex"] = "d"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["13"]["datatype"] = "(encode_uchar)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["13"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["description"] = "TPIDTranslation"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["hex"] = "e"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["1"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["1"]["description"] = "UpstreamTPIDTranslation"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["2"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["2"]["description"] = "DownstreamTPIDTranslation"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["3"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["3"]["description"] = "UpstreamSTPIDTranslation"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["4"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["4"]["description"] = "DownstreamSTPIDTranslation"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["5"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["5"]["description"] = "UpstreamBTPIDTranslation"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["5"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["6"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["6"]["description"] = "DownstreamBTPIDTranslation"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["6"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["7"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["7"]["description"] = "UpstreamITPIDTranslation"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["7"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["8"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["8"]["description"] = "DownstreamITPIDTranslation"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["8"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["description"] = "L2CPProcessing"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["hex"] = "f"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["1"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["1"]["description"] = "L2CPTunnelMode"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["2"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["2"]["description"] = "L2CPDMACAddress"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["2"]["datatype"] = "(encode_ether)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["3"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["3"]["description"] = "L2CPOverwrotingDMACAddress"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["3"]["datatype"] = "(encode_ether)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["16"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["16"]["description"] = "DACDisableEnableConfiguration"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["16"]["hex"] = "10"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["16"]["datatype"] = "(encode_uchar)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["16"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["18"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["18"]["description"] = "PseudowireClass"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["18"]["hex"] = "12"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["18"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["18"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["description"] = "ServiceDelimiter"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["hex"] = "13"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["1"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["1"]["description"] = "CVIDDelimiter"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["2"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["2"]["description"] = "SVIDDelimiter"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["3"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["3"]["description"] = "ISIDDelimiter"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["4"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["4"]["description"] = "BVIDDelimiter"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["description"] = "VirtualSwitchInstanceEncoding"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["hex"] = "14"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["1"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["1"]["description"] = "VPLSClass"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["2"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["2"]["description"] = "ETreeRole"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["3"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["3"]["description"] = "ETreeRootVID"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["4"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["4"]["description"] = "ETreeLeafVID"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["description"] = "BGPAttribute"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["hex"] = "15"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["1"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["1"]["description"] = "BGPVPNID"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["1"]["datatype"] = "(encode_uint)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["2"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["2"]["description"] = "RouteDistinguisher"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["3"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["3"]["description"] = "RouteTargetImport"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["4"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["4"]["description"] = "RouteTargetExport"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["5"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["5"]["description"] = "CEIDVEID"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["5"]["datatype"] = "(encode_ushort)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["23"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["23"]["description"] = "PseudowireSignaling"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["23"]["hex"] = "17"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["23"]["datatype"] = "(encode_uchar)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["23"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["description"] = "SOAMSubtype"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["hex"] = "18"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["description"] = "MEPConfiguration"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["1"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["1"]["description"] = "MDLevel"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["2"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["2"]["description"] = "MDName"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["2"]["datatype"] = "(encode_string)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["3"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["3"]["description"] = "MAName"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["3"]["datatype"] = "(encode_string)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["4"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["4"]["description"] = "MEPID"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["4"]["datatype"] = "(encode_ushort)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["description"] = "RemoteMEPConfiguration"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["1"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["1"]["description"] = "RemoteMDLevel"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["2"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["2"]["description"] = "RemoteMDName"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["2"]["datatype"] = "(encode_string)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["3"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["3"]["description"] = "RemoteMAName"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["3"]["datatype"] = "(encode_string)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["4"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["4"]["description"] = "RemoteMEPID"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["4"]["datatype"] = "(encode_ushort)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["description"] = "FaultManagementConfiguration"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["1"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["1"]["description"] = "ContinuityCheckMessages"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["2"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["2"]["description"] = "LoopbackFunction"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["3"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["3"]["description"] = "LinktraceFunction"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["3"]["datatype"] = "(encode_uchar)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["description"] = "PerformanceManagementConfiguration"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["description"] = "FrameDelayMeasurement"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["1"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["1"]["description"] = "FrameDelayMeasurementEnable"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["2"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["2"]["description"] = "FrameDelayMeasurementOneWayTwoWay"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["3"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["3"]["description"] = "FrameDelayMeasurementTransmissionPeriodicity"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["3"]["datatype"] = "(encode_ushort)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["description"] = "FrameLossMeasurement"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["1"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["1"]["description"] = "FrameLossMeasurementEnable"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["2"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["2"]["description"] = "FrameLossMeasurementTransmissionPeriodicity"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["26"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["26"]["description"] = "L2VPNDSID"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["26"]["hex"] = "1a"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["26"]["datatype"] = "(encode_uint24)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["26"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["description"] = "VendorSpecificL2VPNSubtype"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["hex"] = "2b"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["subTlvs"]["8"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["subTlvs"]["8"]["description"] = "VendorIdentifier"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["subTlvs"]["8"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["6"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["6"]["description"] = "ExtendedCMTSMICConfigurationSetting"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["6"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["1"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["1"]["description"] = "ExtendedCMTSMICHMACtype"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["2"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["2"]["description"] = "ExtendedCMTSMICBitmap"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["3"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["3"]["description"] = "ExplicitExtendedCMTSMICDigest"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["7"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["7"]["description"] = "SAVAuthorizationEncoding"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["7"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["1"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["1"]["description"] = "SAVGroupName"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["1"]["datatype"] = "(encode_string)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["description"] = "SAVStaticPrefixRule"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["1"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["1"]["description"] = "SAVStaticPrefixAddress"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["1"]["datatype"] = "(encode_ip_ip6)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["2"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["2"]["description"] = "SAVStaticPrefixLength"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["8"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["8"]["description"] = "VendorIdentifier"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["8"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["9"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["9"]["description"] = "CMAttributeMasks"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["9"]["hex"] = "9"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["9"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["1"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["1"]["description"] = "CMDownstreamRequiredAttributeMask"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["2"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["2"]["description"] = "CMDownstreamForbiddenAttributeMask"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["3"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["3"]["description"] = "CMUpstreamRequiredAttributeMask"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["4"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["4"]["description"] = "CMUpstreamForbiddenAttributeMask"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["description"] = "IPMulticastJoinAuthorization"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["hex"] = "a"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["1"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["1"]["description"] = "IPMulticastProfileName"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["1"]["datatype"] = "(encode_string)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["description"] = "IPMulticastJoinAuthStaticSessionRule"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["1"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["1"]["description"] = "MulticastRulePriority"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["2"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["2"]["description"] = "AuthorizationAction"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["3"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["3"]["description"] = "SourcePrefixAddress"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["3"]["datatype"] = "(encode_ip_ip6)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["4"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["4"]["description"] = "SourcePrefixLength"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["4"]["datatype"] = "(encode_uchar)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["5"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["5"]["description"] = "GroupPrefixAddress"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["5"]["datatype"] = "(encode_ip_ip6)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["6"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["6"]["description"] = "GroupPrefixLength"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["6"]["datatype"] = "(encode_uchar)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["3"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["3"]["description"] = "MaximumMulticastSessions"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["3"]["datatype"] = "(encode_ushort)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["11"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["11"]["description"] = "ServiceTypeIdentifier"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["11"]["hex"] = "b"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["11"]["datatype"] = "(encode_string)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"]["description"] = "DEMARCAutoConfiguration"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"]["hex"] = "c"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["1"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["1"]["description"] = "DACDisableEnableConfig"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["2"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["2"]["description"] = "CMIMEncoding"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["3"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["3"]["description"] = "UpstreamServiceClassName"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["3"]["datatype"] = "(encode_strzero)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["4"] = {}
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["4"]["description"] = "DownstreamServiceClassName"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["4"]["datatype"] = "(encode_strzero)"
DocsisTlvs["23"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["24"] = {}
DocsisTlvs["24"]["description"] = "UsServiceFlow"
DocsisTlvs["24"]["hex"] = "18"
DocsisTlvs["24"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["24"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["1"] = {}
DocsisTlvs["24"]["subTlvs"]["1"]["description"] = "UsServiceFlowRef"
DocsisTlvs["24"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["24"]["subTlvs"]["1"]["datatype"] = "(encode_ushort)"
DocsisTlvs["24"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["2"] = {}
DocsisTlvs["24"]["subTlvs"]["2"]["description"] = "UsServiceFlowId"
DocsisTlvs["24"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["24"]["subTlvs"]["2"]["datatype"] = "(encode_uint)"
DocsisTlvs["24"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["3"] = {}
DocsisTlvs["24"]["subTlvs"]["3"]["description"] = "ServiceIdentifier"
DocsisTlvs["24"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["24"]["subTlvs"]["3"]["datatype"] = "(encode_ushort)"
DocsisTlvs["24"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["4"] = {}
DocsisTlvs["24"]["subTlvs"]["4"]["description"] = "ServiceClassName"
DocsisTlvs["24"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["24"]["subTlvs"]["4"]["datatype"] = "(encode_strzero)"
DocsisTlvs["24"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["6"] = {}
DocsisTlvs["24"]["subTlvs"]["6"]["description"] = "QosParamSetType"
DocsisTlvs["24"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["24"]["subTlvs"]["6"]["datatype"] = "(encode_uchar)"
DocsisTlvs["24"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["7"] = {}
DocsisTlvs["24"]["subTlvs"]["7"]["description"] = "TrafficPriority"
DocsisTlvs["24"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["24"]["subTlvs"]["7"]["datatype"] = "(encode_uchar)"
DocsisTlvs["24"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["8"] = {}
DocsisTlvs["24"]["subTlvs"]["8"]["description"] = "MaxRateSustained"
DocsisTlvs["24"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["24"]["subTlvs"]["8"]["datatype"] = "(encode_uint)"
DocsisTlvs["24"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["9"] = {}
DocsisTlvs["24"]["subTlvs"]["9"]["description"] = "MaxTrafficBurst"
DocsisTlvs["24"]["subTlvs"]["9"]["hex"] = "9"
DocsisTlvs["24"]["subTlvs"]["9"]["datatype"] = "(encode_uint)"
DocsisTlvs["24"]["subTlvs"]["9"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["10"] = {}
DocsisTlvs["24"]["subTlvs"]["10"]["description"] = "MinReservedRate"
DocsisTlvs["24"]["subTlvs"]["10"]["hex"] = "a"
DocsisTlvs["24"]["subTlvs"]["10"]["datatype"] = "(encode_uint)"
DocsisTlvs["24"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["11"] = {}
DocsisTlvs["24"]["subTlvs"]["11"]["description"] = "MinResPacketSize"
DocsisTlvs["24"]["subTlvs"]["11"]["hex"] = "b"
DocsisTlvs["24"]["subTlvs"]["11"]["datatype"] = "(encode_ushort)"
DocsisTlvs["24"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["12"] = {}
DocsisTlvs["24"]["subTlvs"]["12"]["description"] = "ActQosParamsTimeout"
DocsisTlvs["24"]["subTlvs"]["12"]["hex"] = "c"
DocsisTlvs["24"]["subTlvs"]["12"]["datatype"] = "(encode_ushort)"
DocsisTlvs["24"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["13"] = {}
DocsisTlvs["24"]["subTlvs"]["13"]["description"] = "AdmQosParamsTimeout"
DocsisTlvs["24"]["subTlvs"]["13"]["hex"] = "d"
DocsisTlvs["24"]["subTlvs"]["13"]["datatype"] = "(encode_ushort)"
DocsisTlvs["24"]["subTlvs"]["13"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["14"] = {}
DocsisTlvs["24"]["subTlvs"]["14"]["description"] = "MaxConcatenatedBurst"
DocsisTlvs["24"]["subTlvs"]["14"]["hex"] = "e"
DocsisTlvs["24"]["subTlvs"]["14"]["datatype"] = "(encode_ushort)"
DocsisTlvs["24"]["subTlvs"]["14"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["15"] = {}
DocsisTlvs["24"]["subTlvs"]["15"]["description"] = "SchedulingType"
DocsisTlvs["24"]["subTlvs"]["15"]["hex"] = "f"
DocsisTlvs["24"]["subTlvs"]["15"]["datatype"] = "(encode_uchar)"
DocsisTlvs["24"]["subTlvs"]["15"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["16"] = {}
DocsisTlvs["24"]["subTlvs"]["16"]["description"] = "RequestOrTxPolicy"
DocsisTlvs["24"]["subTlvs"]["16"]["hex"] = "10"
DocsisTlvs["24"]["subTlvs"]["16"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["16"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["17"] = {}
DocsisTlvs["24"]["subTlvs"]["17"]["description"] = "NominalPollInterval"
DocsisTlvs["24"]["subTlvs"]["17"]["hex"] = "11"
DocsisTlvs["24"]["subTlvs"]["17"]["datatype"] = "(encode_uint)"
DocsisTlvs["24"]["subTlvs"]["17"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["18"] = {}
DocsisTlvs["24"]["subTlvs"]["18"]["description"] = "ToleratedPollJitter"
DocsisTlvs["24"]["subTlvs"]["18"]["hex"] = "12"
DocsisTlvs["24"]["subTlvs"]["18"]["datatype"] = "(encode_uint)"
DocsisTlvs["24"]["subTlvs"]["18"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["19"] = {}
DocsisTlvs["24"]["subTlvs"]["19"]["description"] = "UnsolicitedGrantSize"
DocsisTlvs["24"]["subTlvs"]["19"]["hex"] = "13"
DocsisTlvs["24"]["subTlvs"]["19"]["datatype"] = "(encode_ushort)"
DocsisTlvs["24"]["subTlvs"]["19"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["20"] = {}
DocsisTlvs["24"]["subTlvs"]["20"]["description"] = "NominalGrantInterval"
DocsisTlvs["24"]["subTlvs"]["20"]["hex"] = "14"
DocsisTlvs["24"]["subTlvs"]["20"]["datatype"] = "(encode_uint)"
DocsisTlvs["24"]["subTlvs"]["20"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["21"] = {}
DocsisTlvs["24"]["subTlvs"]["21"]["description"] = "ToleratedGrantJitter"
DocsisTlvs["24"]["subTlvs"]["21"]["hex"] = "15"
DocsisTlvs["24"]["subTlvs"]["21"]["datatype"] = "(encode_uint)"
DocsisTlvs["24"]["subTlvs"]["21"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["22"] = {}
DocsisTlvs["24"]["subTlvs"]["22"]["description"] = "GrantsPerInterval"
DocsisTlvs["24"]["subTlvs"]["22"]["hex"] = "16"
DocsisTlvs["24"]["subTlvs"]["22"]["datatype"] = "(encode_uchar)"
DocsisTlvs["24"]["subTlvs"]["22"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["23"] = {}
DocsisTlvs["24"]["subTlvs"]["23"]["description"] = "IpTosOverwrite"
DocsisTlvs["24"]["subTlvs"]["23"]["hex"] = "17"
DocsisTlvs["24"]["subTlvs"]["23"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["23"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["26"] = {}
DocsisTlvs["24"]["subTlvs"]["26"]["description"] = "MultipliertoNumberofBytesRequested"
DocsisTlvs["24"]["subTlvs"]["26"]["hex"] = "1a"
DocsisTlvs["24"]["subTlvs"]["26"]["datatype"] = "(encode_uchar)"
DocsisTlvs["24"]["subTlvs"]["26"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["27"] = {}
DocsisTlvs["24"]["subTlvs"]["27"]["description"] = "UpstreamPeakTrafficRate"
DocsisTlvs["24"]["subTlvs"]["27"]["hex"] = "1b"
DocsisTlvs["24"]["subTlvs"]["27"]["datatype"] = "(encode_uint)"
DocsisTlvs["24"]["subTlvs"]["27"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["31"] = {}
DocsisTlvs["24"]["subTlvs"]["31"]["description"] = "ServiceFlowRequiredAttributeMask"
DocsisTlvs["24"]["subTlvs"]["31"]["hex"] = "1f"
DocsisTlvs["24"]["subTlvs"]["31"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["31"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["32"] = {}
DocsisTlvs["24"]["subTlvs"]["32"]["description"] = "ServiceFlowForbiddenAttributeMask"
DocsisTlvs["24"]["subTlvs"]["32"]["hex"] = "20"
DocsisTlvs["24"]["subTlvs"]["32"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["32"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["33"] = {}
DocsisTlvs["24"]["subTlvs"]["33"]["description"] = "ServiceFlowAttributeAggregationRuleMask"
DocsisTlvs["24"]["subTlvs"]["33"]["hex"] = "21"
DocsisTlvs["24"]["subTlvs"]["33"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["33"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["34"] = {}
DocsisTlvs["24"]["subTlvs"]["34"]["description"] = "ApplicationIdentifier"
DocsisTlvs["24"]["subTlvs"]["34"]["hex"] = "22"
DocsisTlvs["24"]["subTlvs"]["34"]["datatype"] = "(encode_uint)"
DocsisTlvs["24"]["subTlvs"]["34"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["35"] = {}
DocsisTlvs["24"]["subTlvs"]["35"]["description"] = "BufferControl"
DocsisTlvs["24"]["subTlvs"]["35"]["hex"] = "23"
DocsisTlvs["24"]["subTlvs"]["35"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["24"]["subTlvs"]["35"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["35"]["subTlvs"]["1"] = {}
DocsisTlvs["24"]["subTlvs"]["35"]["subTlvs"]["1"]["description"] = "MinimumBuffer"
DocsisTlvs["24"]["subTlvs"]["35"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["24"]["subTlvs"]["35"]["subTlvs"]["1"]["datatype"] = "(encode_uint)"
DocsisTlvs["24"]["subTlvs"]["35"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["35"]["subTlvs"]["2"] = {}
DocsisTlvs["24"]["subTlvs"]["35"]["subTlvs"]["2"]["description"] = "TargetBuffer"
DocsisTlvs["24"]["subTlvs"]["35"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["24"]["subTlvs"]["35"]["subTlvs"]["2"]["datatype"] = "(encode_uint)"
DocsisTlvs["24"]["subTlvs"]["35"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["35"]["subTlvs"]["3"] = {}
DocsisTlvs["24"]["subTlvs"]["35"]["subTlvs"]["3"]["description"] = "MaximumBuffer"
DocsisTlvs["24"]["subTlvs"]["35"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["24"]["subTlvs"]["35"]["subTlvs"]["3"]["datatype"] = "(encode_uint)"
DocsisTlvs["24"]["subTlvs"]["35"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["36"] = {}
DocsisTlvs["24"]["subTlvs"]["36"]["description"] = "UpstreamAggregateServiceFlowReference"
DocsisTlvs["24"]["subTlvs"]["36"]["hex"] = "24"
DocsisTlvs["24"]["subTlvs"]["36"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["24"]["subTlvs"]["36"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["37"] = {}
DocsisTlvs["24"]["subTlvs"]["37"]["description"] = "UpstreamMESPReference"
DocsisTlvs["24"]["subTlvs"]["37"]["hex"] = "25"
DocsisTlvs["24"]["subTlvs"]["37"]["datatype"] = "(encode_ushort)"
DocsisTlvs["24"]["subTlvs"]["37"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["40"] = {}
DocsisTlvs["24"]["subTlvs"]["40"]["description"] = "AQMEncodings"
DocsisTlvs["24"]["subTlvs"]["40"]["hex"] = "28"
DocsisTlvs["24"]["subTlvs"]["40"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["24"]["subTlvs"]["40"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["40"]["subTlvs"]["1"] = {}
DocsisTlvs["24"]["subTlvs"]["40"]["subTlvs"]["1"]["description"] = "SFAQMDisable"
DocsisTlvs["24"]["subTlvs"]["40"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["24"]["subTlvs"]["40"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["24"]["subTlvs"]["40"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["40"]["subTlvs"]["2"] = {}
DocsisTlvs["24"]["subTlvs"]["40"]["subTlvs"]["2"]["description"] = "SFAQMLatencyTarget"
DocsisTlvs["24"]["subTlvs"]["40"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["24"]["subTlvs"]["40"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["24"]["subTlvs"]["40"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["41"] = {}
DocsisTlvs["24"]["subTlvs"]["41"]["description"] = "DataRateUnitSetting"
DocsisTlvs["24"]["subTlvs"]["41"]["hex"] = "29"
DocsisTlvs["24"]["subTlvs"]["41"]["datatype"] = "(encode_uchar)"
DocsisTlvs["24"]["subTlvs"]["41"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["description"] = "VendorSpecific"
DocsisTlvs["24"]["subTlvs"]["43"]["hex"] = "2b"
DocsisTlvs["24"]["subTlvs"]["43"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["1"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["1"]["description"] = "CMLoadBalancingPolicyID"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["1"]["datatype"] = "(encode_uint)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["2"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["2"]["description"] = "CMLoadBalancingPriority"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["2"]["datatype"] = "(encode_uint)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["3"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["3"]["description"] = "CMLoadBalancingGroupID"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["3"]["datatype"] = "(encode_uint)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["4"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["4"]["description"] = "CMRangingClassIDExtension"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["4"]["datatype"] = "(encode_ushort)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["description"] = "L2VPNEncoding"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["1"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["1"]["description"] = "VPNIdentifier"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["description"] = "NSIEncapsulation"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["1"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["1"]["description"] = "ServiceMultiplexingValueOther"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["1"]["datatype"] = "(encode_lenzero)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["2"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["2"]["description"] = "NSIEncapsulationSingleQTag"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["2"]["datatype"] = "(encode_ushort)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["3"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["3"]["description"] = "NSIEncapsulationDualQTag"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["3"]["datatype"] = "(encode_dual_qtag)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["description"] = "ServiceMultiplexingValueMPLSPW"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["1"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["1"]["description"] = "MPLSPseudowireID"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["1"]["datatype"] = "(encode_uint)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["2"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["2"]["description"] = "MPLSPeerIpAddress"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["2"]["datatype"] = "(encode_char_ip_ip6)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["3"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["3"]["description"] = "MPLSPseudowireType"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["3"]["datatype"] = "(encode_uchar)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["4"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["4"]["description"] = "MPLSBackupPseudowireID"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["4"]["datatype"] = "(encode_uint)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["5"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["5"]["description"] = "MPLSBackupPeerIpAddress"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["5"]["datatype"] = "(encode_char_ip_ip6)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["5"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["5"]["description"] = "ServiceMultiplexingValueL2TPv3Peer"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["5"]["datatype"] = "(encode_char_ip_ip6)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["description"] = "IEEE8021ahEncapsulation"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["1"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["1"]["description"] = "ITCIEncapsulation"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["2"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["2"]["description"] = "BDAEncapsulation"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["3"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["3"]["description"] = "BTCIEncapsulation"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["4"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["4"]["description"] = "ITPIDEncapsulation"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["5"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["5"]["description"] = "IPCPEncapsulation"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["5"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["6"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["6"]["description"] = "IDEIEncapsulation"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["6"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["7"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["7"]["description"] = "IUCAEncapsulation"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["7"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["8"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["8"]["description"] = "ISIDEncapsulation"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["8"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["9"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["9"]["description"] = "BTPIDEncapsulation"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["9"]["hex"] = "9"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["9"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["9"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["10"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["10"]["description"] = "BPCPEncapsulation"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["10"]["hex"] = "a"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["10"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["11"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["11"]["description"] = "BDEIEncapsulation"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["11"]["hex"] = "b"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["11"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["12"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["12"]["description"] = "BVIDEncapsulation"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["12"]["hex"] = "c"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["12"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["8"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["8"]["description"] = "ServiceMultiplexingValueIEEE8021adSTPID"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["8"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["3"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["3"]["description"] = "eSAFEDHCPSnooping"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["4"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["4"]["description"] = "CMInterfaceMaskCMIMSubtype"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["5"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["5"]["description"] = "AttachmentGroupID"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["5"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["6"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["6"]["description"] = "SourceAttachmentIndividualID"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["6"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["7"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["7"]["description"] = "TargetAttachmentIndividualID"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["7"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["8"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["8"]["description"] = "IngressUserPriority"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["8"]["datatype"] = "(encode_uchar)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["9"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["9"]["description"] = "UserPriorityRange"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["9"]["hex"] = "9"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["9"]["datatype"] = "(encode_char_list)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["9"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["10"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["10"]["description"] = "L2VPNSADescriptorSubtype"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["10"]["hex"] = "a"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["10"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["12"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["12"]["description"] = "PseudowireType"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["12"]["hex"] = "c"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["12"]["datatype"] = "(encode_uchar)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["13"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["13"]["description"] = "L2VPNMode"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["13"]["hex"] = "d"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["13"]["datatype"] = "(encode_uchar)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["13"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["description"] = "TPIDTranslation"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["hex"] = "e"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["1"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["1"]["description"] = "UpstreamTPIDTranslation"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["2"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["2"]["description"] = "DownstreamTPIDTranslation"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["3"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["3"]["description"] = "UpstreamSTPIDTranslation"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["4"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["4"]["description"] = "DownstreamSTPIDTranslation"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["5"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["5"]["description"] = "UpstreamBTPIDTranslation"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["5"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["6"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["6"]["description"] = "DownstreamBTPIDTranslation"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["6"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["7"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["7"]["description"] = "UpstreamITPIDTranslation"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["7"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["8"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["8"]["description"] = "DownstreamITPIDTranslation"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["8"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["description"] = "L2CPProcessing"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["hex"] = "f"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["1"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["1"]["description"] = "L2CPTunnelMode"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["2"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["2"]["description"] = "L2CPDMACAddress"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["2"]["datatype"] = "(encode_ether)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["3"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["3"]["description"] = "L2CPOverwrotingDMACAddress"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["3"]["datatype"] = "(encode_ether)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["16"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["16"]["description"] = "DACDisableEnableConfiguration"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["16"]["hex"] = "10"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["16"]["datatype"] = "(encode_uchar)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["16"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["18"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["18"]["description"] = "PseudowireClass"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["18"]["hex"] = "12"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["18"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["18"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["description"] = "ServiceDelimiter"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["hex"] = "13"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["1"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["1"]["description"] = "CVIDDelimiter"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["2"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["2"]["description"] = "SVIDDelimiter"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["3"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["3"]["description"] = "ISIDDelimiter"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["4"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["4"]["description"] = "BVIDDelimiter"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["description"] = "VirtualSwitchInstanceEncoding"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["hex"] = "14"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["1"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["1"]["description"] = "VPLSClass"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["2"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["2"]["description"] = "ETreeRole"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["3"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["3"]["description"] = "ETreeRootVID"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["4"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["4"]["description"] = "ETreeLeafVID"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["description"] = "BGPAttribute"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["hex"] = "15"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["1"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["1"]["description"] = "BGPVPNID"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["1"]["datatype"] = "(encode_uint)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["2"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["2"]["description"] = "RouteDistinguisher"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["3"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["3"]["description"] = "RouteTargetImport"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["4"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["4"]["description"] = "RouteTargetExport"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["5"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["5"]["description"] = "CEIDVEID"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["5"]["datatype"] = "(encode_ushort)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["23"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["23"]["description"] = "PseudowireSignaling"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["23"]["hex"] = "17"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["23"]["datatype"] = "(encode_uchar)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["23"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["description"] = "SOAMSubtype"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["hex"] = "18"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["description"] = "MEPConfiguration"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["1"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["1"]["description"] = "MDLevel"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["2"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["2"]["description"] = "MDName"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["2"]["datatype"] = "(encode_string)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["3"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["3"]["description"] = "MAName"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["3"]["datatype"] = "(encode_string)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["4"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["4"]["description"] = "MEPID"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["4"]["datatype"] = "(encode_ushort)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["description"] = "RemoteMEPConfiguration"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["1"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["1"]["description"] = "RemoteMDLevel"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["2"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["2"]["description"] = "RemoteMDName"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["2"]["datatype"] = "(encode_string)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["3"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["3"]["description"] = "RemoteMAName"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["3"]["datatype"] = "(encode_string)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["4"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["4"]["description"] = "RemoteMEPID"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["4"]["datatype"] = "(encode_ushort)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["description"] = "FaultManagementConfiguration"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["1"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["1"]["description"] = "ContinuityCheckMessages"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["2"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["2"]["description"] = "LoopbackFunction"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["3"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["3"]["description"] = "LinktraceFunction"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["3"]["datatype"] = "(encode_uchar)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["description"] = "PerformanceManagementConfiguration"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["description"] = "FrameDelayMeasurement"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["1"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["1"]["description"] = "FrameDelayMeasurementEnable"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["2"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["2"]["description"] = "FrameDelayMeasurementOneWayTwoWay"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["3"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["3"]["description"] = "FrameDelayMeasurementTransmissionPeriodicity"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["3"]["datatype"] = "(encode_ushort)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["description"] = "FrameLossMeasurement"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["1"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["1"]["description"] = "FrameLossMeasurementEnable"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["2"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["2"]["description"] = "FrameLossMeasurementTransmissionPeriodicity"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["26"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["26"]["description"] = "L2VPNDSID"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["26"]["hex"] = "1a"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["26"]["datatype"] = "(encode_uint24)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["26"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["description"] = "VendorSpecificL2VPNSubtype"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["hex"] = "2b"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["subTlvs"]["8"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["subTlvs"]["8"]["description"] = "VendorIdentifier"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["subTlvs"]["8"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["6"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["6"]["description"] = "ExtendedCMTSMICConfigurationSetting"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["6"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["1"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["1"]["description"] = "ExtendedCMTSMICHMACtype"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["2"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["2"]["description"] = "ExtendedCMTSMICBitmap"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["3"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["3"]["description"] = "ExplicitExtendedCMTSMICDigest"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["7"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["7"]["description"] = "SAVAuthorizationEncoding"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["7"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["1"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["1"]["description"] = "SAVGroupName"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["1"]["datatype"] = "(encode_string)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["description"] = "SAVStaticPrefixRule"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["1"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["1"]["description"] = "SAVStaticPrefixAddress"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["1"]["datatype"] = "(encode_ip_ip6)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["2"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["2"]["description"] = "SAVStaticPrefixLength"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["8"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["8"]["description"] = "VendorIdentifier"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["8"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["9"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["9"]["description"] = "CMAttributeMasks"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["9"]["hex"] = "9"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["9"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["1"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["1"]["description"] = "CMDownstreamRequiredAttributeMask"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["2"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["2"]["description"] = "CMDownstreamForbiddenAttributeMask"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["3"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["3"]["description"] = "CMUpstreamRequiredAttributeMask"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["4"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["4"]["description"] = "CMUpstreamForbiddenAttributeMask"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["description"] = "IPMulticastJoinAuthorization"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["hex"] = "a"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["1"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["1"]["description"] = "IPMulticastProfileName"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["1"]["datatype"] = "(encode_string)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["description"] = "IPMulticastJoinAuthStaticSessionRule"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["1"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["1"]["description"] = "MulticastRulePriority"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["2"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["2"]["description"] = "AuthorizationAction"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["3"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["3"]["description"] = "SourcePrefixAddress"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["3"]["datatype"] = "(encode_ip_ip6)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["4"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["4"]["description"] = "SourcePrefixLength"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["4"]["datatype"] = "(encode_uchar)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["5"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["5"]["description"] = "GroupPrefixAddress"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["5"]["datatype"] = "(encode_ip_ip6)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["6"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["6"]["description"] = "GroupPrefixLength"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["6"]["datatype"] = "(encode_uchar)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["3"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["3"]["description"] = "MaximumMulticastSessions"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["3"]["datatype"] = "(encode_ushort)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["11"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["11"]["description"] = "ServiceTypeIdentifier"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["11"]["hex"] = "b"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["11"]["datatype"] = "(encode_string)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"]["description"] = "DEMARCAutoConfiguration"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"]["hex"] = "c"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["1"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["1"]["description"] = "DACDisableEnableConfig"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["2"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["2"]["description"] = "CMIMEncoding"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["3"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["3"]["description"] = "UpstreamServiceClassName"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["3"]["datatype"] = "(encode_strzero)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["4"] = {}
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["4"]["description"] = "DownstreamServiceClassName"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["4"]["datatype"] = "(encode_strzero)"
DocsisTlvs["24"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["25"] = {}
DocsisTlvs["25"]["description"] = "DsServiceFlow"
DocsisTlvs["25"]["hex"] = "19"
DocsisTlvs["25"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["25"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["1"] = {}
DocsisTlvs["25"]["subTlvs"]["1"]["description"] = "DsServiceFlowRef"
DocsisTlvs["25"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["25"]["subTlvs"]["1"]["datatype"] = "(encode_ushort)"
DocsisTlvs["25"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["2"] = {}
DocsisTlvs["25"]["subTlvs"]["2"]["description"] = "DsServiceFlowId"
DocsisTlvs["25"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["25"]["subTlvs"]["2"]["datatype"] = "(encode_uint)"
DocsisTlvs["25"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["4"] = {}
DocsisTlvs["25"]["subTlvs"]["4"]["description"] = "ServiceClassName"
DocsisTlvs["25"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["25"]["subTlvs"]["4"]["datatype"] = "(encode_strzero)"
DocsisTlvs["25"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["6"] = {}
DocsisTlvs["25"]["subTlvs"]["6"]["description"] = "QosParamSetType"
DocsisTlvs["25"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["25"]["subTlvs"]["6"]["datatype"] = "(encode_uchar)"
DocsisTlvs["25"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["7"] = {}
DocsisTlvs["25"]["subTlvs"]["7"]["description"] = "TrafficPriority"
DocsisTlvs["25"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["25"]["subTlvs"]["7"]["datatype"] = "(encode_uchar)"
DocsisTlvs["25"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["8"] = {}
DocsisTlvs["25"]["subTlvs"]["8"]["description"] = "MaxRateSustained"
DocsisTlvs["25"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["25"]["subTlvs"]["8"]["datatype"] = "(encode_uint)"
DocsisTlvs["25"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["9"] = {}
DocsisTlvs["25"]["subTlvs"]["9"]["description"] = "MaxTrafficBurst"
DocsisTlvs["25"]["subTlvs"]["9"]["hex"] = "9"
DocsisTlvs["25"]["subTlvs"]["9"]["datatype"] = "(encode_uint)"
DocsisTlvs["25"]["subTlvs"]["9"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["10"] = {}
DocsisTlvs["25"]["subTlvs"]["10"]["description"] = "MinReservedRate"
DocsisTlvs["25"]["subTlvs"]["10"]["hex"] = "a"
DocsisTlvs["25"]["subTlvs"]["10"]["datatype"] = "(encode_uint)"
DocsisTlvs["25"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["11"] = {}
DocsisTlvs["25"]["subTlvs"]["11"]["description"] = "MinResPacketSize"
DocsisTlvs["25"]["subTlvs"]["11"]["hex"] = "b"
DocsisTlvs["25"]["subTlvs"]["11"]["datatype"] = "(encode_ushort)"
DocsisTlvs["25"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["12"] = {}
DocsisTlvs["25"]["subTlvs"]["12"]["description"] = "ActQosParamsTimeout"
DocsisTlvs["25"]["subTlvs"]["12"]["hex"] = "c"
DocsisTlvs["25"]["subTlvs"]["12"]["datatype"] = "(encode_ushort)"
DocsisTlvs["25"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["13"] = {}
DocsisTlvs["25"]["subTlvs"]["13"]["description"] = "AdmQosParamsTimeout"
DocsisTlvs["25"]["subTlvs"]["13"]["hex"] = "d"
DocsisTlvs["25"]["subTlvs"]["13"]["datatype"] = "(encode_ushort)"
DocsisTlvs["25"]["subTlvs"]["13"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["14"] = {}
DocsisTlvs["25"]["subTlvs"]["14"]["description"] = "MaxDsLatency"
DocsisTlvs["25"]["subTlvs"]["14"]["hex"] = "e"
DocsisTlvs["25"]["subTlvs"]["14"]["datatype"] = "(encode_uint)"
DocsisTlvs["25"]["subTlvs"]["14"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["17"] = {}
DocsisTlvs["25"]["subTlvs"]["17"]["description"] = "DsResequencing"
DocsisTlvs["25"]["subTlvs"]["17"]["hex"] = "11"
DocsisTlvs["25"]["subTlvs"]["17"]["datatype"] = "(encode_uchar)"
DocsisTlvs["25"]["subTlvs"]["17"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["23"] = {}
DocsisTlvs["25"]["subTlvs"]["23"]["description"] = "IpTosOverwrite"
DocsisTlvs["25"]["subTlvs"]["23"]["hex"] = "17"
DocsisTlvs["25"]["subTlvs"]["23"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["23"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["27"] = {}
DocsisTlvs["25"]["subTlvs"]["27"]["description"] = "DownstreamPeakTrafficRate"
DocsisTlvs["25"]["subTlvs"]["27"]["hex"] = "1b"
DocsisTlvs["25"]["subTlvs"]["27"]["datatype"] = "(encode_uint)"
DocsisTlvs["25"]["subTlvs"]["27"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["31"] = {}
DocsisTlvs["25"]["subTlvs"]["31"]["description"] = "ServiceFlowRequiredAttributeMask"
DocsisTlvs["25"]["subTlvs"]["31"]["hex"] = "1f"
DocsisTlvs["25"]["subTlvs"]["31"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["31"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["32"] = {}
DocsisTlvs["25"]["subTlvs"]["32"]["description"] = "ServiceFlowForbiddenAttributeMask"
DocsisTlvs["25"]["subTlvs"]["32"]["hex"] = "20"
DocsisTlvs["25"]["subTlvs"]["32"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["32"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["33"] = {}
DocsisTlvs["25"]["subTlvs"]["33"]["description"] = "ServiceFlowAttributeAggregationRuleMask"
DocsisTlvs["25"]["subTlvs"]["33"]["hex"] = "21"
DocsisTlvs["25"]["subTlvs"]["33"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["33"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["34"] = {}
DocsisTlvs["25"]["subTlvs"]["34"]["description"] = "ApplicationIdentifier"
DocsisTlvs["25"]["subTlvs"]["34"]["hex"] = "22"
DocsisTlvs["25"]["subTlvs"]["34"]["datatype"] = "(encode_uint)"
DocsisTlvs["25"]["subTlvs"]["34"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["35"] = {}
DocsisTlvs["25"]["subTlvs"]["35"]["description"] = "BufferControl"
DocsisTlvs["25"]["subTlvs"]["35"]["hex"] = "23"
DocsisTlvs["25"]["subTlvs"]["35"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["25"]["subTlvs"]["35"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["35"]["subTlvs"]["1"] = {}
DocsisTlvs["25"]["subTlvs"]["35"]["subTlvs"]["1"]["description"] = "MinimumBuffer"
DocsisTlvs["25"]["subTlvs"]["35"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["25"]["subTlvs"]["35"]["subTlvs"]["1"]["datatype"] = "(encode_uint)"
DocsisTlvs["25"]["subTlvs"]["35"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["35"]["subTlvs"]["2"] = {}
DocsisTlvs["25"]["subTlvs"]["35"]["subTlvs"]["2"]["description"] = "TargetBuffer"
DocsisTlvs["25"]["subTlvs"]["35"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["25"]["subTlvs"]["35"]["subTlvs"]["2"]["datatype"] = "(encode_uint)"
DocsisTlvs["25"]["subTlvs"]["35"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["35"]["subTlvs"]["3"] = {}
DocsisTlvs["25"]["subTlvs"]["35"]["subTlvs"]["3"]["description"] = "MaximumBuffer"
DocsisTlvs["25"]["subTlvs"]["35"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["25"]["subTlvs"]["35"]["subTlvs"]["3"]["datatype"] = "(encode_uint)"
DocsisTlvs["25"]["subTlvs"]["35"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["36"] = {}
DocsisTlvs["25"]["subTlvs"]["36"]["description"] = "DownstreamAggregateServiceFlowReference"
DocsisTlvs["25"]["subTlvs"]["36"]["hex"] = "24"
DocsisTlvs["25"]["subTlvs"]["36"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["25"]["subTlvs"]["36"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["37"] = {}
DocsisTlvs["25"]["subTlvs"]["37"]["description"] = "DownstreamMESPReference"
DocsisTlvs["25"]["subTlvs"]["37"]["hex"] = "25"
DocsisTlvs["25"]["subTlvs"]["37"]["datatype"] = "(encode_ushort)"
DocsisTlvs["25"]["subTlvs"]["37"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["40"] = {}
DocsisTlvs["25"]["subTlvs"]["40"]["description"] = "AQMEncodings"
DocsisTlvs["25"]["subTlvs"]["40"]["hex"] = "28"
DocsisTlvs["25"]["subTlvs"]["40"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["25"]["subTlvs"]["40"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["40"]["subTlvs"]["1"] = {}
DocsisTlvs["25"]["subTlvs"]["40"]["subTlvs"]["1"]["description"] = "SFAQMDisable"
DocsisTlvs["25"]["subTlvs"]["40"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["25"]["subTlvs"]["40"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["25"]["subTlvs"]["40"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["40"]["subTlvs"]["2"] = {}
DocsisTlvs["25"]["subTlvs"]["40"]["subTlvs"]["2"]["description"] = "SFAQMLatencyTarget"
DocsisTlvs["25"]["subTlvs"]["40"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["25"]["subTlvs"]["40"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["25"]["subTlvs"]["40"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["41"] = {}
DocsisTlvs["25"]["subTlvs"]["41"]["description"] = "DataRateUnitSetting"
DocsisTlvs["25"]["subTlvs"]["41"]["hex"] = "29"
DocsisTlvs["25"]["subTlvs"]["41"]["datatype"] = "(encode_uchar)"
DocsisTlvs["25"]["subTlvs"]["41"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["description"] = "VendorSpecific"
DocsisTlvs["25"]["subTlvs"]["43"]["hex"] = "2b"
DocsisTlvs["25"]["subTlvs"]["43"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["1"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["1"]["description"] = "CMLoadBalancingPolicyID"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["1"]["datatype"] = "(encode_uint)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["2"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["2"]["description"] = "CMLoadBalancingPriority"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["2"]["datatype"] = "(encode_uint)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["3"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["3"]["description"] = "CMLoadBalancingGroupID"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["3"]["datatype"] = "(encode_uint)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["4"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["4"]["description"] = "CMRangingClassIDExtension"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["4"]["datatype"] = "(encode_ushort)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["description"] = "L2VPNEncoding"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["1"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["1"]["description"] = "VPNIdentifier"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["description"] = "NSIEncapsulation"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["1"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["1"]["description"] = "ServiceMultiplexingValueOther"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["1"]["datatype"] = "(encode_lenzero)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["2"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["2"]["description"] = "NSIEncapsulationSingleQTag"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["2"]["datatype"] = "(encode_ushort)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["3"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["3"]["description"] = "NSIEncapsulationDualQTag"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["3"]["datatype"] = "(encode_dual_qtag)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["description"] = "ServiceMultiplexingValueMPLSPW"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["1"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["1"]["description"] = "MPLSPseudowireID"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["1"]["datatype"] = "(encode_uint)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["2"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["2"]["description"] = "MPLSPeerIpAddress"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["2"]["datatype"] = "(encode_char_ip_ip6)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["3"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["3"]["description"] = "MPLSPseudowireType"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["3"]["datatype"] = "(encode_uchar)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["4"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["4"]["description"] = "MPLSBackupPseudowireID"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["4"]["datatype"] = "(encode_uint)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["5"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["5"]["description"] = "MPLSBackupPeerIpAddress"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["5"]["datatype"] = "(encode_char_ip_ip6)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["5"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["5"]["description"] = "ServiceMultiplexingValueL2TPv3Peer"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["5"]["datatype"] = "(encode_char_ip_ip6)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["description"] = "IEEE8021ahEncapsulation"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["1"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["1"]["description"] = "ITCIEncapsulation"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["2"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["2"]["description"] = "BDAEncapsulation"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["3"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["3"]["description"] = "BTCIEncapsulation"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["4"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["4"]["description"] = "ITPIDEncapsulation"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["5"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["5"]["description"] = "IPCPEncapsulation"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["5"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["6"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["6"]["description"] = "IDEIEncapsulation"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["6"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["7"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["7"]["description"] = "IUCAEncapsulation"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["7"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["8"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["8"]["description"] = "ISIDEncapsulation"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["8"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["9"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["9"]["description"] = "BTPIDEncapsulation"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["9"]["hex"] = "9"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["9"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["9"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["10"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["10"]["description"] = "BPCPEncapsulation"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["10"]["hex"] = "a"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["10"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["11"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["11"]["description"] = "BDEIEncapsulation"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["11"]["hex"] = "b"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["11"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["12"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["12"]["description"] = "BVIDEncapsulation"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["12"]["hex"] = "c"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["12"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["8"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["8"]["description"] = "ServiceMultiplexingValueIEEE8021adSTPID"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["8"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["3"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["3"]["description"] = "eSAFEDHCPSnooping"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["4"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["4"]["description"] = "CMInterfaceMaskCMIMSubtype"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["5"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["5"]["description"] = "AttachmentGroupID"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["5"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["6"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["6"]["description"] = "SourceAttachmentIndividualID"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["6"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["7"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["7"]["description"] = "TargetAttachmentIndividualID"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["7"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["8"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["8"]["description"] = "IngressUserPriority"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["8"]["datatype"] = "(encode_uchar)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["9"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["9"]["description"] = "UserPriorityRange"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["9"]["hex"] = "9"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["9"]["datatype"] = "(encode_char_list)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["9"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["10"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["10"]["description"] = "L2VPNSADescriptorSubtype"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["10"]["hex"] = "a"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["10"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["12"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["12"]["description"] = "PseudowireType"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["12"]["hex"] = "c"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["12"]["datatype"] = "(encode_uchar)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["13"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["13"]["description"] = "L2VPNMode"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["13"]["hex"] = "d"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["13"]["datatype"] = "(encode_uchar)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["13"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["description"] = "TPIDTranslation"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["hex"] = "e"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["1"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["1"]["description"] = "UpstreamTPIDTranslation"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["2"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["2"]["description"] = "DownstreamTPIDTranslation"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["3"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["3"]["description"] = "UpstreamSTPIDTranslation"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["4"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["4"]["description"] = "DownstreamSTPIDTranslation"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["5"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["5"]["description"] = "UpstreamBTPIDTranslation"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["5"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["6"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["6"]["description"] = "DownstreamBTPIDTranslation"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["6"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["7"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["7"]["description"] = "UpstreamITPIDTranslation"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["7"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["8"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["8"]["description"] = "DownstreamITPIDTranslation"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["8"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["description"] = "L2CPProcessing"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["hex"] = "f"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["1"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["1"]["description"] = "L2CPTunnelMode"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["2"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["2"]["description"] = "L2CPDMACAddress"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["2"]["datatype"] = "(encode_ether)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["3"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["3"]["description"] = "L2CPOverwrotingDMACAddress"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["3"]["datatype"] = "(encode_ether)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["16"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["16"]["description"] = "DACDisableEnableConfiguration"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["16"]["hex"] = "10"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["16"]["datatype"] = "(encode_uchar)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["16"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["18"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["18"]["description"] = "PseudowireClass"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["18"]["hex"] = "12"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["18"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["18"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["description"] = "ServiceDelimiter"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["hex"] = "13"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["1"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["1"]["description"] = "CVIDDelimiter"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["2"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["2"]["description"] = "SVIDDelimiter"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["3"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["3"]["description"] = "ISIDDelimiter"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["4"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["4"]["description"] = "BVIDDelimiter"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["description"] = "VirtualSwitchInstanceEncoding"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["hex"] = "14"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["1"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["1"]["description"] = "VPLSClass"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["2"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["2"]["description"] = "ETreeRole"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["3"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["3"]["description"] = "ETreeRootVID"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["4"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["4"]["description"] = "ETreeLeafVID"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["description"] = "BGPAttribute"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["hex"] = "15"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["1"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["1"]["description"] = "BGPVPNID"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["1"]["datatype"] = "(encode_uint)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["2"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["2"]["description"] = "RouteDistinguisher"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["3"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["3"]["description"] = "RouteTargetImport"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["4"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["4"]["description"] = "RouteTargetExport"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["5"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["5"]["description"] = "CEIDVEID"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["5"]["datatype"] = "(encode_ushort)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["23"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["23"]["description"] = "PseudowireSignaling"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["23"]["hex"] = "17"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["23"]["datatype"] = "(encode_uchar)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["23"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["description"] = "SOAMSubtype"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["hex"] = "18"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["description"] = "MEPConfiguration"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["1"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["1"]["description"] = "MDLevel"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["2"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["2"]["description"] = "MDName"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["2"]["datatype"] = "(encode_string)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["3"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["3"]["description"] = "MAName"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["3"]["datatype"] = "(encode_string)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["4"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["4"]["description"] = "MEPID"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["4"]["datatype"] = "(encode_ushort)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["description"] = "RemoteMEPConfiguration"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["1"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["1"]["description"] = "RemoteMDLevel"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["2"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["2"]["description"] = "RemoteMDName"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["2"]["datatype"] = "(encode_string)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["3"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["3"]["description"] = "RemoteMAName"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["3"]["datatype"] = "(encode_string)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["4"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["4"]["description"] = "RemoteMEPID"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["4"]["datatype"] = "(encode_ushort)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["description"] = "FaultManagementConfiguration"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["1"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["1"]["description"] = "ContinuityCheckMessages"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["2"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["2"]["description"] = "LoopbackFunction"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["3"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["3"]["description"] = "LinktraceFunction"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["3"]["datatype"] = "(encode_uchar)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["description"] = "PerformanceManagementConfiguration"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["description"] = "FrameDelayMeasurement"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["1"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["1"]["description"] = "FrameDelayMeasurementEnable"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["2"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["2"]["description"] = "FrameDelayMeasurementOneWayTwoWay"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["3"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["3"]["description"] = "FrameDelayMeasurementTransmissionPeriodicity"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["3"]["datatype"] = "(encode_ushort)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["description"] = "FrameLossMeasurement"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["1"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["1"]["description"] = "FrameLossMeasurementEnable"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["2"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["2"]["description"] = "FrameLossMeasurementTransmissionPeriodicity"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["26"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["26"]["description"] = "L2VPNDSID"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["26"]["hex"] = "1a"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["26"]["datatype"] = "(encode_uint24)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["26"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["description"] = "VendorSpecificL2VPNSubtype"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["hex"] = "2b"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["subTlvs"]["8"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["subTlvs"]["8"]["description"] = "VendorIdentifier"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["subTlvs"]["8"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["6"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["6"]["description"] = "ExtendedCMTSMICConfigurationSetting"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["6"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["1"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["1"]["description"] = "ExtendedCMTSMICHMACtype"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["2"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["2"]["description"] = "ExtendedCMTSMICBitmap"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["3"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["3"]["description"] = "ExplicitExtendedCMTSMICDigest"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["7"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["7"]["description"] = "SAVAuthorizationEncoding"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["7"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["1"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["1"]["description"] = "SAVGroupName"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["1"]["datatype"] = "(encode_string)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["description"] = "SAVStaticPrefixRule"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["1"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["1"]["description"] = "SAVStaticPrefixAddress"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["1"]["datatype"] = "(encode_ip_ip6)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["2"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["2"]["description"] = "SAVStaticPrefixLength"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["8"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["8"]["description"] = "VendorIdentifier"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["8"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["9"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["9"]["description"] = "CMAttributeMasks"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["9"]["hex"] = "9"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["9"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["1"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["1"]["description"] = "CMDownstreamRequiredAttributeMask"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["2"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["2"]["description"] = "CMDownstreamForbiddenAttributeMask"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["3"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["3"]["description"] = "CMUpstreamRequiredAttributeMask"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["4"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["4"]["description"] = "CMUpstreamForbiddenAttributeMask"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["description"] = "IPMulticastJoinAuthorization"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["hex"] = "a"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["1"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["1"]["description"] = "IPMulticastProfileName"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["1"]["datatype"] = "(encode_string)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["description"] = "IPMulticastJoinAuthStaticSessionRule"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["1"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["1"]["description"] = "MulticastRulePriority"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["2"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["2"]["description"] = "AuthorizationAction"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["3"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["3"]["description"] = "SourcePrefixAddress"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["3"]["datatype"] = "(encode_ip_ip6)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["4"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["4"]["description"] = "SourcePrefixLength"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["4"]["datatype"] = "(encode_uchar)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["5"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["5"]["description"] = "GroupPrefixAddress"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["5"]["datatype"] = "(encode_ip_ip6)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["6"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["6"]["description"] = "GroupPrefixLength"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["6"]["datatype"] = "(encode_uchar)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["3"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["3"]["description"] = "MaximumMulticastSessions"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["3"]["datatype"] = "(encode_ushort)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["11"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["11"]["description"] = "ServiceTypeIdentifier"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["11"]["hex"] = "b"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["11"]["datatype"] = "(encode_string)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"]["description"] = "DEMARCAutoConfiguration"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"]["hex"] = "c"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["1"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["1"]["description"] = "DACDisableEnableConfig"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["2"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["2"]["description"] = "CMIMEncoding"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["3"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["3"]["description"] = "UpstreamServiceClassName"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["3"]["datatype"] = "(encode_strzero)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["4"] = {}
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["4"]["description"] = "DownstreamServiceClassName"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["4"]["datatype"] = "(encode_strzero)"
DocsisTlvs["25"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["26"] = {}
DocsisTlvs["26"]["description"] = "PHS"
DocsisTlvs["26"]["hex"] = "1a"
DocsisTlvs["26"]["datatype"] = "(decode_aggregate)   "
DocsisTlvs["26"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["1"] = {}
DocsisTlvs["26"]["subTlvs"]["1"]["description"] = "PHSClassifierRef"
DocsisTlvs["26"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["26"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["26"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["2"] = {}
DocsisTlvs["26"]["subTlvs"]["2"]["description"] = "PHSClassifierId"
DocsisTlvs["26"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["26"]["subTlvs"]["2"]["datatype"] = "(encode_ushort)"
DocsisTlvs["26"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["3"] = {}
DocsisTlvs["26"]["subTlvs"]["3"]["description"] = "PHSServiceFlowRef"
DocsisTlvs["26"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["26"]["subTlvs"]["3"]["datatype"] = "(encode_ushort)"
DocsisTlvs["26"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["4"] = {}
DocsisTlvs["26"]["subTlvs"]["4"]["description"] = "PHSServiceFlowId"
DocsisTlvs["26"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["26"]["subTlvs"]["4"]["datatype"] = "(encode_uint)"
DocsisTlvs["26"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["5"] = {}
DocsisTlvs["26"]["subTlvs"]["5"]["description"] = "PHSDSCAction"
DocsisTlvs["26"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["26"]["subTlvs"]["5"]["datatype"] = "(encode_uchar)"
DocsisTlvs["26"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["7"] = {}
DocsisTlvs["26"]["subTlvs"]["7"]["description"] = "PHSField"
DocsisTlvs["26"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["26"]["subTlvs"]["7"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["8"] = {}
DocsisTlvs["26"]["subTlvs"]["8"]["description"] = "PHSIndex"
DocsisTlvs["26"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["26"]["subTlvs"]["8"]["datatype"] = "(encode_uchar)"
DocsisTlvs["26"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["9"] = {}
DocsisTlvs["26"]["subTlvs"]["9"]["description"] = "PHSMask"
DocsisTlvs["26"]["subTlvs"]["9"]["hex"] = "9"
DocsisTlvs["26"]["subTlvs"]["9"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["9"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["10"] = {}
DocsisTlvs["26"]["subTlvs"]["10"]["description"] = "PHSSize"
DocsisTlvs["26"]["subTlvs"]["10"]["hex"] = "a"
DocsisTlvs["26"]["subTlvs"]["10"]["datatype"] = "(encode_uchar)"
DocsisTlvs["26"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["11"] = {}
DocsisTlvs["26"]["subTlvs"]["11"]["description"] = "PHSVerify"
DocsisTlvs["26"]["subTlvs"]["11"]["hex"] = "b"
DocsisTlvs["26"]["subTlvs"]["11"]["datatype"] = "(encode_uchar)"
DocsisTlvs["26"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["13"] = {}
DocsisTlvs["26"]["subTlvs"]["13"]["description"] = "PHSDBCAction"
DocsisTlvs["26"]["subTlvs"]["13"]["hex"] = "d"
DocsisTlvs["26"]["subTlvs"]["13"]["datatype"] = "(encode_uchar)"
DocsisTlvs["26"]["subTlvs"]["13"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["description"] = "VendorSpecific"
DocsisTlvs["26"]["subTlvs"]["43"]["hex"] = "2b"
DocsisTlvs["26"]["subTlvs"]["43"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["1"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["1"]["description"] = "CMLoadBalancingPolicyID"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["1"]["datatype"] = "(encode_uint)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["2"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["2"]["description"] = "CMLoadBalancingPriority"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["2"]["datatype"] = "(encode_uint)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["3"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["3"]["description"] = "CMLoadBalancingGroupID"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["3"]["datatype"] = "(encode_uint)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["4"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["4"]["description"] = "CMRangingClassIDExtension"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["4"]["datatype"] = "(encode_ushort)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["description"] = "L2VPNEncoding"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["1"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["1"]["description"] = "VPNIdentifier"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["description"] = "NSIEncapsulation"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["1"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["1"]["description"] = "ServiceMultiplexingValueOther"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["1"]["datatype"] = "(encode_lenzero)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["2"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["2"]["description"] = "NSIEncapsulationSingleQTag"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["2"]["datatype"] = "(encode_ushort)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["3"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["3"]["description"] = "NSIEncapsulationDualQTag"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["3"]["datatype"] = "(encode_dual_qtag)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["description"] = "ServiceMultiplexingValueMPLSPW"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["1"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["1"]["description"] = "MPLSPseudowireID"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["1"]["datatype"] = "(encode_uint)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["2"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["2"]["description"] = "MPLSPeerIpAddress"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["2"]["datatype"] = "(encode_char_ip_ip6)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["3"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["3"]["description"] = "MPLSPseudowireType"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["3"]["datatype"] = "(encode_uchar)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["4"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["4"]["description"] = "MPLSBackupPseudowireID"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["4"]["datatype"] = "(encode_uint)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["5"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["5"]["description"] = "MPLSBackupPeerIpAddress"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["5"]["datatype"] = "(encode_char_ip_ip6)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["5"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["5"]["description"] = "ServiceMultiplexingValueL2TPv3Peer"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["5"]["datatype"] = "(encode_char_ip_ip6)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["description"] = "IEEE8021ahEncapsulation"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["1"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["1"]["description"] = "ITCIEncapsulation"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["2"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["2"]["description"] = "BDAEncapsulation"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["3"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["3"]["description"] = "BTCIEncapsulation"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["4"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["4"]["description"] = "ITPIDEncapsulation"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["5"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["5"]["description"] = "IPCPEncapsulation"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["5"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["6"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["6"]["description"] = "IDEIEncapsulation"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["6"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["7"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["7"]["description"] = "IUCAEncapsulation"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["7"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["8"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["8"]["description"] = "ISIDEncapsulation"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["8"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["9"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["9"]["description"] = "BTPIDEncapsulation"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["9"]["hex"] = "9"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["9"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["9"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["10"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["10"]["description"] = "BPCPEncapsulation"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["10"]["hex"] = "a"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["10"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["11"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["11"]["description"] = "BDEIEncapsulation"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["11"]["hex"] = "b"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["11"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["12"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["12"]["description"] = "BVIDEncapsulation"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["12"]["hex"] = "c"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["12"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["8"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["8"]["description"] = "ServiceMultiplexingValueIEEE8021adSTPID"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["8"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["3"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["3"]["description"] = "eSAFEDHCPSnooping"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["4"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["4"]["description"] = "CMInterfaceMaskCMIMSubtype"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["5"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["5"]["description"] = "AttachmentGroupID"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["5"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["6"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["6"]["description"] = "SourceAttachmentIndividualID"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["6"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["7"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["7"]["description"] = "TargetAttachmentIndividualID"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["7"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["8"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["8"]["description"] = "IngressUserPriority"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["8"]["datatype"] = "(encode_uchar)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["9"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["9"]["description"] = "UserPriorityRange"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["9"]["hex"] = "9"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["9"]["datatype"] = "(encode_char_list)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["9"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["10"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["10"]["description"] = "L2VPNSADescriptorSubtype"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["10"]["hex"] = "a"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["10"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["12"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["12"]["description"] = "PseudowireType"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["12"]["hex"] = "c"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["12"]["datatype"] = "(encode_uchar)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["13"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["13"]["description"] = "L2VPNMode"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["13"]["hex"] = "d"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["13"]["datatype"] = "(encode_uchar)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["13"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["description"] = "TPIDTranslation"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["hex"] = "e"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["1"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["1"]["description"] = "UpstreamTPIDTranslation"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["2"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["2"]["description"] = "DownstreamTPIDTranslation"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["3"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["3"]["description"] = "UpstreamSTPIDTranslation"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["4"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["4"]["description"] = "DownstreamSTPIDTranslation"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["5"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["5"]["description"] = "UpstreamBTPIDTranslation"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["5"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["6"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["6"]["description"] = "DownstreamBTPIDTranslation"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["6"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["7"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["7"]["description"] = "UpstreamITPIDTranslation"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["7"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["8"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["8"]["description"] = "DownstreamITPIDTranslation"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["8"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["description"] = "L2CPProcessing"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["hex"] = "f"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["1"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["1"]["description"] = "L2CPTunnelMode"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["2"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["2"]["description"] = "L2CPDMACAddress"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["2"]["datatype"] = "(encode_ether)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["3"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["3"]["description"] = "L2CPOverwrotingDMACAddress"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["3"]["datatype"] = "(encode_ether)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["16"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["16"]["description"] = "DACDisableEnableConfiguration"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["16"]["hex"] = "10"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["16"]["datatype"] = "(encode_uchar)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["16"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["18"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["18"]["description"] = "PseudowireClass"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["18"]["hex"] = "12"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["18"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["18"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["description"] = "ServiceDelimiter"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["hex"] = "13"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["1"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["1"]["description"] = "CVIDDelimiter"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["2"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["2"]["description"] = "SVIDDelimiter"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["3"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["3"]["description"] = "ISIDDelimiter"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["4"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["4"]["description"] = "BVIDDelimiter"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["description"] = "VirtualSwitchInstanceEncoding"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["hex"] = "14"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["1"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["1"]["description"] = "VPLSClass"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["2"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["2"]["description"] = "ETreeRole"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["3"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["3"]["description"] = "ETreeRootVID"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["4"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["4"]["description"] = "ETreeLeafVID"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["description"] = "BGPAttribute"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["hex"] = "15"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["1"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["1"]["description"] = "BGPVPNID"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["1"]["datatype"] = "(encode_uint)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["2"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["2"]["description"] = "RouteDistinguisher"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["3"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["3"]["description"] = "RouteTargetImport"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["4"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["4"]["description"] = "RouteTargetExport"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["5"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["5"]["description"] = "CEIDVEID"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["5"]["datatype"] = "(encode_ushort)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["23"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["23"]["description"] = "PseudowireSignaling"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["23"]["hex"] = "17"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["23"]["datatype"] = "(encode_uchar)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["23"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["description"] = "SOAMSubtype"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["hex"] = "18"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["description"] = "MEPConfiguration"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["1"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["1"]["description"] = "MDLevel"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["2"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["2"]["description"] = "MDName"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["2"]["datatype"] = "(encode_string)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["3"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["3"]["description"] = "MAName"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["3"]["datatype"] = "(encode_string)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["4"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["4"]["description"] = "MEPID"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["4"]["datatype"] = "(encode_ushort)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["description"] = "RemoteMEPConfiguration"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["1"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["1"]["description"] = "RemoteMDLevel"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["2"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["2"]["description"] = "RemoteMDName"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["2"]["datatype"] = "(encode_string)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["3"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["3"]["description"] = "RemoteMAName"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["3"]["datatype"] = "(encode_string)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["4"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["4"]["description"] = "RemoteMEPID"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["4"]["datatype"] = "(encode_ushort)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["description"] = "FaultManagementConfiguration"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["1"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["1"]["description"] = "ContinuityCheckMessages"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["2"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["2"]["description"] = "LoopbackFunction"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["3"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["3"]["description"] = "LinktraceFunction"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["3"]["datatype"] = "(encode_uchar)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["description"] = "PerformanceManagementConfiguration"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["description"] = "FrameDelayMeasurement"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["1"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["1"]["description"] = "FrameDelayMeasurementEnable"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["2"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["2"]["description"] = "FrameDelayMeasurementOneWayTwoWay"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["3"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["3"]["description"] = "FrameDelayMeasurementTransmissionPeriodicity"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["3"]["datatype"] = "(encode_ushort)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["description"] = "FrameLossMeasurement"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["1"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["1"]["description"] = "FrameLossMeasurementEnable"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["2"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["2"]["description"] = "FrameLossMeasurementTransmissionPeriodicity"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["26"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["26"]["description"] = "L2VPNDSID"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["26"]["hex"] = "1a"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["26"]["datatype"] = "(encode_uint24)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["26"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["description"] = "VendorSpecificL2VPNSubtype"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["hex"] = "2b"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["subTlvs"]["8"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["subTlvs"]["8"]["description"] = "VendorIdentifier"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["subTlvs"]["8"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["6"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["6"]["description"] = "ExtendedCMTSMICConfigurationSetting"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["6"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["1"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["1"]["description"] = "ExtendedCMTSMICHMACtype"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["2"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["2"]["description"] = "ExtendedCMTSMICBitmap"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["3"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["3"]["description"] = "ExplicitExtendedCMTSMICDigest"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["7"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["7"]["description"] = "SAVAuthorizationEncoding"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["7"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["1"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["1"]["description"] = "SAVGroupName"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["1"]["datatype"] = "(encode_string)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["description"] = "SAVStaticPrefixRule"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["1"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["1"]["description"] = "SAVStaticPrefixAddress"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["1"]["datatype"] = "(encode_ip_ip6)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["2"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["2"]["description"] = "SAVStaticPrefixLength"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["8"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["8"]["description"] = "VendorIdentifier"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["8"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["9"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["9"]["description"] = "CMAttributeMasks"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["9"]["hex"] = "9"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["9"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["1"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["1"]["description"] = "CMDownstreamRequiredAttributeMask"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["2"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["2"]["description"] = "CMDownstreamForbiddenAttributeMask"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["3"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["3"]["description"] = "CMUpstreamRequiredAttributeMask"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["4"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["4"]["description"] = "CMUpstreamForbiddenAttributeMask"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["description"] = "IPMulticastJoinAuthorization"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["hex"] = "a"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["1"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["1"]["description"] = "IPMulticastProfileName"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["1"]["datatype"] = "(encode_string)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["description"] = "IPMulticastJoinAuthStaticSessionRule"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["1"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["1"]["description"] = "MulticastRulePriority"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["2"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["2"]["description"] = "AuthorizationAction"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["3"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["3"]["description"] = "SourcePrefixAddress"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["3"]["datatype"] = "(encode_ip_ip6)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["4"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["4"]["description"] = "SourcePrefixLength"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["4"]["datatype"] = "(encode_uchar)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["5"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["5"]["description"] = "GroupPrefixAddress"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["5"]["datatype"] = "(encode_ip_ip6)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["6"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["6"]["description"] = "GroupPrefixLength"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["6"]["datatype"] = "(encode_uchar)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["3"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["3"]["description"] = "MaximumMulticastSessions"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["3"]["datatype"] = "(encode_ushort)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["11"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["11"]["description"] = "ServiceTypeIdentifier"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["11"]["hex"] = "b"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["11"]["datatype"] = "(encode_string)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"]["description"] = "DEMARCAutoConfiguration"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"]["hex"] = "c"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["1"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["1"]["description"] = "DACDisableEnableConfig"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["2"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["2"]["description"] = "CMIMEncoding"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["3"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["3"]["description"] = "UpstreamServiceClassName"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["3"]["datatype"] = "(encode_strzero)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["4"] = {}
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["4"]["description"] = "DownstreamServiceClassName"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["4"]["datatype"] = "(encode_strzero)"
DocsisTlvs["26"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["28"] = {}
DocsisTlvs["28"]["description"] = "MaxClassifiers"
DocsisTlvs["28"]["hex"] = "1c"
DocsisTlvs["28"]["datatype"] = "(encode_ushort)"
DocsisTlvs["28"]["subTlvs"] = {}

DocsisTlvs["29"] = {}
DocsisTlvs["29"]["description"] = "GlobalPrivacyEnable"
DocsisTlvs["29"]["hex"] = "1d"
DocsisTlvs["29"]["datatype"] = "(encode_uchar)"
DocsisTlvs["29"]["subTlvs"] = {}

DocsisTlvs["32"] = {}
DocsisTlvs["32"]["description"] = "MfgCVCData"
DocsisTlvs["32"]["hex"] = "20"
DocsisTlvs["32"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["32"]["subTlvs"] = {}

DocsisTlvs["170"] = {}
DocsisTlvs["170"]["description"] = "ManufacturerCVC"
DocsisTlvs["170"]["hex"] = "aa"
DocsisTlvs["170"]["datatype"] = "(decode_hexstr)"
DocsisTlvs["170"]["subTlvs"] = {}

DocsisTlvs["33"] = {}
DocsisTlvs["33"]["description"] = "CoSignerCVCData"
DocsisTlvs["33"]["hex"] = "21"
DocsisTlvs["33"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["33"]["subTlvs"] = {}

DocsisTlvs["172"] = {}
DocsisTlvs["172"]["description"] = "CoSignerCVC"
DocsisTlvs["172"]["hex"] = "ac"
DocsisTlvs["172"]["datatype"] = "(decode_hexstr)"
DocsisTlvs["172"]["subTlvs"] = {}

DocsisTlvs["34"] = {}
DocsisTlvs["34"]["description"] = "SnmpV3Kickstart"
DocsisTlvs["34"]["hex"] = "22"
DocsisTlvs["34"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["34"]["subTlvs"] = {}

DocsisTlvs["34"]["subTlvs"]["1"] = {}
DocsisTlvs["34"]["subTlvs"]["1"]["description"] = "SnmpV3SecurityName"
DocsisTlvs["34"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["34"]["subTlvs"]["1"]["datatype"] = "(encode_string)"
DocsisTlvs["34"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["34"]["subTlvs"]["2"] = {}
DocsisTlvs["34"]["subTlvs"]["2"]["description"] = "SnmpV3MgrPublicNumber"
DocsisTlvs["34"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["34"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["34"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["35"] = {}
DocsisTlvs["35"]["description"] = "SubMgmtControl"
DocsisTlvs["35"]["hex"] = "23"
DocsisTlvs["35"]["datatype"] = "(encode_hexstr)"
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
DocsisTlvs["38"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["38"]["subTlvs"] = {}

DocsisTlvs["38"]["subTlvs"]["1"] = {}
DocsisTlvs["38"]["subTlvs"]["1"]["description"] = "SnmpV3TrapRxIP"
DocsisTlvs["38"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["38"]["subTlvs"]["1"]["datatype"] = "(encode_ip)"
DocsisTlvs["38"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["38"]["subTlvs"]["2"] = {}
DocsisTlvs["38"]["subTlvs"]["2"]["description"] = "SnmpV3TrapRxPort"
DocsisTlvs["38"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["38"]["subTlvs"]["2"]["datatype"] = "(encode_ushort)"
DocsisTlvs["38"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["38"]["subTlvs"]["3"] = {}
DocsisTlvs["38"]["subTlvs"]["3"]["description"] = "SnmpV3TrapRxType"
DocsisTlvs["38"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["38"]["subTlvs"]["3"]["datatype"] = "(encode_ushort)"
DocsisTlvs["38"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["38"]["subTlvs"]["4"] = {}
DocsisTlvs["38"]["subTlvs"]["4"]["description"] = "SnmpV3TrapRxTimeout"
DocsisTlvs["38"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["38"]["subTlvs"]["4"]["datatype"] = "(encode_ushort)"
DocsisTlvs["38"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["38"]["subTlvs"]["5"] = {}
DocsisTlvs["38"]["subTlvs"]["5"]["description"] = "SnmpV3TrapRxRetries"
DocsisTlvs["38"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["38"]["subTlvs"]["5"]["datatype"] = "(encode_ushort)"
DocsisTlvs["38"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["38"]["subTlvs"]["6"] = {}
DocsisTlvs["38"]["subTlvs"]["6"]["description"] = "SnmpV3TrapRxFilterOID"
DocsisTlvs["38"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["38"]["subTlvs"]["6"]["datatype"] = "(encode_oid)"
DocsisTlvs["38"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["38"]["subTlvs"]["7"] = {}
DocsisTlvs["38"]["subTlvs"]["7"]["description"] = "SnmpV3TrapRxSecurityName"
DocsisTlvs["38"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["38"]["subTlvs"]["7"]["datatype"] = "(encode_string)"
DocsisTlvs["38"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["38"]["subTlvs"]["8"] = {}
DocsisTlvs["38"]["subTlvs"]["8"]["description"] = "SnmpV3TrapRxIP6"
DocsisTlvs["38"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["38"]["subTlvs"]["8"]["datatype"] = "(encode_ip6)"
DocsisTlvs["38"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["39"] = {}
DocsisTlvs["39"]["description"] = "DocsisTwoEnable"
DocsisTlvs["39"]["hex"] = "27"
DocsisTlvs["39"]["datatype"] = "(encode_uchar)"
DocsisTlvs["39"]["subTlvs"] = {}

DocsisTlvs["40"] = {}
DocsisTlvs["40"]["description"] = "EnableTestModes"
DocsisTlvs["40"]["hex"] = "28"
DocsisTlvs["40"]["datatype"] = "(encode_uchar)"
DocsisTlvs["40"]["subTlvs"] = {}

DocsisTlvs["41"] = {}
DocsisTlvs["41"]["description"] = "DsChannelList"
DocsisTlvs["41"]["hex"] = "29"
DocsisTlvs["41"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["41"]["subTlvs"] = {}

DocsisTlvs["41"]["subTlvs"]["1"] = {}
DocsisTlvs["41"]["subTlvs"]["1"]["description"] = "SingleDsChannel"
DocsisTlvs["41"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["41"]["subTlvs"]["1"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["41"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["41"]["subTlvs"]["1"]["subTlvs"]["1"] = {}
DocsisTlvs["41"]["subTlvs"]["1"]["subTlvs"]["1"]["description"] = "SingleDsTimeout"
DocsisTlvs["41"]["subTlvs"]["1"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["41"]["subTlvs"]["1"]["subTlvs"]["1"]["datatype"] = "(encode_ushort)"
DocsisTlvs["41"]["subTlvs"]["1"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["41"]["subTlvs"]["1"]["subTlvs"]["2"] = {}
DocsisTlvs["41"]["subTlvs"]["1"]["subTlvs"]["2"]["description"] = "SingleDsFrequency"
DocsisTlvs["41"]["subTlvs"]["1"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["41"]["subTlvs"]["1"]["subTlvs"]["2"]["datatype"] = "(encode_uint)"
DocsisTlvs["41"]["subTlvs"]["1"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["41"]["subTlvs"]["2"] = {}
DocsisTlvs["41"]["subTlvs"]["2"]["description"] = "DsFreqRange"
DocsisTlvs["41"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["41"]["subTlvs"]["2"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["41"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["41"]["subTlvs"]["2"]["subTlvs"]["1"] = {}
DocsisTlvs["41"]["subTlvs"]["2"]["subTlvs"]["1"]["description"] = "DsFreqRangeTimeout"
DocsisTlvs["41"]["subTlvs"]["2"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["41"]["subTlvs"]["2"]["subTlvs"]["1"]["datatype"] = "(encode_ushort)"
DocsisTlvs["41"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["41"]["subTlvs"]["2"]["subTlvs"]["2"] = {}
DocsisTlvs["41"]["subTlvs"]["2"]["subTlvs"]["2"]["description"] = "DsFreqRangeStart"
DocsisTlvs["41"]["subTlvs"]["2"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["41"]["subTlvs"]["2"]["subTlvs"]["2"]["datatype"] = "(encode_uint)"
DocsisTlvs["41"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["41"]["subTlvs"]["2"]["subTlvs"]["3"] = {}
DocsisTlvs["41"]["subTlvs"]["2"]["subTlvs"]["3"]["description"] = "DsFreqRangeEnd"
DocsisTlvs["41"]["subTlvs"]["2"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["41"]["subTlvs"]["2"]["subTlvs"]["3"]["datatype"] = "(encode_uint)"
DocsisTlvs["41"]["subTlvs"]["2"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["41"]["subTlvs"]["2"]["subTlvs"]["4"] = {}
DocsisTlvs["41"]["subTlvs"]["2"]["subTlvs"]["4"]["description"] = "DsFreqRangeStepSize"
DocsisTlvs["41"]["subTlvs"]["2"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["41"]["subTlvs"]["2"]["subTlvs"]["4"]["datatype"] = "(encode_uint)"
DocsisTlvs["41"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["41"]["subTlvs"]["3"] = {}
DocsisTlvs["41"]["subTlvs"]["3"]["description"] = "DefaultScanTimeout"
DocsisTlvs["41"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["41"]["subTlvs"]["3"]["datatype"] = "(encode_ushort)"
DocsisTlvs["41"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["42"] = {}
DocsisTlvs["42"]["description"] = "MulticastMACAddress"
DocsisTlvs["42"]["hex"] = "2a"
DocsisTlvs["42"]["datatype"] = "(encode_ether)"
DocsisTlvs["42"]["subTlvs"] = {}

DocsisTlvs["43"] = {}
DocsisTlvs["43"]["description"] = "VendorSpecific"
DocsisTlvs["43"]["hex"] = "2b"
DocsisTlvs["43"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["43"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["1"] = {}
DocsisTlvs["43"]["subTlvs"]["1"]["description"] = "CMLoadBalancingPolicyID"
DocsisTlvs["43"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["43"]["subTlvs"]["1"]["datatype"] = "(encode_uint)"
DocsisTlvs["43"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["2"] = {}
DocsisTlvs["43"]["subTlvs"]["2"]["description"] = "CMLoadBalancingPriority"
DocsisTlvs["43"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["43"]["subTlvs"]["2"]["datatype"] = "(encode_uint)"
DocsisTlvs["43"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["3"] = {}
DocsisTlvs["43"]["subTlvs"]["3"]["description"] = "CMLoadBalancingGroupID"
DocsisTlvs["43"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["43"]["subTlvs"]["3"]["datatype"] = "(encode_uint)"
DocsisTlvs["43"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["4"] = {}
DocsisTlvs["43"]["subTlvs"]["4"]["description"] = "CMRangingClassIDExtension"
DocsisTlvs["43"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["43"]["subTlvs"]["4"]["datatype"] = "(encode_ushort)"
DocsisTlvs["43"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["description"] = "L2VPNEncoding"
DocsisTlvs["43"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["43"]["subTlvs"]["5"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["1"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["1"]["description"] = "VPNIdentifier"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["description"] = "NSIEncapsulation"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["1"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["1"]["description"] = "ServiceMultiplexingValueOther"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["1"]["datatype"] = "(encode_lenzero)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["2"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["2"]["description"] = "NSIEncapsulationSingleQTag"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["2"]["datatype"] = "(encode_ushort)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["3"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["3"]["description"] = "NSIEncapsulationDualQTag"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["3"]["datatype"] = "(encode_dual_qtag)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["description"] = "ServiceMultiplexingValueMPLSPW"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["1"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["1"]["description"] = "MPLSPseudowireID"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["1"]["datatype"] = "(encode_uint)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["2"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["2"]["description"] = "MPLSPeerIpAddress"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["2"]["datatype"] = "(encode_char_ip_ip6)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["3"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["3"]["description"] = "MPLSPseudowireType"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["3"]["datatype"] = "(encode_uchar)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["4"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["4"]["description"] = "MPLSBackupPseudowireID"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["4"]["datatype"] = "(encode_uint)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["5"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["5"]["description"] = "MPLSBackupPeerIpAddress"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["5"]["datatype"] = "(encode_char_ip_ip6)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["5"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["5"]["description"] = "ServiceMultiplexingValueL2TPv3Peer"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["5"]["datatype"] = "(encode_char_ip_ip6)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["description"] = "IEEE8021ahEncapsulation"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["1"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["1"]["description"] = "ITCIEncapsulation"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["2"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["2"]["description"] = "BDAEncapsulation"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["3"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["3"]["description"] = "BTCIEncapsulation"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["4"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["4"]["description"] = "ITPIDEncapsulation"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["5"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["5"]["description"] = "IPCPEncapsulation"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["5"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["6"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["6"]["description"] = "IDEIEncapsulation"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["6"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["7"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["7"]["description"] = "IUCAEncapsulation"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["7"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["8"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["8"]["description"] = "ISIDEncapsulation"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["8"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["9"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["9"]["description"] = "BTPIDEncapsulation"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["9"]["hex"] = "9"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["9"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["9"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["10"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["10"]["description"] = "BPCPEncapsulation"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["10"]["hex"] = "a"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["10"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["11"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["11"]["description"] = "BDEIEncapsulation"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["11"]["hex"] = "b"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["11"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["12"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["12"]["description"] = "BVIDEncapsulation"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["12"]["hex"] = "c"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["12"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["8"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["8"]["description"] = "ServiceMultiplexingValueIEEE8021adSTPID"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["8"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["3"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["3"]["description"] = "eSAFEDHCPSnooping"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["4"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["4"]["description"] = "CMInterfaceMaskCMIMSubtype"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["5"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["5"]["description"] = "AttachmentGroupID"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["5"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["6"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["6"]["description"] = "SourceAttachmentIndividualID"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["6"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["7"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["7"]["description"] = "TargetAttachmentIndividualID"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["7"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["8"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["8"]["description"] = "IngressUserPriority"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["8"]["datatype"] = "(encode_uchar)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["9"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["9"]["description"] = "UserPriorityRange"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["9"]["hex"] = "9"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["9"]["datatype"] = "(encode_char_list)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["9"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["10"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["10"]["description"] = "L2VPNSADescriptorSubtype"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["10"]["hex"] = "a"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["10"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["12"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["12"]["description"] = "PseudowireType"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["12"]["hex"] = "c"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["12"]["datatype"] = "(encode_uchar)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["13"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["13"]["description"] = "L2VPNMode"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["13"]["hex"] = "d"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["13"]["datatype"] = "(encode_uchar)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["13"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["14"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["14"]["description"] = "TPIDTranslation"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["14"]["hex"] = "e"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["14"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["1"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["1"]["description"] = "UpstreamTPIDTranslation"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["2"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["2"]["description"] = "DownstreamTPIDTranslation"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["3"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["3"]["description"] = "UpstreamSTPIDTranslation"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["4"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["4"]["description"] = "DownstreamSTPIDTranslation"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["5"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["5"]["description"] = "UpstreamBTPIDTranslation"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["5"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["6"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["6"]["description"] = "DownstreamBTPIDTranslation"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["6"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["7"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["7"]["description"] = "UpstreamITPIDTranslation"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["7"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["8"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["8"]["description"] = "DownstreamITPIDTranslation"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["8"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["15"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["15"]["description"] = "L2CPProcessing"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["15"]["hex"] = "f"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["15"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["1"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["1"]["description"] = "L2CPTunnelMode"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["2"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["2"]["description"] = "L2CPDMACAddress"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["2"]["datatype"] = "(encode_ether)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["3"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["3"]["description"] = "L2CPOverwrotingDMACAddress"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["3"]["datatype"] = "(encode_ether)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["16"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["16"]["description"] = "DACDisableEnableConfiguration"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["16"]["hex"] = "10"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["16"]["datatype"] = "(encode_uchar)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["16"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["18"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["18"]["description"] = "PseudowireClass"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["18"]["hex"] = "12"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["18"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["18"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["19"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["19"]["description"] = "ServiceDelimiter"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["19"]["hex"] = "13"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["19"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["1"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["1"]["description"] = "CVIDDelimiter"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["2"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["2"]["description"] = "SVIDDelimiter"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["3"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["3"]["description"] = "ISIDDelimiter"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["4"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["4"]["description"] = "BVIDDelimiter"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["20"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["20"]["description"] = "VirtualSwitchInstanceEncoding"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["20"]["hex"] = "14"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["20"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["1"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["1"]["description"] = "VPLSClass"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["2"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["2"]["description"] = "ETreeRole"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["3"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["3"]["description"] = "ETreeRootVID"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["4"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["4"]["description"] = "ETreeLeafVID"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["21"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["21"]["description"] = "BGPAttribute"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["21"]["hex"] = "15"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["21"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["1"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["1"]["description"] = "BGPVPNID"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["1"]["datatype"] = "(encode_uint)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["2"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["2"]["description"] = "RouteDistinguisher"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["3"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["3"]["description"] = "RouteTargetImport"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["4"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["4"]["description"] = "RouteTargetExport"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["5"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["5"]["description"] = "CEIDVEID"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["5"]["datatype"] = "(encode_ushort)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["23"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["23"]["description"] = "PseudowireSignaling"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["23"]["hex"] = "17"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["23"]["datatype"] = "(encode_uchar)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["23"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["description"] = "SOAMSubtype"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["hex"] = "18"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["description"] = "MEPConfiguration"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["1"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["1"]["description"] = "MDLevel"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["2"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["2"]["description"] = "MDName"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["2"]["datatype"] = "(encode_string)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["3"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["3"]["description"] = "MAName"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["3"]["datatype"] = "(encode_string)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["4"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["4"]["description"] = "MEPID"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["4"]["datatype"] = "(encode_ushort)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["description"] = "RemoteMEPConfiguration"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["1"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["1"]["description"] = "RemoteMDLevel"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["2"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["2"]["description"] = "RemoteMDName"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["2"]["datatype"] = "(encode_string)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["3"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["3"]["description"] = "RemoteMAName"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["3"]["datatype"] = "(encode_string)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["4"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["4"]["description"] = "RemoteMEPID"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["4"]["datatype"] = "(encode_ushort)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["description"] = "FaultManagementConfiguration"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["1"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["1"]["description"] = "ContinuityCheckMessages"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["2"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["2"]["description"] = "LoopbackFunction"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["3"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["3"]["description"] = "LinktraceFunction"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["3"]["datatype"] = "(encode_uchar)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["description"] = "PerformanceManagementConfiguration"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["description"] = "FrameDelayMeasurement"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["1"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["1"]["description"] = "FrameDelayMeasurementEnable"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["2"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["2"]["description"] = "FrameDelayMeasurementOneWayTwoWay"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["3"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["3"]["description"] = "FrameDelayMeasurementTransmissionPeriodicity"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["3"]["datatype"] = "(encode_ushort)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["description"] = "FrameLossMeasurement"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["1"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["1"]["description"] = "FrameLossMeasurementEnable"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["2"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["2"]["description"] = "FrameLossMeasurementTransmissionPeriodicity"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["26"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["26"]["description"] = "L2VPNDSID"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["26"]["hex"] = "1a"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["26"]["datatype"] = "(encode_uint24)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["26"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["43"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["43"]["description"] = "VendorSpecificL2VPNSubtype"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["43"]["hex"] = "2b"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["43"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["43"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["43"]["subTlvs"]["8"] = {}
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["43"]["subTlvs"]["8"]["description"] = "VendorIdentifier"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["43"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["43"]["subTlvs"]["8"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["43"]["subTlvs"]["5"]["subTlvs"]["43"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["6"] = {}
DocsisTlvs["43"]["subTlvs"]["6"]["description"] = "ExtendedCMTSMICConfiguration"
DocsisTlvs["43"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["43"]["subTlvs"]["6"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["43"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["6"]["subTlvs"]["1"] = {}
DocsisTlvs["43"]["subTlvs"]["6"]["subTlvs"]["1"]["description"] = "ExtendedCMTSMICHMACDigestType"
DocsisTlvs["43"]["subTlvs"]["6"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["43"]["subTlvs"]["6"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["43"]["subTlvs"]["6"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["6"]["subTlvs"]["2"] = {}
DocsisTlvs["43"]["subTlvs"]["6"]["subTlvs"]["2"]["description"] = "ExtendedCMTSMICHMACBitmap"
DocsisTlvs["43"]["subTlvs"]["6"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["43"]["subTlvs"]["6"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["43"]["subTlvs"]["6"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["6"]["subTlvs"]["3"] = {}
DocsisTlvs["43"]["subTlvs"]["6"]["subTlvs"]["3"]["description"] = "ExtendedCMTSMICHMACDigest"
DocsisTlvs["43"]["subTlvs"]["6"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["43"]["subTlvs"]["6"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["43"]["subTlvs"]["6"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["7"] = {}
DocsisTlvs["43"]["subTlvs"]["7"]["description"] = "SAVAuthorizationEncoding"
DocsisTlvs["43"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["43"]["subTlvs"]["7"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["43"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["7"]["subTlvs"]["1"] = {}
DocsisTlvs["43"]["subTlvs"]["7"]["subTlvs"]["1"]["description"] = "SAVGroupName"
DocsisTlvs["43"]["subTlvs"]["7"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["43"]["subTlvs"]["7"]["subTlvs"]["1"]["datatype"] = "(encode_string)"
DocsisTlvs["43"]["subTlvs"]["7"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["7"]["subTlvs"]["2"] = {}
DocsisTlvs["43"]["subTlvs"]["7"]["subTlvs"]["2"]["description"] = "SAVStaticPrefixRule"
DocsisTlvs["43"]["subTlvs"]["7"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["43"]["subTlvs"]["7"]["subTlvs"]["2"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["1"] = {}
DocsisTlvs["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["1"]["description"] = "SAVStaticPrefixAddress"
DocsisTlvs["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["1"]["datatype"] = "(encode_ip_ip6)"
DocsisTlvs["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["2"] = {}
DocsisTlvs["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["2"]["description"] = "SAVStaticPrefixLength"
DocsisTlvs["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["8"] = {}
DocsisTlvs["43"]["subTlvs"]["8"]["description"] = "VendorIdentifier"
DocsisTlvs["43"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["43"]["subTlvs"]["8"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["43"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["9"] = {}
DocsisTlvs["43"]["subTlvs"]["9"]["description"] = "CMAttributeMasks"
DocsisTlvs["43"]["subTlvs"]["9"]["hex"] = "9"
DocsisTlvs["43"]["subTlvs"]["9"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["43"]["subTlvs"]["9"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["9"]["subTlvs"]["1"] = {}
DocsisTlvs["43"]["subTlvs"]["9"]["subTlvs"]["1"]["description"] = "CMDownstreamRequiredAttributeMask"
DocsisTlvs["43"]["subTlvs"]["9"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["43"]["subTlvs"]["9"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["43"]["subTlvs"]["9"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["9"]["subTlvs"]["2"] = {}
DocsisTlvs["43"]["subTlvs"]["9"]["subTlvs"]["2"]["description"] = "CMDownstreamForbiddenAttributeMask"
DocsisTlvs["43"]["subTlvs"]["9"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["43"]["subTlvs"]["9"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["43"]["subTlvs"]["9"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["9"]["subTlvs"]["3"] = {}
DocsisTlvs["43"]["subTlvs"]["9"]["subTlvs"]["3"]["description"] = "CMUpstreamRequiredAttributeMask"
DocsisTlvs["43"]["subTlvs"]["9"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["43"]["subTlvs"]["9"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["43"]["subTlvs"]["9"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["9"]["subTlvs"]["4"] = {}
DocsisTlvs["43"]["subTlvs"]["9"]["subTlvs"]["4"]["description"] = "CMUpstreamForbiddenAttributeMask"
DocsisTlvs["43"]["subTlvs"]["9"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["43"]["subTlvs"]["9"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["43"]["subTlvs"]["9"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["10"] = {}
DocsisTlvs["43"]["subTlvs"]["10"]["description"] = "IPMulticastJoinAuthorization"
DocsisTlvs["43"]["subTlvs"]["10"]["hex"] = "a"
DocsisTlvs["43"]["subTlvs"]["10"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["1"] = {}
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["1"]["description"] = "IPMulticastProfileName"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["1"]["datatype"] = "(encode_string)"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["2"] = {}
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["2"]["description"] = "IPMulticastJoinAuthStaticSessionRule"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["2"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["1"] = {}
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["1"]["description"] = "MulticastRulePriority"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["2"] = {}
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["2"]["description"] = "AuthorizationAction"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["3"] = {}
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["3"]["description"] = "SourcePrefixAddress"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["3"]["datatype"] = "(encode_ip_ip6)"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["4"] = {}
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["4"]["description"] = "SourcePrefixLength"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["4"]["datatype"] = "(encode_uchar)"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["5"] = {}
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["5"]["description"] = "GroupPrefixAddress"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["5"]["datatype"] = "(encode_ip_ip6)"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["6"] = {}
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["6"]["description"] = "GroupPrefixLength"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["6"]["datatype"] = "(encode_uchar)"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["3"] = {}
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["3"]["description"] = "MaximumMulticastSessions"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["3"]["datatype"] = "(encode_ushort)"
DocsisTlvs["43"]["subTlvs"]["10"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["11"] = {}
DocsisTlvs["43"]["subTlvs"]["11"]["description"] = "ServiceTypeIdentifier"
DocsisTlvs["43"]["subTlvs"]["11"]["hex"] = "b"
DocsisTlvs["43"]["subTlvs"]["11"]["datatype"] = "(encode_string)"
DocsisTlvs["43"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["12"] = {}
DocsisTlvs["43"]["subTlvs"]["12"]["description"] = "DEMARCAutoConfiguration"
DocsisTlvs["43"]["subTlvs"]["12"]["hex"] = "c"
DocsisTlvs["43"]["subTlvs"]["12"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["43"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["12"]["subTlvs"]["1"] = {}
DocsisTlvs["43"]["subTlvs"]["12"]["subTlvs"]["1"]["description"] = "DACDisableEnableConfig"
DocsisTlvs["43"]["subTlvs"]["12"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["43"]["subTlvs"]["12"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["43"]["subTlvs"]["12"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["12"]["subTlvs"]["2"] = {}
DocsisTlvs["43"]["subTlvs"]["12"]["subTlvs"]["2"]["description"] = "CMIMEncoding"
DocsisTlvs["43"]["subTlvs"]["12"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["43"]["subTlvs"]["12"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["43"]["subTlvs"]["12"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["12"]["subTlvs"]["3"] = {}
DocsisTlvs["43"]["subTlvs"]["12"]["subTlvs"]["3"]["description"] = "UpstreamServiceClassName"
DocsisTlvs["43"]["subTlvs"]["12"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["43"]["subTlvs"]["12"]["subTlvs"]["3"]["datatype"] = "(encode_strzero)"
DocsisTlvs["43"]["subTlvs"]["12"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["43"]["subTlvs"]["12"]["subTlvs"]["4"] = {}
DocsisTlvs["43"]["subTlvs"]["12"]["subTlvs"]["4"]["description"] = "DownstreamServiceClassName"
DocsisTlvs["43"]["subTlvs"]["12"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["43"]["subTlvs"]["12"]["subTlvs"]["4"]["datatype"] = "(encode_strzero)"
DocsisTlvs["43"]["subTlvs"]["12"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["45"] = {}
DocsisTlvs["45"]["description"] = "DUTFiltering"
DocsisTlvs["45"]["hex"] = "2d"
DocsisTlvs["45"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["45"]["subTlvs"] = {}

DocsisTlvs["45"]["subTlvs"]["1"] = {}
DocsisTlvs["45"]["subTlvs"]["1"]["description"] = "DUTControl"
DocsisTlvs["45"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["45"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["45"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["45"]["subTlvs"]["2"] = {}
DocsisTlvs["45"]["subTlvs"]["2"]["description"] = "DUTCMIM"
DocsisTlvs["45"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["45"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["45"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["53"] = {}
DocsisTlvs["53"]["description"] = "SNMPv1v2cCoexistenceConfig"
DocsisTlvs["53"]["hex"] = "35"
DocsisTlvs["53"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["53"]["subTlvs"] = {}

DocsisTlvs["53"]["subTlvs"]["1"] = {}
DocsisTlvs["53"]["subTlvs"]["1"]["description"] = "SNMPv1v2cCommunityName"
DocsisTlvs["53"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["53"]["subTlvs"]["1"]["datatype"] = "(encode_string)"
DocsisTlvs["53"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["53"]["subTlvs"]["2"] = {}
DocsisTlvs["53"]["subTlvs"]["2"]["description"] = "SNMPv1v2cTransportAddressAccess"
DocsisTlvs["53"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["53"]["subTlvs"]["2"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["53"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["53"]["subTlvs"]["2"]["subTlvs"]["1"] = {}
DocsisTlvs["53"]["subTlvs"]["2"]["subTlvs"]["1"]["description"] = "SNMPv1v2cTransportAddress"
DocsisTlvs["53"]["subTlvs"]["2"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["53"]["subTlvs"]["2"]["subTlvs"]["1"]["datatype"] = "(encode_ip_ip6_port)"
DocsisTlvs["53"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["53"]["subTlvs"]["2"]["subTlvs"]["2"] = {}
DocsisTlvs["53"]["subTlvs"]["2"]["subTlvs"]["2"]["description"] = "SNMPv1v2cTransportAddressMask"
DocsisTlvs["53"]["subTlvs"]["2"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["53"]["subTlvs"]["2"]["subTlvs"]["2"]["datatype"] = "(encode_ip_ip6_port)"
DocsisTlvs["53"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["53"]["subTlvs"]["3"] = {}
DocsisTlvs["53"]["subTlvs"]["3"]["description"] = "SNMPv1v2cAccessViewType"
DocsisTlvs["53"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["53"]["subTlvs"]["3"]["datatype"] = "(encode_uchar)"
DocsisTlvs["53"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["53"]["subTlvs"]["4"] = {}
DocsisTlvs["53"]["subTlvs"]["4"]["description"] = "SNMPv1v2cAccessViewName"
DocsisTlvs["53"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["53"]["subTlvs"]["4"]["datatype"] = "(encode_string)"
DocsisTlvs["53"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["54"] = {}
DocsisTlvs["54"]["description"] = "SNMPv3AccessViewConfiguration"
DocsisTlvs["54"]["hex"] = "36"
DocsisTlvs["54"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["54"]["subTlvs"] = {}

DocsisTlvs["54"]["subTlvs"]["1"] = {}
DocsisTlvs["54"]["subTlvs"]["1"]["description"] = "SNMPv3AccessViewName"
DocsisTlvs["54"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["54"]["subTlvs"]["1"]["datatype"] = "(encode_string)"
DocsisTlvs["54"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["54"]["subTlvs"]["2"] = {}
DocsisTlvs["54"]["subTlvs"]["2"]["description"] = "SNMPv3AccessViewSubtree"
DocsisTlvs["54"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["54"]["subTlvs"]["2"]["datatype"] = "(encode_oid)"
DocsisTlvs["54"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["54"]["subTlvs"]["3"] = {}
DocsisTlvs["54"]["subTlvs"]["3"]["description"] = "SNMPv3AccessViewMask"
DocsisTlvs["54"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["54"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["54"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["54"]["subTlvs"]["4"] = {}
DocsisTlvs["54"]["subTlvs"]["4"]["description"] = "SNMPv3AccessViewType"
DocsisTlvs["54"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["54"]["subTlvs"]["4"]["datatype"] = "(encode_uchar)"
DocsisTlvs["54"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["55"] = {}
DocsisTlvs["55"]["description"] = "SNMPCPEAccessControl"
DocsisTlvs["55"]["hex"] = "37"
DocsisTlvs["55"]["datatype"] = "(encode_uchar)"
DocsisTlvs["55"]["subTlvs"] = {}

DocsisTlvs["56"] = {}
DocsisTlvs["56"]["description"] = "ChannelAssignmentConfig"
DocsisTlvs["56"]["hex"] = "38"
DocsisTlvs["56"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["56"]["subTlvs"] = {}

DocsisTlvs["56"]["subTlvs"]["1"] = {}
DocsisTlvs["56"]["subTlvs"]["1"]["description"] = "CaTransmit"
DocsisTlvs["56"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["56"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["56"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["56"]["subTlvs"]["2"] = {}
DocsisTlvs["56"]["subTlvs"]["2"]["description"] = "CaReceive"
DocsisTlvs["56"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["56"]["subTlvs"]["2"]["datatype"] = "(encode_uint)"
DocsisTlvs["56"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["58"] = {}
DocsisTlvs["58"]["description"] = "SwUpgradeServer6"
DocsisTlvs["58"]["hex"] = "3a"
DocsisTlvs["58"]["datatype"] = "(encode_ip6)"
DocsisTlvs["58"]["subTlvs"] = {}

DocsisTlvs["59"] = {}
DocsisTlvs["59"]["description"] = "TFTPProvisionedModemIPv6Address"
DocsisTlvs["59"]["hex"] = "3b"
DocsisTlvs["59"]["datatype"] = "(encode_ip6)"
DocsisTlvs["59"]["subTlvs"] = {}

DocsisTlvs["60"] = {}
DocsisTlvs["60"]["description"] = "UpstreamDropPacketClassification"
DocsisTlvs["60"]["hex"] = "3c"
DocsisTlvs["60"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["60"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["1"] = {}
DocsisTlvs["60"]["subTlvs"]["1"]["description"] = "ClassifierReference"
DocsisTlvs["60"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["60"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["60"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["2"] = {}
DocsisTlvs["60"]["subTlvs"]["2"]["description"] = "ClassifierIdentifier"
DocsisTlvs["60"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["60"]["subTlvs"]["2"]["datatype"] = "(encode_ushort)"
DocsisTlvs["60"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["5"] = {}
DocsisTlvs["60"]["subTlvs"]["5"]["description"] = "RulePriority"
DocsisTlvs["60"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["60"]["subTlvs"]["5"]["datatype"] = "(encode_uchar)"
DocsisTlvs["60"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["7"] = {}
DocsisTlvs["60"]["subTlvs"]["7"]["description"] = "DynamicServiceChangeAction"
DocsisTlvs["60"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["60"]["subTlvs"]["7"]["datatype"] = "(encode_uchar)"
DocsisTlvs["60"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["9"] = {}
DocsisTlvs["60"]["subTlvs"]["9"]["description"] = "IPv4PacketClassification"
DocsisTlvs["60"]["subTlvs"]["9"]["hex"] = "9"
DocsisTlvs["60"]["subTlvs"]["9"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["1"] = {}
DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["1"]["description"] = "IPv4Tos"
DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["2"] = {}
DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["2"]["description"] = "IPProtocol"
DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["2"]["datatype"] = "(encode_ushort)"
DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["3"] = {}
DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["3"]["description"] = "IPv4SourceAddress"
DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["3"]["datatype"] = "(encode_ip)"
DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["4"] = {}
DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["4"]["description"] = "IPv4SourceMask"
DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["4"]["datatype"] = "(encode_ip)"
DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["5"] = {}
DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["5"]["description"] = "IPv4DestinationAddress"
DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["5"]["datatype"] = "(encode_ip)"
DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["6"] = {}
DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["6"]["description"] = "IPv4DestinationMask"
DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["6"]["datatype"] = "(encode_ip)"
DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["7"] = {}
DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["7"]["description"] = "SourcePortStart"
DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["7"]["datatype"] = "(encode_ushort)"
DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["8"] = {}
DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["8"]["description"] = "SourcePortEnd"
DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["8"]["datatype"] = "(encode_ushort)"
DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["9"] = {}
DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["9"]["description"] = "DestinationPortStart"
DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["9"]["hex"] = "9"
DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["9"]["datatype"] = "(encode_ushort)"
DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["9"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["10"] = {}
DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["10"]["description"] = "DestinationPortEnd"
DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["10"]["hex"] = "a"
DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["10"]["datatype"] = "(encode_ushort)"
DocsisTlvs["60"]["subTlvs"]["9"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["10"] = {}
DocsisTlvs["60"]["subTlvs"]["10"]["description"] = "EthernetLLCPacketClassification"
DocsisTlvs["60"]["subTlvs"]["10"]["hex"] = "a"
DocsisTlvs["60"]["subTlvs"]["10"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["60"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["10"]["subTlvs"]["1"] = {}
DocsisTlvs["60"]["subTlvs"]["10"]["subTlvs"]["1"]["description"] = "DestinationMACAddress"
DocsisTlvs["60"]["subTlvs"]["10"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["60"]["subTlvs"]["10"]["subTlvs"]["1"]["datatype"] = "(encode_ethermask)"
DocsisTlvs["60"]["subTlvs"]["10"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["10"]["subTlvs"]["2"] = {}
DocsisTlvs["60"]["subTlvs"]["10"]["subTlvs"]["2"]["description"] = "SourceMACAddress"
DocsisTlvs["60"]["subTlvs"]["10"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["60"]["subTlvs"]["10"]["subTlvs"]["2"]["datatype"] = "(encode_ether)"
DocsisTlvs["60"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["10"]["subTlvs"]["3"] = {}
DocsisTlvs["60"]["subTlvs"]["10"]["subTlvs"]["3"]["description"] = "EthertypeDSAPMacType"
DocsisTlvs["60"]["subTlvs"]["10"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["60"]["subTlvs"]["10"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["10"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["11"] = {}
DocsisTlvs["60"]["subTlvs"]["11"]["description"] = "IEEE8021PQPacketClassification"
DocsisTlvs["60"]["subTlvs"]["11"]["hex"] = "b"
DocsisTlvs["60"]["subTlvs"]["11"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["60"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["11"]["subTlvs"]["1"] = {}
DocsisTlvs["60"]["subTlvs"]["11"]["subTlvs"]["1"]["description"] = "UserPriority"
DocsisTlvs["60"]["subTlvs"]["11"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["60"]["subTlvs"]["11"]["subTlvs"]["1"]["datatype"] = "(encode_char_list)"
DocsisTlvs["60"]["subTlvs"]["11"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["11"]["subTlvs"]["2"] = {}
DocsisTlvs["60"]["subTlvs"]["11"]["subTlvs"]["2"]["description"] = "VlanID"
DocsisTlvs["60"]["subTlvs"]["11"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["60"]["subTlvs"]["11"]["subTlvs"]["2"]["datatype"] = "(encode_ushort)"
DocsisTlvs["60"]["subTlvs"]["11"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["12"] = {}
DocsisTlvs["60"]["subTlvs"]["12"]["description"] = "IPv6PacketClassification"
DocsisTlvs["60"]["subTlvs"]["12"]["hex"] = "c"
DocsisTlvs["60"]["subTlvs"]["12"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["1"] = {}
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["1"]["description"] = "IPv6TrafficClassRangeandMask"
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["2"] = {}
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["2"]["description"] = "IPv6FlowLabel"
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["3"] = {}
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["3"]["description"] = "IPv6NextHeaderType"
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["3"]["datatype"] = "(encode_ushort)"
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["4"] = {}
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["4"]["description"] = "IPv6SourceAddress"
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["4"]["datatype"] = "(encode_ip6)"
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["5"] = {}
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["5"]["description"] = "IPv6SourcePrefixLength"
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["5"]["datatype"] = "(encode_uchar)"
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["6"] = {}
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["6"]["description"] = "IPv6DestinationAddress"
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["6"]["datatype"] = "(encode_ip6)"
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["7"] = {}
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["7"]["description"] = "IPv6DestinationPrefixLength"
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["7"]["datatype"] = "(encode_uchar)"
DocsisTlvs["60"]["subTlvs"]["12"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["13"] = {}
DocsisTlvs["60"]["subTlvs"]["13"]["description"] = "CMInterfaceMaskEncoding"
DocsisTlvs["60"]["subTlvs"]["13"]["hex"] = "d"
DocsisTlvs["60"]["subTlvs"]["13"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["13"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["14"] = {}
DocsisTlvs["60"]["subTlvs"]["14"]["description"] = "STagCTagFrameClassification"
DocsisTlvs["60"]["subTlvs"]["14"]["hex"] = "e"
DocsisTlvs["60"]["subTlvs"]["14"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["1"] = {}
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["1"]["description"] = "STPID"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["2"] = {}
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["2"]["description"] = "SVID"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["3"] = {}
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["3"]["description"] = "SPCP"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["4"] = {}
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["4"]["description"] = "SDEI"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["5"] = {}
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["5"]["description"] = "CTPID"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["5"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["6"] = {}
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["6"]["description"] = "CVID"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["6"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["7"] = {}
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["7"]["description"] = "CPCP"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["7"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["8"] = {}
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["8"]["description"] = "CCFI"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["8"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["9"] = {}
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["9"]["description"] = "STCI"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["9"]["hex"] = "9"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["9"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["9"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["10"] = {}
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["10"]["description"] = "CTCI"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["10"]["hex"] = "a"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["10"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["14"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["15"] = {}
DocsisTlvs["60"]["subTlvs"]["15"]["description"] = "IEEE8021ahPacketClassification"
DocsisTlvs["60"]["subTlvs"]["15"]["hex"] = "f"
DocsisTlvs["60"]["subTlvs"]["15"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["1"] = {}
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["1"]["description"] = "ITPID"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["2"] = {}
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["2"]["description"] = "ISID"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["3"] = {}
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["3"]["description"] = "ITCI"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["4"] = {}
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["4"]["description"] = "IPCP"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["5"] = {}
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["5"]["description"] = "IDEI"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["5"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["6"] = {}
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["6"]["description"] = "IUCA"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["6"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["7"] = {}
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["7"]["description"] = "BTPID"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["7"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["8"] = {}
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["8"]["description"] = "BTCI"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["8"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["9"] = {}
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["9"]["description"] = "BPCP"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["9"]["hex"] = "9"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["9"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["9"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["10"] = {}
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["10"]["description"] = "BDEI"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["10"]["hex"] = "a"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["10"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["11"] = {}
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["11"]["description"] = "BVID"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["11"]["hex"] = "b"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["11"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["12"] = {}
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["12"]["description"] = "BDA"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["12"]["hex"] = "c"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["12"]["datatype"] = "(encode_ether)"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["13"] = {}
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["13"]["description"] = "BSA"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["13"]["hex"] = "d"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["13"]["datatype"] = "(encode_ether)"
DocsisTlvs["60"]["subTlvs"]["15"]["subTlvs"]["13"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["16"] = {}
DocsisTlvs["60"]["subTlvs"]["16"]["description"] = "ICMPv4ICMPv6PacketClassification"
DocsisTlvs["60"]["subTlvs"]["16"]["hex"] = "10"
DocsisTlvs["60"]["subTlvs"]["16"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["60"]["subTlvs"]["16"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["16"]["subTlvs"]["1"] = {}
DocsisTlvs["60"]["subTlvs"]["16"]["subTlvs"]["1"]["description"] = "ICMPv4ICMPv6TypeStart"
DocsisTlvs["60"]["subTlvs"]["16"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["60"]["subTlvs"]["16"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["60"]["subTlvs"]["16"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["16"]["subTlvs"]["2"] = {}
DocsisTlvs["60"]["subTlvs"]["16"]["subTlvs"]["2"]["description"] = "ICMPv4ICMPv6TypeEnd"
DocsisTlvs["60"]["subTlvs"]["16"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["60"]["subTlvs"]["16"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["60"]["subTlvs"]["16"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["17"] = {}
DocsisTlvs["60"]["subTlvs"]["17"]["description"] = "MPLSClassificationEncoding"
DocsisTlvs["60"]["subTlvs"]["17"]["hex"] = "11"
DocsisTlvs["60"]["subTlvs"]["17"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["60"]["subTlvs"]["17"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["17"]["subTlvs"]["1"] = {}
DocsisTlvs["60"]["subTlvs"]["17"]["subTlvs"]["1"]["description"] = "MPLSTCbits"
DocsisTlvs["60"]["subTlvs"]["17"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["60"]["subTlvs"]["17"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["17"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["17"]["subTlvs"]["2"] = {}
DocsisTlvs["60"]["subTlvs"]["17"]["subTlvs"]["2"]["description"] = "MPLSLabel"
DocsisTlvs["60"]["subTlvs"]["17"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["60"]["subTlvs"]["17"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["17"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["description"] = "VendorSpecific"
DocsisTlvs["60"]["subTlvs"]["43"]["hex"] = "2b"
DocsisTlvs["60"]["subTlvs"]["43"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["1"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["1"]["description"] = "CMLoadBalancingPolicyID"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["1"]["datatype"] = "(encode_uint)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["2"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["2"]["description"] = "CMLoadBalancingPriority"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["2"]["datatype"] = "(encode_uint)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["3"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["3"]["description"] = "CMLoadBalancingGroupID"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["3"]["datatype"] = "(encode_uint)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["4"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["4"]["description"] = "CMRangingClassIDExtension"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["4"]["datatype"] = "(encode_ushort)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["description"] = "L2VPNEncoding"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["1"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["1"]["description"] = "VPNIdentifier"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["description"] = "NSIEncapsulation"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["1"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["1"]["description"] = "ServiceMultiplexingValueOther"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["1"]["datatype"] = "(encode_lenzero)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["2"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["2"]["description"] = "NSIEncapsulationSingleQTag"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["2"]["datatype"] = "(encode_ushort)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["3"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["3"]["description"] = "NSIEncapsulationDualQTag"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["3"]["datatype"] = "(encode_dual_qtag)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["description"] = "ServiceMultiplexingValueMPLSPW"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["1"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["1"]["description"] = "MPLSPseudowireID"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["1"]["datatype"] = "(encode_uint)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["2"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["2"]["description"] = "MPLSPeerIpAddress"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["2"]["datatype"] = "(encode_char_ip_ip6)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["3"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["3"]["description"] = "MPLSPseudowireType"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["3"]["datatype"] = "(encode_uchar)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["4"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["4"]["description"] = "MPLSBackupPseudowireID"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["4"]["datatype"] = "(encode_uint)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["5"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["5"]["description"] = "MPLSBackupPeerIpAddress"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["5"]["datatype"] = "(encode_char_ip_ip6)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["5"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["5"]["description"] = "ServiceMultiplexingValueL2TPv3Peer"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["5"]["datatype"] = "(encode_char_ip_ip6)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["description"] = "IEEE8021ahEncapsulation"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["1"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["1"]["description"] = "ITCIEncapsulation"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["2"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["2"]["description"] = "BDAEncapsulation"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["3"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["3"]["description"] = "BTCIEncapsulation"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["4"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["4"]["description"] = "ITPIDEncapsulation"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["5"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["5"]["description"] = "IPCPEncapsulation"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["5"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["6"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["6"]["description"] = "IDEIEncapsulation"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["6"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["7"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["7"]["description"] = "IUCAEncapsulation"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["7"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["8"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["8"]["description"] = "ISIDEncapsulation"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["8"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["9"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["9"]["description"] = "BTPIDEncapsulation"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["9"]["hex"] = "9"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["9"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["9"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["10"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["10"]["description"] = "BPCPEncapsulation"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["10"]["hex"] = "a"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["10"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["11"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["11"]["description"] = "BDEIEncapsulation"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["11"]["hex"] = "b"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["11"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["12"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["12"]["description"] = "BVIDEncapsulation"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["12"]["hex"] = "c"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["12"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["8"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["8"]["description"] = "ServiceMultiplexingValueIEEE8021adSTPID"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["8"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["2"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["3"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["3"]["description"] = "eSAFEDHCPSnooping"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["4"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["4"]["description"] = "CMInterfaceMaskCMIMSubtype"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["5"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["5"]["description"] = "AttachmentGroupID"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["5"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["6"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["6"]["description"] = "SourceAttachmentIndividualID"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["6"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["7"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["7"]["description"] = "TargetAttachmentIndividualID"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["7"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["8"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["8"]["description"] = "IngressUserPriority"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["8"]["datatype"] = "(encode_uchar)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["9"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["9"]["description"] = "UserPriorityRange"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["9"]["hex"] = "9"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["9"]["datatype"] = "(encode_char_list)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["9"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["10"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["10"]["description"] = "L2VPNSADescriptorSubtype"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["10"]["hex"] = "a"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["10"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["12"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["12"]["description"] = "PseudowireType"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["12"]["hex"] = "c"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["12"]["datatype"] = "(encode_uchar)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["13"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["13"]["description"] = "L2VPNMode"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["13"]["hex"] = "d"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["13"]["datatype"] = "(encode_uchar)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["13"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["description"] = "TPIDTranslation"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["hex"] = "e"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["1"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["1"]["description"] = "UpstreamTPIDTranslation"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["2"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["2"]["description"] = "DownstreamTPIDTranslation"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["3"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["3"]["description"] = "UpstreamSTPIDTranslation"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["4"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["4"]["description"] = "DownstreamSTPIDTranslation"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["5"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["5"]["description"] = "UpstreamBTPIDTranslation"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["5"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["6"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["6"]["description"] = "DownstreamBTPIDTranslation"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["6"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["7"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["7"]["description"] = "UpstreamITPIDTranslation"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["7"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["8"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["8"]["description"] = "DownstreamITPIDTranslation"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["8"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["14"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["description"] = "L2CPProcessing"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["hex"] = "f"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["1"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["1"]["description"] = "L2CPTunnelMode"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["2"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["2"]["description"] = "L2CPDMACAddress"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["2"]["datatype"] = "(encode_ether)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["3"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["3"]["description"] = "L2CPOverwrotingDMACAddress"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["3"]["datatype"] = "(encode_ether)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["15"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["16"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["16"]["description"] = "DACDisableEnableConfiguration"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["16"]["hex"] = "10"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["16"]["datatype"] = "(encode_uchar)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["16"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["18"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["18"]["description"] = "PseudowireClass"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["18"]["hex"] = "12"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["18"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["18"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["description"] = "ServiceDelimiter"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["hex"] = "13"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["1"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["1"]["description"] = "CVIDDelimiter"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["2"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["2"]["description"] = "SVIDDelimiter"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["3"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["3"]["description"] = "ISIDDelimiter"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["4"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["4"]["description"] = "BVIDDelimiter"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["19"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["description"] = "VirtualSwitchInstanceEncoding"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["hex"] = "14"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["1"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["1"]["description"] = "VPLSClass"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["2"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["2"]["description"] = "ETreeRole"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["3"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["3"]["description"] = "ETreeRootVID"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["4"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["4"]["description"] = "ETreeLeafVID"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["20"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["description"] = "BGPAttribute"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["hex"] = "15"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["1"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["1"]["description"] = "BGPVPNID"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["1"]["datatype"] = "(encode_uint)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["2"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["2"]["description"] = "RouteDistinguisher"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["3"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["3"]["description"] = "RouteTargetImport"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["4"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["4"]["description"] = "RouteTargetExport"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["5"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["5"]["description"] = "CEIDVEID"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["5"]["datatype"] = "(encode_ushort)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["21"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["23"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["23"]["description"] = "PseudowireSignaling"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["23"]["hex"] = "17"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["23"]["datatype"] = "(encode_uchar)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["23"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["description"] = "SOAMSubtype"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["hex"] = "18"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["description"] = "MEPConfiguration"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["1"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["1"]["description"] = "MDLevel"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["2"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["2"]["description"] = "MDName"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["2"]["datatype"] = "(encode_string)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["3"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["3"]["description"] = "MAName"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["3"]["datatype"] = "(encode_string)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["4"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["4"]["description"] = "MEPID"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["4"]["datatype"] = "(encode_ushort)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["1"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["description"] = "RemoteMEPConfiguration"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["1"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["1"]["description"] = "RemoteMDLevel"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["2"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["2"]["description"] = "RemoteMDName"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["2"]["datatype"] = "(encode_string)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["3"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["3"]["description"] = "RemoteMAName"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["3"]["datatype"] = "(encode_string)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["4"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["4"]["description"] = "RemoteMEPID"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["4"]["datatype"] = "(encode_ushort)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["description"] = "FaultManagementConfiguration"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["1"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["1"]["description"] = "ContinuityCheckMessages"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["2"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["2"]["description"] = "LoopbackFunction"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["3"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["3"]["description"] = "LinktraceFunction"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["3"]["datatype"] = "(encode_uchar)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["3"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["description"] = "PerformanceManagementConfiguration"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["description"] = "FrameDelayMeasurement"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["1"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["1"]["description"] = "FrameDelayMeasurementEnable"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["2"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["2"]["description"] = "FrameDelayMeasurementOneWayTwoWay"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["3"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["3"]["description"] = "FrameDelayMeasurementTransmissionPeriodicity"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["3"]["datatype"] = "(encode_ushort)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["1"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["description"] = "FrameLossMeasurement"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["1"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["1"]["description"] = "FrameLossMeasurementEnable"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["2"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["2"]["description"] = "FrameLossMeasurementTransmissionPeriodicity"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["24"]["subTlvs"]["4"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["26"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["26"]["description"] = "L2VPNDSID"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["26"]["hex"] = "1a"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["26"]["datatype"] = "(encode_uint24)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["26"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["description"] = "VendorSpecificL2VPNSubtype"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["hex"] = "2b"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["subTlvs"]["8"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["subTlvs"]["8"]["description"] = "VendorIdentifier"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["subTlvs"]["8"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["5"]["subTlvs"]["43"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["6"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["6"]["description"] = "ExtendedCMTSMICConfigurationSetting"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["6"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["1"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["1"]["description"] = "ExtendedCMTSMICHMACtype"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["2"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["2"]["description"] = "ExtendedCMTSMICBitmap"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["3"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["3"]["description"] = "ExplicitExtendedCMTSMICDigest"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["6"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["7"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["7"]["description"] = "SAVAuthorizationEncoding"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["7"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["1"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["1"]["description"] = "SAVGroupName"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["1"]["datatype"] = "(encode_string)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["description"] = "SAVStaticPrefixRule"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["1"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["1"]["description"] = "SAVStaticPrefixAddress"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["1"]["datatype"] = "(encode_ip_ip6)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["2"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["2"]["description"] = "SAVStaticPrefixLength"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["8"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["8"]["description"] = "VendorIdentifier"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["8"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["9"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["9"]["description"] = "CMAttributeMasks"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["9"]["hex"] = "9"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["9"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["1"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["1"]["description"] = "CMDownstreamRequiredAttributeMask"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["2"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["2"]["description"] = "CMDownstreamForbiddenAttributeMask"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["3"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["3"]["description"] = "CMUpstreamRequiredAttributeMask"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["4"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["4"]["description"] = "CMUpstreamForbiddenAttributeMask"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["4"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["9"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["description"] = "IPMulticastJoinAuthorization"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["hex"] = "a"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["1"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["1"]["description"] = "IPMulticastProfileName"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["1"]["datatype"] = "(encode_string)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["description"] = "IPMulticastJoinAuthStaticSessionRule"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["1"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["1"]["description"] = "MulticastRulePriority"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["2"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["2"]["description"] = "AuthorizationAction"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["3"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["3"]["description"] = "SourcePrefixAddress"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["3"]["datatype"] = "(encode_ip_ip6)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["4"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["4"]["description"] = "SourcePrefixLength"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["4"]["datatype"] = "(encode_uchar)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["5"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["5"]["description"] = "GroupPrefixAddress"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["5"]["datatype"] = "(encode_ip_ip6)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["6"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["6"]["description"] = "GroupPrefixLength"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["6"]["datatype"] = "(encode_uchar)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["3"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["3"]["description"] = "MaximumMulticastSessions"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["3"]["datatype"] = "(encode_ushort)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["10"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["11"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["11"]["description"] = "ServiceTypeIdentifier"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["11"]["hex"] = "b"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["11"]["datatype"] = "(encode_string)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"]["description"] = "DEMARCAutoConfiguration"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"]["hex"] = "c"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["1"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["1"]["description"] = "DACDisableEnableConfig"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["2"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["2"]["description"] = "CMIMEncoding"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["3"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["3"]["description"] = "UpstreamServiceClassName"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["3"]["datatype"] = "(encode_strzero)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["4"] = {}
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["4"]["description"] = "DownstreamServiceClassName"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["4"]["datatype"] = "(encode_strzero)"
DocsisTlvs["60"]["subTlvs"]["43"]["subTlvs"]["12"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["61"] = {}
DocsisTlvs["61"]["description"] = "SubMgmtCPEIPv6PrefixList"
DocsisTlvs["61"]["hex"] = "3d"
DocsisTlvs["61"]["datatype"] = "(encode_ip6_prefix_list)"
DocsisTlvs["61"]["subTlvs"] = {}

DocsisTlvs["62"] = {}
DocsisTlvs["62"]["description"] = "UpstreamDropClassifierGroupID"
DocsisTlvs["62"]["hex"] = "3e"
DocsisTlvs["62"]["datatype"] = "(encode_char_list)"
DocsisTlvs["62"]["subTlvs"] = {}

DocsisTlvs["63"] = {}
DocsisTlvs["63"]["description"] = "SubMgmtControl6"
DocsisTlvs["63"]["hex"] = "3f"
DocsisTlvs["63"]["datatype"] = "(encode_ushort)"
DocsisTlvs["63"]["subTlvs"] = {}

DocsisTlvs["64"] = {}
DocsisTlvs["64"]["description"] = "CMTSStaticMulticastSessionEncodings"
DocsisTlvs["64"]["hex"] = "40"
DocsisTlvs["64"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["64"]["subTlvs"] = {}

DocsisTlvs["64"]["subTlvs"]["1"] = {}
DocsisTlvs["64"]["subTlvs"]["1"]["description"] = "CMTSStaticMulticastSessionGroup"
DocsisTlvs["64"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["64"]["subTlvs"]["1"]["datatype"] = "(encode_ip_ip6)"
DocsisTlvs["64"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["64"]["subTlvs"]["2"] = {}
DocsisTlvs["64"]["subTlvs"]["2"]["description"] = "CMTSStaticMulticastSessionSource"
DocsisTlvs["64"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["64"]["subTlvs"]["2"]["datatype"] = "(encode_ip_ip6)"
DocsisTlvs["64"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["64"]["subTlvs"]["3"] = {}
DocsisTlvs["64"]["subTlvs"]["3"]["description"] = "CMTSStaticMulticastSessionCMIM"
DocsisTlvs["64"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["64"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["64"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["65"] = {}
DocsisTlvs["65"]["description"] = "L2VPNMACAgingEncoding"
DocsisTlvs["65"]["hex"] = "41"
DocsisTlvs["65"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["65"]["subTlvs"] = {}

DocsisTlvs["65"]["subTlvs"]["1"] = {}
DocsisTlvs["65"]["subTlvs"]["1"]["description"] = "L2VPNMACAgingMode"
DocsisTlvs["65"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["65"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["65"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["66"] = {}
DocsisTlvs["66"]["description"] = "ManagementEventControl"
DocsisTlvs["66"]["hex"] = "42"
DocsisTlvs["66"]["datatype"] = "(encode_uint)"
DocsisTlvs["66"]["subTlvs"] = {}

DocsisTlvs["67"] = {}
DocsisTlvs["67"]["description"] = "SubscriberManagementCPEIPv6Table"
DocsisTlvs["67"]["hex"] = "43"
DocsisTlvs["67"]["datatype"] = "(encode_ip6_list)"
DocsisTlvs["67"]["subTlvs"] = {}

DocsisTlvs["68"] = {}
DocsisTlvs["68"]["description"] = "DefaultUpstreamTargetBuffer"
DocsisTlvs["68"]["hex"] = "44"
DocsisTlvs["68"]["datatype"] = "(encode_ushort)"
DocsisTlvs["68"]["subTlvs"] = {}

DocsisTlvs["69"] = {}
DocsisTlvs["69"]["description"] = "MACAddressLearningControlEncoding"
DocsisTlvs["69"]["hex"] = "45"
DocsisTlvs["69"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["69"]["subTlvs"] = {}

DocsisTlvs["69"]["subTlvs"]["1"] = {}
DocsisTlvs["69"]["subTlvs"]["1"]["description"] = "MACAddressLearningControl"
DocsisTlvs["69"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["69"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["69"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["69"]["subTlvs"]["2"] = {}
DocsisTlvs["69"]["subTlvs"]["2"]["description"] = "MACAddressLearningHoldoffTimer"
DocsisTlvs["69"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["69"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["69"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["70"] = {}
DocsisTlvs["70"]["description"] = "UpstreamAggregateServiceFlow"
DocsisTlvs["70"]["hex"] = "46"
DocsisTlvs["70"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["70"]["subTlvs"] = {}

DocsisTlvs["70"]["subTlvs"]["1"] = {}
DocsisTlvs["70"]["subTlvs"]["1"]["description"] = "UpstreamServiceFlowReference"
DocsisTlvs["70"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["70"]["subTlvs"]["1"]["datatype"] = "(encode_ushort)"
DocsisTlvs["70"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["70"]["subTlvs"]["36"] = {}
DocsisTlvs["70"]["subTlvs"]["36"]["description"] = "UpstreamAggregateServiceFlowReference"
DocsisTlvs["70"]["subTlvs"]["36"]["hex"] = "24"
DocsisTlvs["70"]["subTlvs"]["36"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["70"]["subTlvs"]["36"]["subTlvs"] = {}

DocsisTlvs["70"]["subTlvs"]["37"] = {}
DocsisTlvs["70"]["subTlvs"]["37"]["description"] = "UpstreamMESPReference"
DocsisTlvs["70"]["subTlvs"]["37"]["hex"] = "25"
DocsisTlvs["70"]["subTlvs"]["37"]["datatype"] = "(encode_ushort)"
DocsisTlvs["70"]["subTlvs"]["37"]["subTlvs"] = {}

DocsisTlvs["71"] = {}
DocsisTlvs["71"]["description"] = "DownstreamAggregateServiceFlow"
DocsisTlvs["71"]["hex"] = "47"
DocsisTlvs["71"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["71"]["subTlvs"] = {}

DocsisTlvs["71"]["subTlvs"]["1"] = {}
DocsisTlvs["71"]["subTlvs"]["1"]["description"] = "DownstreamServiceFlowReference"
DocsisTlvs["71"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["71"]["subTlvs"]["1"]["datatype"] = "(encode_ushort)"
DocsisTlvs["71"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["71"]["subTlvs"]["36"] = {}
DocsisTlvs["71"]["subTlvs"]["36"]["description"] = "DownstreamAggregateServiceFlowReference"
DocsisTlvs["71"]["subTlvs"]["36"]["hex"] = "24"
DocsisTlvs["71"]["subTlvs"]["36"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["71"]["subTlvs"]["36"]["subTlvs"] = {}

DocsisTlvs["71"]["subTlvs"]["37"] = {}
DocsisTlvs["71"]["subTlvs"]["37"]["description"] = "DownstreamMESPReference"
DocsisTlvs["71"]["subTlvs"]["37"]["hex"] = "25"
DocsisTlvs["71"]["subTlvs"]["37"]["datatype"] = "(encode_ushort)"
DocsisTlvs["71"]["subTlvs"]["37"]["subTlvs"] = {}

DocsisTlvs["72"] = {}
DocsisTlvs["72"]["description"] = "MetroEthernetServiceProfile"
DocsisTlvs["72"]["hex"] = "48"
DocsisTlvs["72"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["72"]["subTlvs"] = {}

DocsisTlvs["72"]["subTlvs"]["1"] = {}
DocsisTlvs["72"]["subTlvs"]["1"]["description"] = "MESPReference"
DocsisTlvs["72"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["72"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["72"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["72"]["subTlvs"]["2"] = {}
DocsisTlvs["72"]["subTlvs"]["2"]["description"] = "MESPBandwidthProfile"
DocsisTlvs["72"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["72"]["subTlvs"]["2"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["1"] = {}
DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["1"]["description"] = "CIR"
DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["1"]["datatype"] = "(encode_uint)"
DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["2"] = {}
DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["2"]["description"] = "CBR"
DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["2"]["datatype"] = "(encode_uint)"
DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["3"] = {}
DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["3"]["description"] = "EIR"
DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["3"]["datatype"] = "(encode_uint)"
DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["4"] = {}
DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["4"]["description"] = "EBS"
DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["4"]["datatype"] = "(encode_uint)"
DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["5"] = {}
DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["5"]["description"] = "CouplingFlag"
DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["5"]["datatype"] = "(encode_uchar)"
DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["6"] = {}
DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["6"]["description"] = "ColorMode"
DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["6"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["1"] = {}
DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["1"]["description"] = "ColorIdentificationField"
DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["2"] = {}
DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["2"]["description"] = "ColorIdentificationFieldValue"
DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["7"] = {}
DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["7"]["description"] = "ColorMarking"
DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["7"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["7"]["subTlvs"]["1"] = {}
DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["7"]["subTlvs"]["1"]["description"] = "ColorMarkingField"
DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["7"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["7"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["7"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["7"]["subTlvs"]["2"] = {}
DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["7"]["subTlvs"]["2"]["description"] = "ColorMarkingFieldValue"
DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["7"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["7"]["subTlvs"]["2"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["72"]["subTlvs"]["2"]["subTlvs"]["7"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["72"]["subTlvs"]["3"] = {}
DocsisTlvs["72"]["subTlvs"]["3"]["description"] = "MESPName"
DocsisTlvs["72"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["72"]["subTlvs"]["3"]["datatype"] = "(encode_strzero)"
DocsisTlvs["72"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["73"] = {}
DocsisTlvs["73"]["description"] = "NetworkTimingProfile"
DocsisTlvs["73"]["hex"] = "49"
DocsisTlvs["73"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["73"]["subTlvs"] = {}

DocsisTlvs["73"]["subTlvs"]["1"] = {}
DocsisTlvs["73"]["subTlvs"]["1"]["description"] = "NetworkTimingProfileReference"
DocsisTlvs["73"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["73"]["subTlvs"]["1"]["datatype"] = "(encode_ushort)"
DocsisTlvs["73"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["73"]["subTlvs"]["2"] = {}
DocsisTlvs["73"]["subTlvs"]["2"]["description"] = "NetworkTimingProfileName"
DocsisTlvs["73"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["73"]["subTlvs"]["2"]["datatype"] = "(encode_strzero)"
DocsisTlvs["73"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["74"] = {}
DocsisTlvs["74"]["description"] = "EnergyManagementParameter"
DocsisTlvs["74"]["hex"] = "4a"
DocsisTlvs["74"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["74"]["subTlvs"] = {}

DocsisTlvs["74"]["subTlvs"]["1"] = {}
DocsisTlvs["74"]["subTlvs"]["1"]["description"] = "EnergyManagementFeatureControl"
DocsisTlvs["74"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["74"]["subTlvs"]["1"]["datatype"] = "(encode_uint)"
DocsisTlvs["74"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["74"]["subTlvs"]["2"] = {}
DocsisTlvs["74"]["subTlvs"]["2"]["description"] = "EnergyManagement1x1Mode"
DocsisTlvs["74"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["74"]["subTlvs"]["2"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["1"] = {}
DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["1"]["description"] = "DownstreamActivityDetectionParameters"
DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["1"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"]["1"] = {}
DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"]["1"]["description"] = "DownstreamEntryBitrateThreshold"
DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"]["1"]["datatype"] = "(encode_uint)"
DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"]["2"] = {}
DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"]["2"]["description"] = "DownstreamEntryTimeThreshold"
DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"]["2"]["datatype"] = "(encode_ushort)"
DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"]["3"] = {}
DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"]["3"]["description"] = "DownstreamExitBitrateThreshold"
DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"]["3"]["datatype"] = "(encode_uint)"
DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"]["4"] = {}
DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"]["4"]["description"] = "DownstreamExitTimeThreshold"
DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"]["4"]["datatype"] = "(encode_ushort)"
DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["2"] = {}
DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["2"]["description"] = "UpstreamActivityDetectionParameters"
DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["2"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"]["1"] = {}
DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"]["1"]["description"] = "UpstreamEntryBitrateThreshold"
DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"]["1"]["datatype"] = "(encode_uint)"
DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"]["2"] = {}
DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"]["2"]["description"] = "UpstreamEntryTimeThreshold"
DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"]["2"]["datatype"] = "(encode_ushort)"
DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"]["3"] = {}
DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"]["3"]["description"] = "UpstreamExitBitrateThreshold"
DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"]["3"]["datatype"] = "(encode_uint)"
DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"]["4"] = {}
DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"]["4"]["description"] = "UpstreamExitTimeThreshold"
DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"]["4"]["datatype"] = "(encode_ushort)"
DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["3"] = {}
DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["3"]["description"] = "EnergyManagementCyclePeriod"
DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["3"]["datatype"] = "(encode_ushort)"
DocsisTlvs["74"]["subTlvs"]["2"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["75"] = {}
DocsisTlvs["75"]["description"] = "EnergyManagement1x1ModeIndicator"
DocsisTlvs["75"]["hex"] = "4b"
DocsisTlvs["75"]["datatype"] = "(encode_uchar)"
DocsisTlvs["75"]["subTlvs"] = {}

DocsisTlvs["76"] = {}
DocsisTlvs["76"]["description"] = "CMUpstreamAQMDisable"
DocsisTlvs["76"]["hex"] = "4c"
DocsisTlvs["76"]["datatype"] = "(encode_uchar)"
DocsisTlvs["76"]["subTlvs"] = {}

DocsisTlvs["79"] = {}
DocsisTlvs["79"]["description"] = "UNIControlEncodings"
DocsisTlvs["79"]["hex"] = "4f"
DocsisTlvs["79"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["79"]["subTlvs"] = {}

DocsisTlvs["79"]["subTlvs"]["1"] = {}
DocsisTlvs["79"]["subTlvs"]["1"]["description"] = "ContextCMIM"
DocsisTlvs["79"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["79"]["subTlvs"]["1"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["79"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["79"]["subTlvs"]["2"] = {}
DocsisTlvs["79"]["subTlvs"]["2"]["description"] = "UNIAdminStatus"
DocsisTlvs["79"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["79"]["subTlvs"]["2"]["datatype"] = "(encode_uchar)"
DocsisTlvs["79"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["79"]["subTlvs"]["3"] = {}
DocsisTlvs["79"]["subTlvs"]["3"]["description"] = "UNIAutoNegotiationStatus"
DocsisTlvs["79"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["79"]["subTlvs"]["3"]["datatype"] = "(encode_uchar)"
DocsisTlvs["79"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["79"]["subTlvs"]["4"] = {}
DocsisTlvs["79"]["subTlvs"]["4"]["description"] = "UNIOperatingSpeed"
DocsisTlvs["79"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["79"]["subTlvs"]["4"]["datatype"] = "(encode_uchar)"
DocsisTlvs["79"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["79"]["subTlvs"]["5"] = {}
DocsisTlvs["79"]["subTlvs"]["5"]["description"] = "UNIDuplex"
DocsisTlvs["79"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["79"]["subTlvs"]["5"]["datatype"] = "(encode_uchar)"
DocsisTlvs["79"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["79"]["subTlvs"]["6"] = {}
DocsisTlvs["79"]["subTlvs"]["6"]["description"] = "EEEStatus"
DocsisTlvs["79"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["79"]["subTlvs"]["6"]["datatype"] = "(encode_uchar)"
DocsisTlvs["79"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["79"]["subTlvs"]["7"] = {}
DocsisTlvs["79"]["subTlvs"]["7"]["description"] = "MaximumFrameSize"
DocsisTlvs["79"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["79"]["subTlvs"]["7"]["datatype"] = "(encode_ushort)"
DocsisTlvs["79"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["79"]["subTlvs"]["8"] = {}
DocsisTlvs["79"]["subTlvs"]["8"]["description"] = "PowerOverEthernetStatus"
DocsisTlvs["79"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["79"]["subTlvs"]["8"]["datatype"] = "(encode_uchar)"
DocsisTlvs["79"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["79"]["subTlvs"]["9"] = {}
DocsisTlvs["79"]["subTlvs"]["9"]["description"] = "MediaType"
DocsisTlvs["79"]["subTlvs"]["9"]["hex"] = "9"
DocsisTlvs["79"]["subTlvs"]["9"]["datatype"] = "(encode_uchar)"
DocsisTlvs["79"]["subTlvs"]["9"]["subTlvs"] = {}

DocsisTlvs["81"] = {}
DocsisTlvs["81"]["description"] = "ManufacturerCVCChain"
DocsisTlvs["81"]["hex"] = "51"
DocsisTlvs["81"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["81"]["subTlvs"] = {}

DocsisTlvs["82"] = {}
DocsisTlvs["82"]["description"] = "CoSignerCVCChain"
DocsisTlvs["82"]["hex"] = "52"
DocsisTlvs["82"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["82"]["subTlvs"] = {}

DocsisTlvs["202"] = {}
DocsisTlvs["202"]["description"] = "eRouter"
DocsisTlvs["202"]["hex"] = "ca"
DocsisTlvs["202"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["202"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["1"] = {}
DocsisTlvs["202"]["subTlvs"]["1"]["description"] = "InitializationMode"
DocsisTlvs["202"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["202"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["202"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["2"] = {}
DocsisTlvs["202"]["subTlvs"]["2"]["description"] = "TR69ManagementServer"
DocsisTlvs["202"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["202"]["subTlvs"]["2"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["202"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["2"]["subTlvs"]["1"] = {}
DocsisTlvs["202"]["subTlvs"]["2"]["subTlvs"]["1"]["description"] = "EnableCWMP"
DocsisTlvs["202"]["subTlvs"]["2"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["202"]["subTlvs"]["2"]["subTlvs"]["1"]["datatype"] = "(encode_uchar)"
DocsisTlvs["202"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["2"]["subTlvs"]["2"] = {}
DocsisTlvs["202"]["subTlvs"]["2"]["subTlvs"]["2"]["description"] = "URL"
DocsisTlvs["202"]["subTlvs"]["2"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["202"]["subTlvs"]["2"]["subTlvs"]["2"]["datatype"] = "(encode_string)"
DocsisTlvs["202"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["2"]["subTlvs"]["3"] = {}
DocsisTlvs["202"]["subTlvs"]["2"]["subTlvs"]["3"]["description"] = "Username"
DocsisTlvs["202"]["subTlvs"]["2"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["202"]["subTlvs"]["2"]["subTlvs"]["3"]["datatype"] = "(encode_string)"
DocsisTlvs["202"]["subTlvs"]["2"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["2"]["subTlvs"]["4"] = {}
DocsisTlvs["202"]["subTlvs"]["2"]["subTlvs"]["4"]["description"] = "Password"
DocsisTlvs["202"]["subTlvs"]["2"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["202"]["subTlvs"]["2"]["subTlvs"]["4"]["datatype"] = "(encode_string)"
DocsisTlvs["202"]["subTlvs"]["2"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["2"]["subTlvs"]["5"] = {}
DocsisTlvs["202"]["subTlvs"]["2"]["subTlvs"]["5"]["description"] = "ConnectionRequestUsername"
DocsisTlvs["202"]["subTlvs"]["2"]["subTlvs"]["5"]["hex"] = "5"
DocsisTlvs["202"]["subTlvs"]["2"]["subTlvs"]["5"]["datatype"] = "(encode_string)"
DocsisTlvs["202"]["subTlvs"]["2"]["subTlvs"]["5"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["2"]["subTlvs"]["6"] = {}
DocsisTlvs["202"]["subTlvs"]["2"]["subTlvs"]["6"]["description"] = "ConnectionRequestPassword"
DocsisTlvs["202"]["subTlvs"]["2"]["subTlvs"]["6"]["hex"] = "6"
DocsisTlvs["202"]["subTlvs"]["2"]["subTlvs"]["6"]["datatype"] = "(encode_string)"
DocsisTlvs["202"]["subTlvs"]["2"]["subTlvs"]["6"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["2"]["subTlvs"]["7"] = {}
DocsisTlvs["202"]["subTlvs"]["2"]["subTlvs"]["7"]["description"] = "ACSOverride"
DocsisTlvs["202"]["subTlvs"]["2"]["subTlvs"]["7"]["hex"] = "7"
DocsisTlvs["202"]["subTlvs"]["2"]["subTlvs"]["7"]["datatype"] = "(encode_uchar)"
DocsisTlvs["202"]["subTlvs"]["2"]["subTlvs"]["7"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["3"] = {}
DocsisTlvs["202"]["subTlvs"]["3"]["description"] = "InitializationModeOverride"
DocsisTlvs["202"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["202"]["subTlvs"]["3"]["datatype"] = "(encode_uchar)"
DocsisTlvs["202"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["10"] = {}
DocsisTlvs["202"]["subTlvs"]["10"]["description"] = "RATransmissionInterval"
DocsisTlvs["202"]["subTlvs"]["10"]["hex"] = "a"
DocsisTlvs["202"]["subTlvs"]["10"]["datatype"] = "(encode_ushort)"
DocsisTlvs["202"]["subTlvs"]["10"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["11"] = {}
DocsisTlvs["202"]["subTlvs"]["11"]["description"] = "SnmpMibObject"
DocsisTlvs["202"]["subTlvs"]["11"]["hex"] = "b"
DocsisTlvs["202"]["subTlvs"]["11"]["datatype"] = "(decode_snmp_object)"
DocsisTlvs["202"]["subTlvs"]["11"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["42"] = {}
DocsisTlvs["202"]["subTlvs"]["42"]["description"] = "TopologyModeEncoding"
DocsisTlvs["202"]["subTlvs"]["42"]["hex"] = "2a"
DocsisTlvs["202"]["subTlvs"]["42"]["datatype"] = "(encode_uchar)"
DocsisTlvs["202"]["subTlvs"]["42"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["43"] = {}
DocsisTlvs["202"]["subTlvs"]["43"]["description"] = "VendorSpecific"
DocsisTlvs["202"]["subTlvs"]["43"]["hex"] = "2b"
DocsisTlvs["202"]["subTlvs"]["43"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["202"]["subTlvs"]["43"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["43"]["subTlvs"]["8"] = {}
DocsisTlvs["202"]["subTlvs"]["43"]["subTlvs"]["8"]["description"] = "VendorIdentifier"
DocsisTlvs["202"]["subTlvs"]["43"]["subTlvs"]["8"]["hex"] = "8"
DocsisTlvs["202"]["subTlvs"]["43"]["subTlvs"]["8"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["202"]["subTlvs"]["43"]["subTlvs"]["8"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["53"] = {}
DocsisTlvs["202"]["subTlvs"]["53"]["description"] = "SNMPv1v2cCoexistenceConfig"
DocsisTlvs["202"]["subTlvs"]["53"]["hex"] = "35"
DocsisTlvs["202"]["subTlvs"]["53"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["1"] = {}
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["1"]["description"] = "SNMPv1v2cCommunityName"
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["1"]["datatype"] = "(encode_string)"
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["2"] = {}
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["2"]["description"] = "SNMPv1v2cTransportAddressAccess"
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["2"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["2"]["subTlvs"]["1"] = {}
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["2"]["subTlvs"]["1"]["description"] = "SNMPv1v2cTransportAddress"
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["2"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["2"]["subTlvs"]["1"]["datatype"] = "(encode_ip_ip6_port)"
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["2"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["2"]["subTlvs"]["2"] = {}
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["2"]["subTlvs"]["2"]["description"] = "SNMPv1v2cTransportAddressMask"
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["2"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["2"]["subTlvs"]["2"]["datatype"] = "(encode_ip_ip6_port)"
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["2"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["3"] = {}
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["3"]["description"] = "SNMPv1v2cAccessViewType"
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["3"]["datatype"] = "(encode_uchar)"
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["4"] = {}
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["4"]["description"] = "SNMPv1v2cAccessViewName"
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["4"]["datatype"] = "(encode_string)"
DocsisTlvs["202"]["subTlvs"]["53"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["54"] = {}
DocsisTlvs["202"]["subTlvs"]["54"]["description"] = "SNMPv3AccessViewConfiguration"
DocsisTlvs["202"]["subTlvs"]["54"]["hex"] = "36"
DocsisTlvs["202"]["subTlvs"]["54"]["datatype"] = "(decode_aggregate)"
DocsisTlvs["202"]["subTlvs"]["54"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["54"]["subTlvs"]["1"] = {}
DocsisTlvs["202"]["subTlvs"]["54"]["subTlvs"]["1"]["description"] = "SNMPv3AccessViewName"
DocsisTlvs["202"]["subTlvs"]["54"]["subTlvs"]["1"]["hex"] = "1"
DocsisTlvs["202"]["subTlvs"]["54"]["subTlvs"]["1"]["datatype"] = "(encode_string)"
DocsisTlvs["202"]["subTlvs"]["54"]["subTlvs"]["1"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["54"]["subTlvs"]["2"] = {}
DocsisTlvs["202"]["subTlvs"]["54"]["subTlvs"]["2"]["description"] = "SNMPv3AccessViewSubtree"
DocsisTlvs["202"]["subTlvs"]["54"]["subTlvs"]["2"]["hex"] = "2"
DocsisTlvs["202"]["subTlvs"]["54"]["subTlvs"]["2"]["datatype"] = "(encode_oid)"
DocsisTlvs["202"]["subTlvs"]["54"]["subTlvs"]["2"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["54"]["subTlvs"]["3"] = {}
DocsisTlvs["202"]["subTlvs"]["54"]["subTlvs"]["3"]["description"] = "SNMPv3AccessViewMask"
DocsisTlvs["202"]["subTlvs"]["54"]["subTlvs"]["3"]["hex"] = "3"
DocsisTlvs["202"]["subTlvs"]["54"]["subTlvs"]["3"]["datatype"] = "(encode_hexstr)"
DocsisTlvs["202"]["subTlvs"]["54"]["subTlvs"]["3"]["subTlvs"] = {}

DocsisTlvs["202"]["subTlvs"]["54"]["subTlvs"]["4"] = {}
DocsisTlvs["202"]["subTlvs"]["54"]["subTlvs"]["4"]["description"] = "SNMPv3AccessViewType"
DocsisTlvs["202"]["subTlvs"]["54"]["subTlvs"]["4"]["hex"] = "4"
DocsisTlvs["202"]["subTlvs"]["54"]["subTlvs"]["4"]["datatype"] = "(encode_uchar)"
DocsisTlvs["202"]["subTlvs"]["54"]["subTlvs"]["4"]["subTlvs"] = {}

DocsisTlvs["998"] = {}
DocsisTlvs["998"]["description"] = "GenericTLV"
DocsisTlvs["998"]["hex"] = "3e6"
DocsisTlvs["998"]["datatype"] = "(decode_special)"
DocsisTlvs["998"]["subTlvs"] = {}

DocsisTlvs["254"] = {}
DocsisTlvs["254"]["description"] = "MtaConfigDelimiter"
DocsisTlvs["254"]["hex"] = "fe"
DocsisTlvs["254"]["datatype"] = "(encode_uchar)"
DocsisTlvs["254"]["subTlvs"] = {}

DocsisTlvs[""] = {}
DocsisTlvs[""]["description"] = "/*EndOfDataMkr*/"
DocsisTlvs[""]["datatype"] = "(decode_special)"
DocsisTlvs[""]["subTlvs"] = {}

