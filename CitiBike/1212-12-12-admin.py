#!/usr/bin/python
import cgi,cgitb,os
cgitb.enable()
form=cgi.FieldStorage()

print '''Content-type: text/html'''
print
def makePage():
    return '''<!DOCTYPE html>
    <html>
    <head>
      <link rel="shortcut icon" type="image/png" href="../logo.png" />
    </head>
    <title>Console</title>
    <body>

    <h1>Admin Console for Specified Event</h1>
    <h2>If you are not an admin, please send us a message on the contact page()</h2>
<h2 id="eventmanage">Who's Going?</h2>'''+getevent()+'''
</body>
</html>
    '''
def getevent():

    csvfile = open('1212-12-12.csv', "r")#opens the file
    lines= csvfile.readlines()
    csvfile.close()
    final=' '
    count=0
    for j in lines:
	count+=1
    final+="<p><b>"+str(count)+ "</b> people are going</p>"
    count=0
    for show in lines:
        ret=show.split(",")#gives you the DATE of the Event
	for i in ret:
            ping=ret[i]
            final+=ping+" "
	    i+=1
        final+="<br>"
        count+=1
    return final
print makePage()
