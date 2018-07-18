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
    os.remove(tile+".csv")
    os.remove(tile+"-admin.py")
    os.remove(tile+".py")

def user():
    return """
    <!DOCTYPE html>
<html>
<head>
  <link rel="shortcut icon" type="image/png" href="logo.png" />
</head>
<title>Dashboard</title>
<body>
<h1>U submitted an event!</h1>
<p><a href="dashboard.py">back to dashboard</a></p>
</body>
</html>"""
remove()
print user()
