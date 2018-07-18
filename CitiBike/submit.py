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
def getFile():
    file=FStoD()['file']
    return file
def csvWrite():
    fd = open(getFile()+'.csv','a')
    firstName=FStoD()['firstName']
    lastName=FStoD()['lastName']
    bday=FStoD()['date']
    osis=FStoD()['osis']
    contact=FStoD()['contact']
    myCsvRow=""+osis+""+","+" "+lastName+" "+","+" "+firstName+","+contact+","+bday+" \n"

    fd.write(myCsvRow)
    fd.close()

def user():
    return """
    <!DOCTYPE html>
<html>
<head>
  <link rel="shortcut icon" type="image/png" href="logo.png" />
</head>
<title>Dashboard</title>

<body>

<h1>Thanks for registering!</h1>
<p><a href="../index.html">back home</a></p>

</body>
</html>"""
csvWrite()
print user()
