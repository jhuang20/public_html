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
        print querystring

    
print '<!DOCTYPE html><html><body>'
print query()+'</body></html>'

