DOCSIS40 = {}

DOCSIS40["00"] = {}
DOCSIS40["00"]["description"] = "Pad"
DOCSIS40["00"]["note"] = "This has no length or value fields and is only used following the end of data marker to pad the file to an integral number of 32-bit words."
DOCSIS40["00"]["datatype"] = "special"
DOCSIS40["00"]["subTlvs"] = {}

DOCSIS40["01"] = {}
DOCSIS40["01"]["description"] = "DownstreamFrequency"
DOCSIS40["01"]["note"] = "Valid Range: For SC-QAM channels, the receive frequency needs to be a multiple of 62500 Hz. For OFDM channels, the center frequency of the lowest subcarrier of the 6 MHz encompassed spectrum containing the PLC at its center can be located on any one MHz boundary."
DOCSIS40["01"]["datatype"] = "uint"
DOCSIS40["01"]["subTlvs"] = {}

DOCSIS40["02"] = {}
DOCSIS40["02"]["description"] = "UpstreamChannelId"
DOCSIS40["02"]["note"] = "The upstream channel ID which the CM MUST use. The CM MUST listen on the defined downstream channel until an upstream channel description message with this ID is found. It is an override for the channel selected during initialization."
DOCSIS40["02"]["datatype"] = "uchar"
DOCSIS40["02"]["subTlvs"] = {}

DOCSIS40["03"] = {}
DOCSIS40["03"]["description"] = "Network Access Control Object"
DOCSIS40["03"]["note"] = "Must be 0 or 1"
DOCSIS40["03"]["datatype"] = "uchar"
DOCSIS40["03"]["subTlvs"] = {}

DOCSIS40["04"] = {}
DOCSIS40["04"]["description"] = "ClassOfService"
DOCSIS40["04"]["note"] = "DOCSIS 1.0...depreciated...don't use this!"
DOCSIS40["04"]["datatype"] = "aggregate"
DOCSIS40["04"]["subTlvs"] = {}

DOCSIS40["05"] = {}
DOCSIS40["05"]["description"] = "Modem Capabilities"
DOCSIS40["05"]["note"] = "Not in the cfg file, this comes from the modem."
DOCSIS40["05"]["datatype"] = "unknown"
DOCSIS40["05"]["subTlvs"] = {}

DOCSIS40["06"] = {}
DOCSIS40["06"]["description"] = "CM Message Integrity Check (MIC)"
DOCSIS40["06"]["note"] = ""
DOCSIS40["06"]["datatype"] = "md5"
DOCSIS40["06"]["subTlvs"] = {}

DOCSIS40["07"] = {}
DOCSIS40["07"]["description"] = "CMTS Message Integrity Check (MIC)"
DOCSIS40["07"]["note"] = ""
DOCSIS40["07"]["datatype"] = "md5"
DOCSIS40["07"]["subTlvs"] = {}

DOCSIS40["08"] = {}
DOCSIS40["08"]["description"] = "Vendor ID Encoding"
DOCSIS40["08"]["note"] = ""
DOCSIS40["08"]["datatype"] = "unknown"
DOCSIS40["08"]["subTlvs"] = {}