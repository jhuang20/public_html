#!/usr/bin/python
import cgi,cgitb,os
cgitb.enable()
form=cgi.FieldStorage()
print """Content-type: text/html\n\n"""
print
#this creates a new page!
def FStoD():
    '''
    Converts cgi.FieldStorage() return value into a standard dictionary
    '''
    d = {}
    formData = cgi.FieldStorage()
    for k in formData.keys():
        d[k] = formData[k].value
    return d

def remove():
    nile=FStoD()['admit']
    tile=FStoD()['file']
    csvfile = open(tile+".csv", "r+")#opens the file
    lines= csvfile.readlines()
    csvfile.seek(0)
    for i in lines:
        if FStoD()['osis'] in i:
	    if nile=='1':
	        i=i.rstrip('\n')+',accept \n'
            else:
		i=i.rstrip('\n')+',reject \n'
	    csvfile.write(i)
	else:
	    csvfile.write(i)
    csvfile.truncate()
    csvfile.close()

def user():
    return """
    <!DOCTYPE html>
<html>
<head>
  <link rel="shortcut icon" type="image/png" href="logo.png" />
<meta http-equiv="refresh" content='20; url="""+FStoD()['file']+"""-admin.py'>
</head>
<title>Dashboard</title>
<body>
<h1>You accepted/rejected a person</h1>
<p><a href='"""+FStoD()['file']+"""-admin.py'>back to event</a></p>
</body>
</html>"""
remove()
print user()
