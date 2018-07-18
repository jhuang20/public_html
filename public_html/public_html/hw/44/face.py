#!/usr/bin/python
print "Content-Type: text/html\n"
print ""
print "<!DOCTYPE html>"
print "<html><head><style>body {background-color: lightblue;}</style><title>Madlibification</title></head><body>"
import random
hair=["|","Z","*","$"]
#brows=["w",
eyes=["-","o","0","_","X"]
nose=["j","J","|","/","T","V","^"]
mouth=["_","O","P","$","%","*"]
z=random.randrange(len(eyes))
print "Here's Our Face"
print "<pre> \n"+hair[random.randrange(len(hair))]*5+"\n"+eyes[z]+3*" "+eyes[z] \
      +"\n"+2*" "+nose[random.randrange(len(nose))]+2*" "+"\n"+2*" "+mouth[random.randrange(len(mouth))]+"</pre>"
print "Here's Our more COmplex Face"
print "<pre"
print "</body></html>"


    
           
