pyDocsis: A library for doing things to DOCSIS configs with python
=========

A few python files for reading, modifying, and creating DOCSIS files.

It *mostly* works! Mibs need some more testing and TLV7 assumes that your CMTS is going to strip out that value and replace it with something else. See te Docs folder for examples.

I am adding scripts to the library so that you can just use cli to do the important bits.

# Using the scripts

## Updating the list of mibs

Mibs are stored in ~/.mibs.json. If you want to update the list of mibs, run `mib-json-builder.py` and it will update the list from /var/lib/snmp/mibs and  ~/.mibs. If you keep your mibs is a different place, you should tell me to add the '-a' flag to the script. You should only need to run this command if you change the mibs on your system.

## Decoding a DOCSIS config

Running the command cm_decode will decode a DOCSIS config file. It will print out the decoded config to the screen. You should use the -o flag to output the config to a file in a future version.