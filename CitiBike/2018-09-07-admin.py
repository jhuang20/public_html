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

    csvfile = open('2018-09-07.csv', "r")#opens the file
    lines= csvfile.readlines()
    csvfile.close()
    final=' '
    count=0
    for j in lines:
	count+=1
    final+="<p><b>"+str(count)+ "</b> people are signed up</p>"
    final+="<p><b>"+str(count-75)+"</b> people are on waitlist</p>"
    count=0
    for show in lines:
	if count<75:
            ret=show.split(",")#gives you the DATE of the Event
            final+=str(show)
	    final+="<br>"
	else:
	    final+="<b>WAITLIST</b>"+str(show)
	final+="<br>"
        count+=1

    return final
print makePage()