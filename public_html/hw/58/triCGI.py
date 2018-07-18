#!/usr/bin/python
#james huang
#HW58
#introcs2 pd03
#05-26-2017
print 'content-type: text/html'
print ""
print '<!DOCTYPE html><html><body>'

import os
import cgi
print '<form>a:<br><input type="number" name="a"><br>b:<br><input type="number" name="b"><br>c:<br><input type="number" name="c"><br> <input type="submit" value="Submit"></form>'
cgi.FieldStorage()
foo = cgi.FieldStorage()
#diag output
def life(foo):
    a=[]
    for k in foo.keys():
        a+= [foo[k].value]
    return a



def quor(a):
    if a==[]:
        return 'no query string:input 3 values into form above'
    else:
	
        perimeter=0
        c=[]
        if len(a)==3:
            for i in a:		
                c+=[int(i)]
            for x in c:
                perimeter+=x
            area=(c[0]*c[2])/2
        else:
            perimeter='no valid parameters'
            area='no valid parameters: all values in the form must be entered, then submitted'
    print 'orig values: '+str(a)+'<br>'+'area='+str(area)+'<br>perimeter='+str(perimeter)
    
    
a=life(foo)    
print quor(a)+'</body></html>'


