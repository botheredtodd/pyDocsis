"""
stack up a bunch of TLVs and send it to a cable modem
"""
import binascii
from pydocsis.TLV import TLV
from pydocsis.docsisTlvs import DocsisTlvs
import hashlib


class CmConfig(object):
    """
A config file for a cable modem.
    """

    def __init__(self):
        self.tlvs = []
        self.configFilePath = ""
        self.tlv_string = ""
        self.tags = DocsisTlvs
        self.hashme = []

    def generate_string_from_file(self, file=""):
        """
        loads the bytes form the file as a string...because this is all string trickery
        :param file: filename to import
        :type file: basestring
        """
        if file != "":
            self.configFilePath = file
        if self.configFilePath != "":
            f = open(self.configFilePath, "rb")
            content = f.read()
            self.tlv_string = binascii.hexlify(content).decode('UTF-8')[:]
        else:
            raise ValueError("Cannot turn a file into a string if there is no file.")

    def parse(self, tlv_string="", tags=None):
        """stolen from https://github.com/timgabets/pytlv and modified"""
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
                    value_length = 0
                    try:
                        if tlv_string[i + tag_length:i + tag_length + 2] != '':
                            value_length = int(tlv_string[i + tag_length:i + tag_length + 2], 16)
                    except ValueError:
                        raise ValueError('Parse error: tag ' + tag + ' has incorrect data length')

                    value_start_position = i + tag_length + 2
                    value_end_position = i + tag_length + 2 + value_length * 2

                    if value_end_position > len(tlv_string) and hv != "ff" and tag != "00":
                        raise ValueError('Parse error: tag ' + tag + ' declared data of length ' + str(
                            value_length) + ', but actual data length is ' + str(
                            int(len(tlv_string[value_start_position - 1:-1]) / 2)))
                    else:

                        value = tlv_string[value_start_position:value_end_position]
                        # if tag == "11":
                        #    print(value)
                        if len(tags[tag]["subTlvs"].keys()) > 0:
                            # print(tag)
                            # print("down")
                            subts = self.parse(value, tags[tag]["subTlvs"])
                            # print("up")
                            parsed_data = [tag, subts]
                            tlvs.append(TLV(tag=tag, subTLVs=subts, datatype=tags[tag]["datatype"]))
                        # tlvs.append(parsed_data)
                        else:
                            # if tag == "11":
                            #    print(value)
                            # if "str" in tags[tag]["datatype"]:
                            #    if "encode_strzero" in tags[tag]["datatype"]:
                            #        value = value[:-2]
                            #    value = codecs.decode(value, "hex")
                            # parsed_data = [tag,  tags[tag]["description"], tags[tag]["datatype"] , value]
                            tlvs.append(TLV(tag=tag, value=value, datatype=tags[tag]["datatype"]))
                        i = value_end_position
                    tag_found = True
            if not tag_found:
                # print(i)
                print(tlvs)
                msg = 'Unknown tag found: ' + tlv_string[i:i + 10]
                raise ValueError(msg)
        self.tlvs = tlvs
        return tlvs

    def encode(self):
        """
Writes out the config in binary to self.configFilePath. This should be a working config file, unless you filled it full
of bad values.
        """
        oldTLV7 = TLV(tag="07", datatype="md5", value="")
        stuff = ''  # '0x'
        lastTLV = TLV()
        for tag in self.tlvs:
            if tag.tag not in ["06", "07", "255"]:
                if tag.tag != "00":
                    stuff += tag.encode_for_file()
            elif tag.tag in ["06", "07"]:
                self.hashme.append(tag.tag)
                if tag.tag == "07":
                    oldTLV7.set_value(tag.get_value())
            else:
                lastTLV = tag
        # stuff = stuff.encode('UTF-8')
        exts = ""
        if '06' in self.hashme:
            newval = hashlib.md5(binascii.unhexlify(stuff))
            # print(newval.hexdigest())
            nextTLV = TLV(tag="06", datatype="md5", value=newval.hexdigest())
            exts += nextTLV.encode_for_file()
        if '07' in self.hashme:
            newval = hashlib.md5(binascii.unhexlify(stuff))
            nextTLV = TLV(tag="07", datatype="md5", value=newval.hexdigest())
            #exts += nextTLV.encode_for_file()
            exts += oldTLV7.encode_for_file()

        stuff += exts
        stuff += lastTLV.encode_for_file()

        while (len(stuff) / 2) % 4 != 0:
            stuff += "00"
        # print(stuff)
        if self.configFilePath != "":
            f = open(self.configFilePath, "wb")
            f.write(binascii.unhexlify(stuff))
            f.close()


def json_this(tlvs):
    """
I don't think I am using this for anything. It _should_ convert a cm config, or at least it's list of TLVs, into JSON
    :param tlvs: list of TLVs
    :type tlvs: [TLV]
    :return: a disct that can be easily converted to json
    :rtype: {}
    """
    outs = {}
    for t in tlvs:
        if len(t.subTLVs) == 0:
            outs[t.tag] = str(t.get_value()) + " (" + t.datatype + ")"
        else:
            outs[t.tag] = json_this(t.subTLVs)
    return outs
