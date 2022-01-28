# I dislike TLV 6 and TLV 7

At this time, you are a little on your own for CMTS MIC (TLV7). 

In the .encode() function of the cmConfig object, there is this:

```
if '06' in self.hashme:
	newval = hashlib.md5(binascii.unhexlify(stuff))
	print(newval.hexdigest())
	nextTLV = TLV(tag="06", datatype = "md5", value = newval.hexdigest())
	exts += nextTLV.encodeForFile()
```

Where `stuff` is a string representation of the binary data in the config file. At this point in the process, it contains everything EXCEPT TLVs 6,7, and 255. `exts` is a temporary variable that holds whatever is going to be tacked on later in the process. I did this because you may have more than one thing that wants to do math to the config file.

TLVs 6, 7, and 255 were dropped in an earlier loop, because they should be recalculated at encode.