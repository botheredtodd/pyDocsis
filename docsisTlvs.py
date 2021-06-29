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
DocsisTlvs["06"]["description"] = "/* Pad */"
DocsisTlvs["06"]["hex"] = "06"
DocsisTlvs["06"]["valueType"] = "00"
DocsisTlvs["06"]["subTlvs"] = []

DocsisTlvs["07"] = {}
DocsisTlvs["07"]["description"] = "/* Pad */"
DocsisTlvs["07"]["hex"] = "07"
DocsisTlvs["07"]["valueType"] = "00"
DocsisTlvs["07"]["subTlvs"] = []

DocsisTlvs["08"] = {}
DocsisTlvs["08"]["description"] = "/* Pad */"
DocsisTlvs["08"]["hex"] = "08"
DocsisTlvs["08"]["valueType"] = "00"
DocsisTlvs["08"]["subTlvs"] = []

DocsisTlvs["09"] = {}
DocsisTlvs["09"]["description"] = "/* Pad */"
DocsisTlvs["09"]["hex"] = "09"
DocsisTlvs["09"]["valueType"] = "00"
DocsisTlvs["09"]["subTlvs"] = []

DocsisTlvs["10"] = {}
DocsisTlvs["10"]["description"] = "/* Pad */"
DocsisTlvs["10"]["hex"] = "0a"
DocsisTlvs["10"]["valueType"] = "00"
DocsisTlvs["10"]["subTlvs"] = []

DocsisTlvs["11"] = {}
DocsisTlvs["11"]["description"] = "/* Pad */"
DocsisTlvs["11"]["hex"] = "0b"
DocsisTlvs["11"]["valueType"] = "00"
DocsisTlvs["11"]["subTlvs"] = []

DocsisTlvs["12"] = {}
DocsisTlvs["12"]["description"] = "/* Pad */"
DocsisTlvs["12"]["hex"] = "0c"
DocsisTlvs["12"]["valueType"] = "00"
DocsisTlvs["12"]["subTlvs"] = []

DocsisTlvs["13"] = {}
DocsisTlvs["13"]["description"] = "/* Pad */"
DocsisTlvs["13"]["hex"] = "0d"
DocsisTlvs["13"]["valueType"] = "00"
DocsisTlvs["13"]["subTlvs"] = []

DocsisTlvs["14"] = {}
DocsisTlvs["14"]["description"] = "/* Pad */"
DocsisTlvs["14"]["hex"] = "0e"
DocsisTlvs["14"]["valueType"] = "00"
DocsisTlvs["14"]["subTlvs"] = []

DocsisTlvs["15"] = {}
DocsisTlvs["15"]["description"] = "/* Pad */"
DocsisTlvs["15"]["hex"] = "0f"
DocsisTlvs["15"]["valueType"] = "00"
DocsisTlvs["15"]["subTlvs"] = []


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
#todo: continue from here!
d5subs["04"] = {}
d5subs["04"]["description"] = "PriorityUp"
d5subs["04"]["hex"] = "04"
d5subs["04"]["valueType"] = "uchar"
d5subs["04"]["subTlvs"] = []

d5subs["05"] = {}
d5subs["05"]["description"] = "GuaranteedUp"
d5subs["05"]["hex"] = "05"
d5subs["05"]["valueType"] = "uint"
d5subs["05"]["subTlvs"] = []

d5subs["06"] = {}
d5subs["06"]["description"] = "MaxBurstUp"
d5subs["06"]["hex"] = "06"
d5subs["06"]["valueType"] = "ushort"
d5subs["06"]["subTlvs"] = []

d5subs["07"] = {}
d5subs["07"]["description"] = "PrivacyEnable"
d5subs["07"]["hex"] = "07"
d5subs["07"]["valueType"] = "uchar"
d5subs["07"]["subTlvs"] = []

d5subs["08"] = {}
d5subs["08"]["description"] = "ClassID"
d5subs["08"]["hex"] = "01"
d5subs["08"]["valueType"] = "uchar"
d5subs["08"]["subTlvs"] = []

d5subs["09"] = {}
d5subs["09"]["description"] = "MaxRateDown"
d5subs["09"]["hex"] = "02"
d5subs["09"]["valueType"] = "uint"
d5subs["09"]["subTlvs"] = []

