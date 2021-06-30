f = open("docsis_symtable.h")
for line in f:
	if line.startswith("{"):
		cols = line.split(",")
		descr = (cols[1].lstrip())
		ecode = (cols[4].lstrip())
		dcode = (cols[5].lstrip())
		tlv = cols[0].split(" ")[-1]
		if len(cols[-1].split(" ")) > 4:
			tlv = cols[-1].split(" ")[3]
		
		ftlv = tlv.split(".")
		if len(ftlv) == 1:
			print("DocsisTlvs[\"" + tlv + "\"] = {}")
			print("DocsisTlvs[\"" + tlv + "\"][\"description\"] = " + descr)
			if tlv != "":
				print("DocsisTlvs[\"" + tlv + "\"][\"hex\"] = " + "\"" + hex(int(tlv))[2:] + "\"")
			if "nothing" in ecode:
				print("DocsisTlvs[\"" + tlv + "\"][\"datatype\"] = \"" + dcode + "\"")
			else:
				print("DocsisTlvs[\"" + tlv + "\"][\"datatype\"] = \"" + ecode + "\"")
			print("DocsisTlvs[\"" + tlv + "\"][\"subTlvs\"] = {}")
		else:
			print("DocsisTlvs[\"" + "\"][\"subTlvs\"][\"".join(ftlv) + "\"] = {}")
			print("DocsisTlvs[\"" + "\"][\"subTlvs\"][\"".join(ftlv) + "\"][\"description\"] = " + descr)
			print("DocsisTlvs[\"" + "\"][\"subTlvs\"][\"".join(ftlv) + "\"][\"hex\"] = " + "\"" + hex(int(ftlv[-1]))[2:] + "\"")
			if "nothing" in ecode:
				print("DocsisTlvs[\"" + "\"][\"subTlvs\"][\"".join(ftlv) + "\"][\"datatype\"] = \"" + dcode + "\"")
			else:
				print("DocsisTlvs[\"" + "\"][\"subTlvs\"][\"".join(ftlv) + "\"][\"datatype\"] = \"" + ecode + "\"")
			print("DocsisTlvs[\"" + "\"][\"subTlvs\"][\"".join(ftlv) + "\"][\"subTlvs\"] = {}")
		
		print()