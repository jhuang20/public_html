#!/usr/bin/python
# ========= HASHBANG LINE ABOVE IS MAGIC! =========
# ========= (Must be first line of file.) =========

#Team Muji - Mihad Khondker and James Huang
#IntroCS2 pd3
#HW60 -- 
#2017-06-01

import cgi
import cgitb
cgitb.enable()  #diag info --- comment out once full functionality achieved

# ~~~~~~~~~~~~~~~ support functions ~~~~~~~~~~~~~~~

def FStoD():
    '''
    Converts cgi.FieldStorage() return value into a standard dictionary
    '''
    d = {}
    formData = cgi.FieldStorage()
    for k in formData.keys():
        d[k] = formData[k].value
    return d

def rot13Chr(x):#this is our encryption process for each word
    if 64 < ord(x) < 91:
        return chr(((ord(x)-65 + 13) % 26) +65)
    elif 123 > ord(x) > 96:
        return chr(((ord(x)-97 + 13) % 26) +97)
    else:
        return x
    
def rot13(phrase):#if we want to do rot13, we get the phrase, split up into elements. we then make it into a string!
    count=0
    new=''
    while count<len(phrase):
        new += rot13Chr(phrase[count])
        count+=1
    return new

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ========= CONTENT-TYPE LINE REQUIRED. ===========
# ======= Must be beginning of HTML string ======== 
print "Content-Type: text/html\n\n" #NOTE there are 2 '\n's !!! 
print '''<html>
<head><title> TEST STUFF </title></head>\n
<body bgcolor=#ffecca>'''
# ~~~~~~~~~~~~~ HTML-generating code ~~~~~~~~~~~~~~
# types of formatting that we need plus its respective tags
types=['B','I','U','BIG','marq']#reference to the name tags we assigned in our html code
tags=['<b>','<i>','<u>','<h1>','<marquee>']
closetags=['</b>','</i>','</u>','</h1>','</marquee>']
print '''
<table width=100% bgcolor=#fce7c4>
<tr><th>
Mihad Khondker & James Huang's Text Converter!
</th></tr>
</table><br>

<table align=center bgcolor=#fce7c4>
<tr><td align=center>'''

for i in range(len(types)):
    if FStoD().has_key(types[i]): #if that tag exists in the query string, print it
	print tags[i]

if FStoD().has_key('type'): # make sure a type of text editing/encryption is selected
    if FStoD()['type']=='ROT13':#if ROT 13 is selected
   	if FStoD().has_key('text')==True: # gotta make sure you have text 
	    print rot13(FStoD()['text'])#print the rot13 edition of your text
        else: 
            print 'Please submit some text!'#if there is no text ask to submit text
    else:
   	if FStoD().has_key('text')==True:
	    print FStoD()['text'][::-1]#if ROT13 isnt selected the other must be selected! We reverse the text here
        else: 
            print 'Please submit some text!' 
else:
    if FStoD().has_key('text')==True: 
        print FStoD()['text']#print out the text
    else: 
        print 'Please submit some text!'

for i in range(len(types)):
    if FStoD().has_key(types[i]): # I have to close the tags from before!
	print closetags[::-1][i]

print'''</td></tr>
</table>'''
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print "\n</body></html>"


