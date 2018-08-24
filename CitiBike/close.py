#!/usr/bin/python
import cgi,cgitb,os
cgitb.enable()
form=cgi.FieldStorage()
print """Content-type: text/html\n\n"""
print
#this removes a person
def FStoD():
    '''
    Converts cgi.FieldStorage() return value into a standard dictionary
    '''
    d = {}
    formData = cgi.FieldStorage()
    for k in formData.keys():
        d[k] = formData[k].value
    return d

def remove(): #removes person by looking for OSIS in cgi and not writing it to the CSV file
    tile=FStoD()['file']
    csvfile = open("events.csv", "r+")#opens the file
    lines= csvfile.readlines()
    csvfile.seek(0)
    for i in lines:
	if tile in i:
	    i=i.rstrip("\n")
	    i+=',4 \n'
	    csvfile.write(i)
        if not tile in i:
            csvfile.write(i)
    csvfile.truncate()
    csvfile.close()

def user(): #confirms removal
    return """
    <!DOCTYPE html>
<html>
<head>
  <link rel="shortcut icon" type="image/png" href="logo.png" />
<meta http-equiv="refresh" content='20; url="""+FStoD()['file']+"""-admin.py'>
</head>
<title>Dashboard</title>
<body>
<h1>You closed this form!</h1>
<p><a href='"""+FStoD()['file']+"""-admin.py'>back to event</a></p>
</body>
</html>"""
remove()
print user()
