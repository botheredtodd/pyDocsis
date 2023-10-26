# Basics

Make a branch, or fork, or whatever. I don’t care. Work how you like.

Submit a pull request!

Brag to your boss that you are part of the development team for the open source tool that you use to break cable modems.

# Needs

- I should rename mtaMibs…
- a better way to handle mibs. The thing I forked is...not ideal
- There are WAY too many TLVs for one mere mortal to enter. See below…
- Eventually, I need to make a database thing for the TLVs

# Wants

- config files for testing. More files means catching more edge cases means a better end product
- A way to make this work as an ansible plugin. People who approve raises seem to be excited about that ansible thing…


# Adding TLVs

 ```
DocsisTlvs[“22”] = {}
DocsisTlvs[“22”][“description”] = “UsPacketClass”
DocsisTlvs[“22”][“hex”] = “16”
DocsisTlvs[“22”][“datatype”] = “aggregate”
DocsisTlvs[“22”][“subTlvs”] = {}

DocsisTlvs[“22”][“subTlvs”][“01”] = {}
DocsisTlvs[“22”][“subTlvs”][“01”][“description”] = “ClassifierRef”
DocsisTlvs[“22”][“subTlvs”][“01”][“hex”] = “01”
DocsisTlvs[“22”][“subTlvs”][“01”][“datatype”] = “uchar”
DocsisTlvs[“22”][“subTlvs”][“01”][“subTlvs”] = {}
```

So, we have a DocsisTlvs dict, where the key is the typecode as a string. Each key has a description, hex (the string of the hex of the typecode…for reasons that are dumb), datatype, and subTlvs. Each sub tlv is just like the tlv as far as properties and all that. It’s like turtles, stacked all the way down.

I know I should be handling the bytes as, well, bytes but strings cause less weirdness with dicts and things.
