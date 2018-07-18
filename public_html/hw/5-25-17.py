#!/usr/bin/python
print ""
outStream=open('foop.txt','w')

import os
d=os.environ
counter=0
e='{'
f=d.values()
for i in d:
    e+=str(d.keys()[counter])
    e+=', '+d[i]+': '
    counter+=1
e+='}'
print e
outStream.write(str(e))
outStream.close()

