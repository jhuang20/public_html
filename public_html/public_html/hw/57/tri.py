#!/usr/bin/python
print 'content-type: text/html'
print ""


import os
def query():
    d=os.environ
    querystring=d['QUERY_STRING']
    if querystring=='':
        print 'no query string'
    else:
        return quor(querystring)
def quor(a):
    if a=='no query string':
        return a
    else:
        perimeter=0
        c=[]
        d=a[2:]
        b=d.split('&')
        if len(b)==3:
        
            for i in b:
                c+=[int(i[2:])]
            for x in c:
                perimeter+=x
            area=(c[0]*c[1])/2
        else:
            perimeter='no valid parameters'
            area='no valid parameters: must be in the form ?q=a=3&b=4&c=5'
    print '<b>orig query string:</b> '+a+'<br>'+'<b>area=</b>'+str(area)+'<br><b>perimeter=</b>'+str(perimeter)
        
    
    
    

    
print '<!DOCTYPE html><html><body>'
query()
print quor(querystring)+'</body></html>'


