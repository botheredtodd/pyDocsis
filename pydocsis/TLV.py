import codecs
from pydocsis.mib import MIB
import binascii
from pydocsis.docsisTlvs import DocsisTlvs
# from pydocsis.mtaMibs import mibs


def to_little(val):
    little_hex = bytearray.fromhex(val)
    little_hex.reverse()
    print("Byte array format:", little_hex)

    str_little = ''.join(format(x, '02x') for x in little_hex)

    return str_little


def pad_hex(val, datatype):
    """
    takes your string of hex and formats it correctly for tlvs

    :param val: the initial hex string
    :type val: basestring
    :param datatype: the type of data you are formatting
    :type datatype: basestring
    :return: the hex you should put in the config file
    :rtype: basestring
    """
    result = val.replace('0x', '').upper()
    if divmod(len(result), 2)[1] == 1:
        # Padding
        result = '0{}'.format(result)
    if datatype == "uchar":
        return result
    elif datatype == "uint":
        while len(result) < 8:
            result = '00{}'.format(result)
    elif datatype == "ushort":
        while len(result) < 4:
            result = '00{}'.format(result)
    return result


class TLV:
    def __init__(self, **args):
        if "tag" in args.keys():
            self.tag = args["tag"]
        else:
            self.tag = ""
        if "datatype" in args.keys():
            self.datatype = args["datatype"]
        else:
            self.datatype = ""
        if "value" in args.keys():
            self.value = args["value"]
        else:
            self.value = ""
        if "subTLVs" in args.keys():
            self.subTLVs = args["subTLVs"]
        else:
            self.subTLVs = []

    def encode_for_file(self, tags=None):
        if tags is None:
            tags = {}
        if tags == {}:
            tags = DocsisTlvs
        tlv_string = ''
        htag = tags[self.tag]["hex"]
        tvalue = self.value
        print(tvalue)
        for st in self.subTLVs:
            tvalue += st.encode_for_file(tags[self.tag]["subTlvs"])
        if divmod(len(tvalue), 2)[1] == 1:
            print(htag)
            print(tvalue)
            print(divmod(len(tvalue), 2))
            raise ValueError('Invalid value length - the length must be even')
        tlvlen = str(hex(int(len(tvalue) / 2)))[2:]

        if len(tlvlen) == 1:
            tlvlen = "0" + tlvlen
        if len(tlvlen) == 3:
            tlvlen = "0" + tlvlen
        tlv_string += tlv_string + htag.upper() + tlvlen + tvalue.upper()
        return tlv_string

    def get_value(self):
        tvalue = self.value
        if self.datatype == "aggregate":
            return
        if self.datatype == "uchar":
            return int(self.value, 16)
        elif self.datatype == "uint":
            return int(self.value, 16)
            # return int(to_little(self.value),
            #            16)  # you should never see this, but I am leaving it here for big-endian hassles.
        elif self.datatype == "ushort":
            return int(self.value, 16)
            # return int(to_little(self.value),
            #            16)  # you should never see this, but I am leaving it here for big-endian hassles.
        elif self.datatype == "strzero":
            return codecs.decode(self.value[:-2], "hex").decode()
        elif self.datatype == "string":
            return codecs.decode(self.value[:-2], "hex").decode()
        elif self.datatype == "hexstr":
            return "0x" + self.value
        elif self.datatype == "snmp_object":
            m = MIB()
            m.decode(self.value)
            return m
            # if m.oid not in mibs.keys():
            #     # return
            #     return (m.oid + " " + m.dataType + " Index:" + m.index + " " + m.value)
            # else:
            #     # return
            #     return (mibs[m.oid]["description"] + " " + m.dataType + " Index:" + m.index + " " + m.value)
        elif self.datatype == "unknown":
            return "0x" + self.value
        elif self.datatype == "md5":
            return self.value
        elif self.datatype == "special":
            return self.value
        elif self.datatype == "encode_ip":
            return self.value
        elif self.datatype == "encode_ip6":
            return self.value
        else:
            print("Write a decoder for " + self.datatype)
            return tvalue

    def set_value(self, value, oid=""):
        if self.datatype in ["uchar", "ushort", "uint"]:
            self.value = pad_hex(str(hex(int(value))), self.datatype)
        elif self.datatype == "hexstr":
            self.value = value.replace('0x', '').upper()
        elif self.datatype == "snmp_object":
            m = MIB()
            m.decode(value)
            if oid != "":
                m.oid = oid
            if value != "":
                m.value = value
            print(m.encode())
            self.value = m.encode()

        elif self.datatype == "strzero":
            # print(self.value)
            newval = ""
            # for ch in value:
            tmp = binascii.hexlify(value.encode("ascii")).decode()
            newval += str(tmp)

            newval += "00"
            self.value = newval
