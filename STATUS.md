A quick status update

Yes, I worked into the night to get OIDs to decode correctly. There are a few things that still need to be done before the decodes are good. Encodes are (hopefully) going to be easier because we will have figured out the trickery by finishing the decodes. Hopefully.

# pyDocsis

I need a lot of help with this.

## Decoding the config file

cmConfig.py and docsisTlvs.py do all the work here. docsisTlvs.py is the list of TLVs I am working with and captures every one that I found scanning a few thousand CM config files form AT1. New settings need to be added, I am sure. Anyone who wants to expand that file or fix errors will earn my undying appreciation.

In cmConfig.py there is a class for cmConfig, which is full of class TLV objects. If you tell a cmConfig object where the config file is, it will parse the TLVs. I stole and updated the parsing code from an abandoned GitHub project at https://github.com/timgabets/pytlv. All DOCSIS TLVs are two digit numbers in hex, which made it easier, and the sub-tlvs are handled with the magic of recursion.

Reference note: a DOCSIS TLV (as a hex string) is two characters for the type, at least two values for the length of the data, which is half of the number of characters) followed by the data.

TLV.decodedValue(tags) turns the hex gibberish into useful information. I am pretty happy with the hex to int conversions...because math. The stringzero values are also trivial. snmp_objects are a hassle.

## snmp_objects

This is another bit of code that someone abandoned on the internet.

This is one of those things that you work with as an array of two hex character blobs. The first blob is the oid tag, the second is the length. Everything after that is oid. You can use mib files and magic to turn the translated data into useful stuff...but I don't know how to do that.

Yeah, here is where my brain ran out.

So, if anyone wants to help with that final step...


## other objects

Haven't started. The IP stuff should be easy because `import ipaddr` is awesome. I don't know what needs to be done for the other stuff.

## encoding!

It works, assuming you have all the TLV values encoded already. The encoder just turns the tag back into hex, calculates the data length in hex, and puts that on the front of the value. It really is that simple. 

Encoding on the TLV level, as in turning useful information into correctly encoded hex strings, hasn't even been started.

Oh, and I need a way for people to put info in. I know old DOCSIS used a text file, but I can make a GUI, or a web interface, or an application that plugs into a database and generates new configs when values change.