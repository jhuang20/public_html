#!/usr/bin/python

import cgi

# ~~~~~~~~~~~~~~~ support functions ~~~~~~~~~~~~~~~
def FStoD():
    
    d = {}
    formData = cgi.FieldStorage()
    for k in formData.keys():
        d[k] = formData[k].value
    return d.values()

htmlStr = "Content-Type: text/html\n" 
htmlStr += "<!DOCTYPE html><html><head><title>Calculations</title>\n"
htmlStr += "<body>"

# ~~~~~~~~~~~~~ HTML-generating code ~~~~~~~~~~~~~~
htmlStr += "<h3>Triangle.</h3>"
htmlStr += "<h4>Triangle Stats:</h4>"
htmlStr += str(FStoD())
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

htmlStr += "</body></head></html>"


print htmlStr
