
# Everything changes, including speeds

This is a simple example of changing a setting in a static config using pyDocsis. For this example, we are changing the up and down stream speeds from 266000 to 1000000. That said, you can use this same process to make any other change you would like (except to TLV 11, which will be documented elsewhere...because it sucks)

## The Beginning parts at the beginning

Let's get the cmConfig class and also set the shebang:

```
#!/usr/bin/env python3
import sys
sys.path.append('/Users/tbalsley/git/pyDocsis')
from cmConfig import cmConfig

if len(sys.argv) != 2:
	print("syntax: " + sys.argv[0] + " <filename> where <filename> is the config file you want to change")
	sys.exit()
```

The sys and sys.path is the cheat that I use to import libraries not in the current path. It's probably not the best way to do it, but I have a TextExpander written already, so that's that.

I added a little usage bit because that's good practice.

## Filling the object

Currently, you need to create an empty cmConfig object, set the input file, and then parse it with a specified blob of tags. We should get the filename from argv.

```
cm = cmConfig()
cm.generateStringFromFile(sys.argv[1])
cm.tlvs = cm.parse(cm.tlv_string, cm.tags)
```

A better person would have done this in one step, but I was in a hurry. And then I was lazy.

The only interesting thing here is the `cm.tags` bit. If you have a different list of tags (say, packetcable or DOCSIS9) you can parse the file with those.

## Finding the bits
```
changed = False
for t in cm.tlvs:
	if t.tag in ["25", "24"]:
		for st in t.subTLVs:
			if st.tag == "08":
				if st.getValue() == 266000:
					changed = True
					st.setValue(1000000)
				else:
					print(t.tag + "." + st.tag + " is set to " + str(st.getValue()) + " so I'm not changing it.")
```

I create a boolean named "changed" so that I can write output only if the file has changed. The rest of this is a pretty standard for loop.

Tags are strings for reasons that make sense elsewhere. Because the spec for 24.8 and 25.8 is a number, these values are going to be ints. I use getValue() and setValue() 

## Saving the new file

By default, running an encode on a cmConfig will send the binary output to cm.configFilePath. In this case, that's the input file, so we should change that before re-encoding:

```
if changed == True:
	cm.configFilePath = cm.configFilePath + "-new"
	cm.encode()
```

# Putting it all together

```
#!/usr/bin/env python3
import sys
sys.path.append('/Users/tbalsley/git/pyDocsis')

from cmConfig import cmConfig


if len(sys.argv) != 2:
	print("syntax: " + sys.argv[0] + " <filename> where <filename> is the config file you want to change")
	sys.exit()

cm = cmConfig()
cm.generateStringFromFile(sys.argv[1])
cm.tlvs = cm.parse(cm.tlv_string, cm.tags)
changed = False

for t in cm.tlvs:
	if t.tag in ["25", "24"]:
		for st in t.subTLVs:
			if st.tag == "08":
				if st.getValue() == 266000:
					changed = True
					st.setValue(1000000)
				else:
					print(t.tag + "." + st.tag + " is set to " + str(st.getValue()) + " so I'm not changing it.")
if changed == True:
	cm.configFilePath = cm.configFilePath + "-new"
	cm.encode()
```