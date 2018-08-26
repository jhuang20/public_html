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
    csvfile = open("events.csv", "r")#opens the file
    lines= csvfile.readlines()
    csvfile.close()
    counter=0
    for row in lines:
        ret=row.split(",")#gives you the DATE of the Event
        ping=ret[0]
	wing=ret[1].replace(" ","")
        if ping==tile or wing==tile:
            os.remove(tile+".csv")
            os.remove(tile+"-admin.py")
            os.remove(tile+".py")
    f = open("events.csv","r+")
    d = f.readlines()
    f.seek(0)
    for i in d:
	search=i.split(",") #gives you name of event
	if tile!=search[1].replace(" ","") and tile!=search[0]:
	    f.write(i)
    f.truncate()
    f.close()

def user():
    return """
    <!DOCTYPE html>
<html>
<head>
  <link rel="shortcut icon" type="image/png" href="logo.png" />
</head>
<title>Dashboard</title>
<body>
<h1>You Deleted an Event!</h1>
<p><a href="dashboard.py">back to dashboard</a></p>
</body>
</html>"""
remove()
print user()
