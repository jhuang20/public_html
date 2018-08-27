#!/usr/bin/python
import cgi,cgitb,os
cgitb.enable()
form=cgi.FieldStorage()
print """Content-type: text/html\n\n"""
print
#this accepts/rejects a person
def FStoD():
    '''
    Converts cgi.FieldStorage() return value into a standard dictionary
    '''
    d = {}
    formData = cgi.FieldStorage()
    for k in formData.keys():
        d[k] = formData[k].value
    return d

def remove(): #lists out all the necessary variables to find
    nile=FStoD()['admit'] #0 means reject, 1 means admit
    tile=FStoD()['file'] #file name to find the csv
    csvfile = open(tile+".csv", "r+")#opens the file
    lines= csvfile.readlines()
    csvfile.seek(0)
    for i in lines:
	p=i.split(",")
	for data in p:
	    if FStoD()['osis']==data:
		if nile=='1':
		    i=i.rstrip('\n')+',accept \n'
		elif nile=='2':
		    i=i.rstrip('\n')+',confirm \n'
		elif nile=='3':
		    i=i.rstrip('\n')+',waitlist \n'
		else:
		    i=i.rstrip('\n')+',reject \n'
	if nile=='10' and 'confirm' in i:
	    i=i.rstrip('\n')+',postpone \n'
	if nile=='20' and 'postpone' in i:
	    i=i.rstrip('\n')+',confirm \n'
        if FStoD()['osis'] in i: #goes to line where OSIS is and changes status
	    if nile=='1':
	        i=i.rstrip('\n')+',accept \n'
	    elif nile=='2':
		i=i.rstrip('\n')+',confirm \n'
	    elif nile=='3':
		i=i.rstrip('\n')+',waitlist \n'
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
