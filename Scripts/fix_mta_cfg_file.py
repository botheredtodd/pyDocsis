#!/usr/bin/env python3
from pydocsis.TLV import TLV
from pydocsis.MTATlvs import MTATlvs
from pydocsis.MtaConfig import MtaConfig
import os
import sys
import json

if len(sys.argv) != 2:
    print("no file specified")
    sys.exit(1)

cm = MtaConfig()
cm.generate_string_from_file(sys.argv[1])
cm.tags = MTATlvs
cm.tlvs = cm.parse(cm.tlv_string, cm.tags)
cm.configFilePath += ".new"
cm.encode()