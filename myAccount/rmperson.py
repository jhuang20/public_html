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
    tile=FStoD()['file']
    csvfile = open("../CitiBike/"+tile+".csv", "r+")#opens the file
    lines= csvfile.readlines()
    csvfile.seek(0)
    for i in lines:
        if not FStoD()['osis'] in i:
            csvfile.write(i)
    csvfile.truncate()
    csvfile.close()

def user():
    return """
    <!DOCTYPE html>
<html>
<head>
  <link rel="shortcut icon" type="image/png" href="logo.png" />
<meta http-equiv="refresh" content="0;URL='http://stuybikes.com/public_html/myAccount/hello.py?osis="""+FStoD()['osis']+"""'"/>
</head>
<title>Confirmation</title>
<body>
<form action="hello.py"><input type="hidden" id="osis" name="osis" value='"""+FStoD()['osis']+"""'><input type="submit" value="Back to your Profile"></form>
<h1>Click the go back to profile button to go back to your profile</h1>
<p>You have de-registered from the event on """+FStoD()['file']+""" successfully</p>
</body>
</html>"""
remove()
print user()