d5subs["10"] = {}
d5subs["10"]["description"] = "MaxRateUp"
d5subs["10"]["hex"] = "03"
d5subs["10"]["valueType"] = "uint"
d5subs["10"]["subTlvs"] = []

d5subs["11"] = {}
d5subs["11"]["description"] = "PriorityUp"
d5subs["11"]["hex"] = "04"
d5subs["11"]["valueType"] = "uchar"
d5subs["11"]["subTlvs"] = []

d5subs["12"] = {}
d5subs["12"]["description"] = "GuaranteedUp"
d5subs["12"]["hex"] = "05"
d5subs["12"]["valueType"] = "uint"
d5subs["12"]["subTlvs"] = []

d5subs["13"] = {}
d5subs["13"]["description"] = "MaxBurstUp"
d5subs["13"]["hex"] = "06"
d5subs["13"]["valueType"] = "ushort"
d5subs["13"]["subTlvs"] = []

d5subs["14"] = {}
d5subs["14"]["description"] = "PrivacyEnable"
d5subs["14"]["hex"] = "07"
d5subs["14"]["valueType"] = "uchar"
d5subs["14"]["subTlvs"] = []

d5subs["15"] = {}
d5subs["15"]["description"] = "ClassID"
d5subs["15"]["hex"] = "01"
d5subs["15"]["valueType"] = "uchar"
d5subs["15"]["subTlvs"] = []

d5subs["16"] = {}
d5subs["16"]["description"] = "MaxRateDown"
d5subs["16"]["hex"] = "02"
d5subs["16"]["valueType"] = "uint"
d5subs["16"]["subTlvs"] = []

d5subs["17"] = {}
d5subs["17"]["description"] = "MaxRateUp"
d5subs["17"]["hex"] = "03"
d5subs["17"]["valueType"] = "uint"
d5subs["17"]["subTlvs"] = []

d5subs["18"] = {}
d5subs["18"]["description"] = "PriorityUp"
d5subs["18"]["hex"] = "04"
d5subs["18"]["valueType"] = "uchar"
d5subs["18"]["subTlvs"] = []

d5subs["19"] = {}
d5subs["19"]["description"] = "GuaranteedUp"
d5subs["19"]["hex"] = "05"
d5subs["19"]["valueType"] = "uint"
d5subs["19"]["subTlvs"] = []

d5subs["20"] = {}
d5subs["20"]["description"] = "MaxBurstUp"
d5subs["20"]["hex"] = "06"
d5subs["20"]["valueType"] = "ushort"
d5subs["20"]["subTlvs"] = []

d5subs["21"] = {}
d5subs["21"]["description"] = "PrivacyEnable"
d5subs["21"]["hex"] = "07"
d5subs["21"]["valueType"] = "uchar"
d5subs["21"]["subTlvs"] = []

d5subs["22"] = {}
d5subs["22"]["description"] = "ClassID"
d5subs["22"]["hex"] = "01"
d5subs["22"]["valueType"] = "uchar"
d5subs["22"]["subTlvs"] = []

d5subs["23"] = {}
d5subs["23"]["description"] = "MaxRateDown"
d5subs["23"]["hex"] = "02"
d5subs["23"]["valueType"] = "uint"
d5subs["23"]["subTlvs"] = []

d5subs["24"] = {}
d5subs["24"]["description"] = "MaxRateUp"
d5subs["24"]["hex"] = "03"
d5subs["24"]["valueType"] = "uint"
d5subs["24"]["subTlvs"] = []

d5subs["25"] = {}
d5subs["25"]["description"] = "PriorityUp"
d5subs["25"]["hex"] = "04"
d5subs["25"]["valueType"] = "uchar"
d5subs["25"]["subTlvs"] = []

d5subs["26"] = {}
d5subs["26"]["description"] = "GuaranteedUp"
d5subs["26"]["hex"] = "05"
d5subs["26"]["valueType"] = "uint"
d5subs["26"]["subTlvs"] = []

d5subs["27"] = {}
d5subs["27"]["description"] = "MaxBurstUp"
d5subs["27"]["hex"] = "06"
d5subs["27"]["valueType"] = "ushort"
d5subs["27"]["subTlvs"] = []

d5subs["28"] = {}
d5subs["28"]["description"] = "PrivacyEnable"
d5subs["28"]["hex"] = "07"
d5subs["28"]["valueType"] = "uchar"
d5subs["28"]["subTlvs"] = []

