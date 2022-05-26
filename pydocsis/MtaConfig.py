import binascii
# import codecs
import sys
from pydocsis.TLV import TLV
# from docsisTlvs import DocsisTlvs
from pydocsis.MTATlvs import MTATlvs
# from mib import mib
import hashlib


class MtaConfig(object):
    def __init__(self):
        self.tlvs = []
        self.configFilePath = ""
        self.tlv_string = ""
        self.tags = MTATlvs
        self.content = None

    def generate_string_from_file(self, file=""):
        if file != "":
            self.configFilePath = file
        if self.configFilePath != "":
            f = open(self.configFilePath, "rb")
            self.content = f.read()
            self.tlv_string = binascii.hexlify(self.content).decode('UTF-8')[:]
        else:
            raise ValueError("Cannot turn a file into a string if there is no file.")

    def parse(self, tlv_string="", tags=None):
        """
        stolen from https://github.com/timgabets/pytlv and modified
        """
        if tags is None:
            tags = {}
        tlvs = []
        if len(tlv_string) == 0:
            tlv_string = self.tlv_string
            print(tlv_string)
        i = 0
        if len(tags.keys()) == 0:
            print("Loading keys from docsis file")
            tags = self.tags
        while i < len(tlv_string):
            tag_found = False
            tag_length = 2
            for tag in tags.keys():
                hv = tags[tag]["hex"]  # hex(int(tag)).replace('0x', '')
                if len(hv) == 1:
                    hv = "0" + hv
                if tlv_string[i:i + tag_length] == hv:
                    # if hv == "fe":
                    #	print("Maybe done with MTA")
                    #	return tlvs
                    value_length = 0
                    try:
                        if tag == "64":
                            value_length = int(tlv_string[i + tag_length:i + tag_length + 4], 16)
                        elif tlv_string[i + tag_length:i + tag_length + 2] != '':
                            value_length = int(tlv_string[i + tag_length:i + tag_length + 2], 16)

                    except ValueError:
                        raise ValueError('Parse error: tag ' + tag + ' has incorrect data length')

                    value_start_position = i + tag_length + 2

                    value_end_position = i + tag_length + 2 + value_length * 2
                    if tag == "64":
                        value_start_position += 2
                        value_end_position += 2
                    if value_end_position > len(
                            tlv_string):  # and hv != "ff" and tag != "00" and tag != "107" and tag != "61" and tag != "97" and tag != "101" and tag != "35" and tag != "10" and tag != "106" and tag != "116" and tag != "52" and tag != "48" and tag != "51" and tag != "54" and tag != "102"  and tag != "83" and tag != "118" and tag != "67" and tag != "80":
                        raise ValueError('Parse error: tag ' + tag + ' declared data of length ' + str(
                            value_length) + ', but actual data length is ' + str(
                            int(len(tlv_string[value_start_position - 1:-1]) / 2)))
                    else:
                        value = tlv_string[value_start_position:value_end_position]
                        # if tag == "64":
                        #	print(value)
                        if len(tags[tag]["subTlvs"].keys()) > 0:
                            print(tag)
                            print("down")
                            subts = self.parse(value, tags[tag]["subTlvs"])
                            print("up")
                            parsed_data = [tag, subts]
                            tlvs.append(TLV(tag=tag, subTLVs=subts, datatype=tags[tag]["datatype"]))
                        # tlvs.append(parsed_data)
                        else:
                            # if "str" in tags[tag]["datatype"]:
                            #	if "encode_strzero" in tags[tag]["datatype"]:
                            #		value = value[:-2]
                            #	value = codecs.decode(value, "hex")
                            # parsed_data = [tag,  tags[tag]["description"], tags[tag]["datatype"] , value]
                            # if tag == "64":
                            tlvs.append(TLV(tag=tag, value=value, datatype=tags[tag]["datatype"]))
                        i = value_end_position
                    tag_found = True
            if not tag_found:
                # print(i)
                print(tlvs)
                msg = 'Unknown tag found: ' + tlv_string[i:i + 10]
                raise ValueError(msg)
        return tlvs

    def encode(self):
        stuff = ''  # '0x'
        for tag in self.tlvs:
            stuff += tag.encode_for_file()
        # stuff = stuff.encode('UTF-8')
        print(stuff)
        if self.configFilePath != "":
            f = open(self.configFilePath, "wb")
            f.write(binascii.unhexlify(stuff))
            f.close()

    def hash(self):
        stuff = ''  # '0x'
        for tag in self.tlvs:
            if MTATlvs[tag.tag]["datatype"] == "snmp_object":
                bob = tag.get_value()
                if tag.tag == "64":
                    print("here")
                if "pktcMtaDevProvConfigHash" in bob:
                    print("Already hashed, it would be great if you got: ")
                    print(tag.get_value())
                else:
                    stuff += tag.encode_for_file()
                # print(len(stuff))
            else:
                stuff += tag.encode_for_file()
            # print(len(stuff))
        # print(stuff)
        print(hashlib.sha1(binascii.unhexlify(stuff)).hexdigest())


if __name__ == '__main__':
    cm = MtaConfig()
    cm.generate_string_from_file(sys.argv[1])
    cm.tags = MTATlvs
    # print(cm.tlv_string)
    cm.tlvs = cm.parse(cm.tlv_string, cm.tags)
    # cm.hash()
    cm.configFilePath += ".new"
    # print(cm.tlv_string.upper())
    # print()
    # cm.encode()
    # print("########")
    for t in cm.tlvs:
        t.get_value()
        # if t.datatype in ["uchar", "uint", "ushort", "hexstr"]:
        #	if t.tag == "18":
        #		bb = t.getValue()
        #		print(bb)
        #		t.setValue(bb + 1)
        # print("before")
        # print(t.value)
        # t.setValue(bb)
        # print("after")
        # print(t.value)
        # else:
        #	if t.datatype not in  ["snmp_object", "aggregate"]:
        #		print("Write a decoder for " + t.datatype)
        # print(t.tag)
        if t.tag == "11" or t.tag == "64":
            # before = t.value
            m = t.get_value()
            print(m.oid + " " + m.value + " " + m.dataType)
        # print(before.upper())
        # print(m.encode().upper())
        # if "datatype" in DocsisTlvs[t.tag].keys():
        #	print(DocsisTlvs[t.tag]["datatype"])
        # if MTATlvs[t.tag]["datatype"] == "snmp_object":
        # 	bob = t.getValue()
        # 	if bob != None:
        # 		print(t.getValue())

        else:
            print(t.tag)
            print(t.datatype)
            print(t.get_value())
    # t.getValue()
    # print(t.getValue())
    # for tt in t.subTLVs:
    #	print("  " + tt.tag)
    # print("  " + tt.datatype)
    # if tt.datatype in ["uchar", "uint", "ushort", "hexstr", "strzero"]:
    # bb = tt.getValue()
    # print("before")
    # print(tt.value)
    # tt.setValue(bb)
    # print("after")
    # print(tt.value)
    # else:
    # if tt.datatype  not in  ["snmp_object", "aggregate"]:
    # print("Write a decoder for " + tt.datatype)
    # if "datatype" in DocsisTlvs[t.tag]["subTlvs"][tt.tag].keys():
    #	print("  " + DocsisTlvs[t.tag]["subTlvs"][tt.tag]["datatype"])
    # print("  " + str(tt.getValue()))
    # tt.getValue()
    #	print("  " + tt.decodedValue(DocsisTlvs[t.tag]["subTlvs"]))
    cm.encode()
