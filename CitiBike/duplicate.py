#!/usr/bin/python
import cgi,cgitb,os
from shutil import copyfile
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
    nile=FStoD()['newdate'] #new files
    tile=FStoD()['file'] #file name to find the file names
    copyfile(tile+'.py',nile+'.py')
    copyfile(tile+'.csv',nile+'.csv')
    copyfile(tile+'-admin.py',nile+'-admin.py')
    os.chmod(nile+'.py',0777)
    os.chmod(nile+'.csv',0777)
    os.chmod(nile+'-admin.py',0777)
def user():
    return """
    <!DOCTYPE html>
<html>
<head>
  <link rel="shortcut icon" type="image/png" href="logo.png" />
<meta http-equiv="refresh" content='20; url="""+FStoD()['newdate']+"""-admin.py'>
</head>
<title>Dashboard</title>
<body>
<h1>You Rescheduled The Event. Now, check that everything is copied over and then proceed to the Dashboard to delete the old event!</h1>
<p><a href='"""+FStoD()['newdate']+"""-admin.py'>To New Event</a></p>
</body>
</html>"""
remove()
print user()
