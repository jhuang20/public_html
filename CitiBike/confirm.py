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
    tile=FStoD()['file'] #file name to find the csv
    csvfile = open(tile+".csv", "r+")#opens the file
    lines= csvfile.readlines()
    csvfile.close()
    final=''
    id=1
    final+="<table style='width:100%'><tr><th>Roster#</th><th>OSIS</th><th>Last Name</th><th>First Name</th><th>Email</th><th>Birthday</th><th>q1 resp</th><th>q2 resp</th><th>confirm</th><th>Here</th></tr>"
    for i in lines:
	p=i.split(",")
        if p[-1].rstrip(' \n')=='confirm':
	    final+="<tr><td>"+str(id)+"</td>"
	    counter=0
	    id+=1
	    for x in p:
		if counter>6:
		    final+="<td>"+p[-1]+"</td"
		    break
		final+="<td>"+x+"</td>"
		counter+=1
	    final+="</tr>"
    final+="</table>"
    return final

def user():
    return """
    <!DOCTYPE html>
<html>
<head>
  <link rel="shortcut icon" type="image/png" href="logo.png" />
</head>
<title>Dashboard</title>
<body>
<h1>Class roster for """+FStoD()['file']+""" as of now</h1>"""+remove()+"""
<p><a href='"""+FStoD()['file']+"""-admin.py'>back to event</a></p>
</body>
</html>"""
print user()
