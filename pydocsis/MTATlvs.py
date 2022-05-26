# For aesthetic reasons, the user is encouraged to put this in a database or something

MTATlvs = {}

MTATlvs["00"] = {}
MTATlvs["00"]["description"] = "/* Pad */"
MTATlvs["00"]["hex"] = "00"
MTATlvs["00"]["datatype"] = "special"
MTATlvs["00"]["subTlvs"] = {}

MTATlvs["11"] = {}
MTATlvs["11"]["description"] = "SnmpMibObject"
MTATlvs["11"]["hex"] = "0b"
MTATlvs["11"]["datatype"] = "snmp_object"
MTATlvs["11"]["subTlvs"] = {}

MTATlvs["38"] = {}
MTATlvs["38"]["description"] = "SnmpV3TrapReceiver"
MTATlvs["38"]["hex"] = "26"
MTATlvs["38"]["datatype"] = "aggregate"
MTATlvs["38"]["subTlvs"] = {}

MTATlvs["38"]["subTlvs"]["01"] = {}
MTATlvs["38"]["subTlvs"]["01"]["description"] = "SnmpV3TrapRxIP"
MTATlvs["38"]["subTlvs"]["01"]["hex"] = "01"
MTATlvs["38"]["subTlvs"]["01"]["datatype"] = "(encode_ip)"
MTATlvs["38"]["subTlvs"]["01"]["subTlvs"] = {}

MTATlvs["38"]["subTlvs"]["02"] = {}
MTATlvs["38"]["subTlvs"]["02"]["description"] = "SnmpV3TrapRxPort"
MTATlvs["38"]["subTlvs"]["02"]["hex"] = "02"
MTATlvs["38"]["subTlvs"]["02"]["datatype"] = "ushort"
MTATlvs["38"]["subTlvs"]["02"]["subTlvs"] = {}

MTATlvs["38"]["subTlvs"]["03"] = {}
MTATlvs["38"]["subTlvs"]["03"]["description"] = "SnmpV3TrapRxType"
MTATlvs["38"]["subTlvs"]["03"]["hex"] = "03"
MTATlvs["38"]["subTlvs"]["03"]["datatype"] = "ushort"
MTATlvs["38"]["subTlvs"]["03"]["subTlvs"] = {}

MTATlvs["38"]["subTlvs"]["04"] = {}
MTATlvs["38"]["subTlvs"]["04"]["description"] = "SnmpV3TrapRxTimeout"
MTATlvs["38"]["subTlvs"]["04"]["hex"] = "04"
MTATlvs["38"]["subTlvs"]["04"]["datatype"] = "ushort"
MTATlvs["38"]["subTlvs"]["04"]["subTlvs"] = {}

MTATlvs["38"]["subTlvs"]["05"] = {}
MTATlvs["38"]["subTlvs"]["05"]["description"] = "SnmpV3TrapRxRetries"
MTATlvs["38"]["subTlvs"]["05"]["hex"] = "05"
MTATlvs["38"]["subTlvs"]["05"]["datatype"] = "ushort"
MTATlvs["38"]["subTlvs"]["05"]["subTlvs"] = {}

MTATlvs["38"]["subTlvs"]["06"] = {}
MTATlvs["38"]["subTlvs"]["06"]["description"] = "SnmpV3TrapRxFilterOID"
MTATlvs["38"]["subTlvs"]["06"]["hex"] = "06"
MTATlvs["38"]["subTlvs"]["06"]["datatype"] = "(encode_oid)"
MTATlvs["38"]["subTlvs"]["06"]["subTlvs"] = {}

MTATlvs["38"]["subTlvs"]["07"] = {}
MTATlvs["38"]["subTlvs"]["07"]["description"] = "SnmpV3TrapRxSecurityName"
MTATlvs["38"]["subTlvs"]["07"]["hex"] = "07"
MTATlvs["38"]["subTlvs"]["07"]["datatype"] = "string"
MTATlvs["38"]["subTlvs"]["07"]["subTlvs"] = {}

MTATlvs["38"]["subTlvs"]["08"] = {}
MTATlvs["38"]["subTlvs"]["08"]["description"] = "SnmpV3TrapRxIP6"
MTATlvs["38"]["subTlvs"]["08"]["hex"] = "08"
MTATlvs["38"]["subTlvs"]["08"]["datatype"] = "(encode_ip6)"
MTATlvs["38"]["subTlvs"]["08"]["subTlvs"] = {}

MTATlvs["64"] = {}
MTATlvs["64"]["description"] = "snmp_object"
MTATlvs["64"]["hex"] = "40"
MTATlvs["64"]["datatype"] = "snmp_object"
MTATlvs["64"]["subTlvs"] = {}

MTATlvs["254"] = {}
MTATlvs["254"]["description"] = "MtaConfigDelimiter"
MTATlvs["254"]["hex"] = "fe"
MTATlvs["254"]["datatype"] = "uchar"
MTATlvs["254"]["subTlvs"] = {}

MTATlvs["255"] = {}
MTATlvs["255"]["description"] = "/*EndOfDataMkr*/"
MTATlvs["255"]["datatype"] = "special"
MTATlvs["255"]["subTlvs"] = {}
MTATlvs["255"]['hex'] = "ff"

if __name__ == '__main__':
    def print_sub_tlvs(tlv, parent):
        for key in tlv:
            if tlv[key]["datatype"] == "aggregate":
                print("var tlv" + parent + key + " = TLVDefinitions(tag: " + key + ", dataType: ." + tlv[key][
                    "datatype"] + ", description: \"" + tlv[key]["description"] + "\")")
            else:
                print("let tlv" + parent + key + " = TLVDefinitions(tag: " + key + ", dataType: ." + tlv[key][
                    "datatype"] + ", description: \"" + tlv[key]["description"] + "\")")
            print_sub_tlvs(tlv[key]["subTlvs"], parent + key)
            print("tlv" + parent + ".subTLVs.append(tlv" + parent + key + ")")


    endbits = "let DOCSIS :[TLVDefinitions] = [\n"
    # fp = open("outs.json", 'w')
    # json.dump(MTATlvs, fp)
    for key in MTATlvs.keys():
        endbits += "tlv" + key + ",\n"
        if MTATlvs[key]["datatype"] == "aggregate":
            print("var tlv" + key + " = TLVDefinitions(tag: " + key + ", dataType: ." + MTATlvs[key][
                "datatype"] + ", description: \"" + MTATlvs[key]["description"] + "\")")
        else:
            print("let tlv" + key + " = TLVDefinitions(tag: " + key + ", dataType: ." + MTATlvs[key][
                "datatype"] + ", description: \"" + MTATlvs[key]["description"] + "\")")
        print_sub_tlvs(MTATlvs[key]["subTlvs"], key)
    endbits += "]"
    print(endbits)