d5subs["29"] = {}
d5subs["29"]["description"] = "ClassID"
d5subs["29"]["hex"] = "01"
d5subs["29"]["valueType"] = "uchar"
d5subs["29"]["subTlvs"] = []

d5subs["30"] = {}
d5subs["30"]["description"] = "MaxRateDown"
d5subs["30"]["hex"] = "02"
d5subs["30"]["valueType"] = "uint"
d5subs["30"]["subTlvs"] = []

d5subs["31"] = {}
d5subs["31"]["description"] = "MaxRateUp"
d5subs["31"]["hex"] = "03"
d5subs["31"]["valueType"] = "uint"
d5subs["31"]["subTlvs"] = []

d5subs["32"] = {}
d5subs["32"]["description"] = "PriorityUp"
d5subs["32"]["hex"] = "04"
d5subs["32"]["valueType"] = "uchar"
d5subs["32"]["subTlvs"] = []

d5subs["33"] = {}
d5subs["33"]["description"] = "GuaranteedUp"
d5subs["33"]["hex"] = "05"
d5subs["33"]["valueType"] = "uint"
d5subs["33"]["subTlvs"] = []

d5subs["34"] = {}
d5subs["34"]["description"] = "MaxBurstUp"
d5subs["34"]["hex"] = "06"
d5subs["34"]["valueType"] = "ushort"
d5subs["34"]["subTlvs"] = []

d5subs["35"] = {}
d5subs["35"]["description"] = "PrivacyEnable"
d5subs["35"]["hex"] = "07"
d5subs["35"]["valueType"] = "uchar"
d5subs["35"]["subTlvs"] = []

d5subs["36"] = {}
d5subs["36"]["description"] = "ClassID"
d5subs["36"]["hex"] = "01"
d5subs["36"]["valueType"] = "uchar"
d5subs["36"]["subTlvs"] = []

d5subs["37"] = {}
d5subs["37"]["description"] = "MaxRateDown"
d5subs["37"]["hex"] = "02"
d5subs["37"]["valueType"] = "uint"
d5subs["37"]["subTlvs"] = []

d5subs["38"] = {}
d5subs["38"]["description"] = "MaxRateUp"
d5subs["38"]["hex"] = "03"
d5subs["38"]["valueType"] = "uint"
d5subs["38"]["subTlvs"] = []

d5subs["39"] = {}
d5subs["39"]["description"] = "PriorityUp"
d5subs["39"]["hex"] = "04"
d5subs["39"]["valueType"] = "uchar"
d5subs["39"]["subTlvs"] = []

d5subs["40"] = {}
d5subs["40"]["description"] = "GuaranteedUp"
d5subs["40"]["hex"] = "05"
d5subs["40"]["valueType"] = "uint"
d5subs["40"]["subTlvs"] = []

d5subs["41"] = {}
d5subs["41"]["description"] = "MaxBurstUp"
d5subs["41"]["hex"] = "06"
d5subs["41"]["valueType"] = "ushort"
d5subs["41"]["subTlvs"] = []

d5subs["42"] = {}
d5subs["42"]["description"] = "PrivacyEnable"
d5subs["42"]["hex"] = "07"
d5subs["42"]["valueType"] = "uchar"
d5subs["42"]["subTlvs"] = []

d5subs["43"] = {}
d5subs["43"]["description"] = "PriorityUp"
d5subs["43"]["hex"] = "04"
d5subs["43"]["valueType"] = "uchar"
d5subs["43"]["subTlvs"] = []

d5subs["44"] = {}
d5subs["44"]["description"] = "GuaranteedUp"
d5subs["44"]["hex"] = "05"
d5subs["44"]["valueType"] = "uint"
d5subs["44"]["subTlvs"] = []

d5subs["45"] = {}
d5subs["45"]["description"] = "MaxBurstUp"
d5subs["45"]["hex"] = "06"
d5subs["45"]["valueType"] = "ushort"
d5subs["45"]["subTlvs"] = []

d5subs["46"] = {}
d5subs["46"]["description"] = "PrivacyEnable"
d5subs["46"]["hex"] = "07"
d5subs["46"]["valueType"] = "uchar"
d5subs["46"]["subTlvs"] = []


DocsisTlvs["05"]["subTlvs"] = d5subs