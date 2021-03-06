#!/usr/bin/python
print 'content-type: text/html\n'


import os
import cgi
import cgitb
cgitb.enable()

def FStoD():
    '''
    Converts cgi.FieldStorage() return value into a standard dictionary
    '''
    d = {}
    formData = cgi.FieldStorage()
    for k in formData.keys():
        d[k] = formData[k].value
    return d

def makenum(L):
    numL=[]
    for i in L:
        numL+=[int(i)]
    return numL

def perimtri(sides):
    if len(sides)<3:
        return 'Error in sides, less than 3 given.'
    else:
        nums=sorted(makenum(sides.values()))
        for i in nums:
            if i<0:
                return "You can't have a negative side!"
        return sum(makenum(sides.values()))
    
def areatri(sides):
    if len(sides)<3:
        return 'Error in sides, less than 3 given.'
    else:
        nums=sorted(makenum(sides.values()))
        for i in nums:
            if i<0:
                return "You can't have a negative side!"
        if nums[0]**2+nums[1]**2==nums[2]**2:
            return nums[0]*nums[1] / 2
        else:
            return 'Not possible, a,b,c must be pythagorean triplets!'
print '''<HTML>
<HEAD>
<BODY bgcolor=#ffecca>
<table bgcolor=#fce7c4 align=center>
<tr><th>James Huang's Right Triangle Calculator</th></tr>
</table>
<TABLE bgcolor=#fce7c4 align=center>
<tr><td align=center><a href="triForm.html">Go back</a>
</td></td>
<tr><td align=center>'''
nums=sorted(makenum(FStoD().values()))
stnum=''
for i in nums: stnum+=str(i)+'|'
print stnum
print '''</td></tr>
<tr><th>Perimeter of Triangle</th></tr>
<tr><td>'''
print perimtri(FStoD())
print '''</td></tr>
<tr><th>Area of Triangle</th></tr>
<tr><td>'''
print areatri(FStoD())
print '''</td></tr>
</TABLE>
</BODY>
</HEAD>
</HTML>'''
