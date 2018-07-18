#!/usr/bin/python
print ""
outStream=open('foop.txt','w')

import os
d=os.environ
counter=0
e=d.values
f=d.keys
for i in d.keys():
    print i+' '+d.values()[counter]
    counter+=1
print d["HOMEPATH"]
outStream.write(d["HOMEPATH"])
outStream.close()

