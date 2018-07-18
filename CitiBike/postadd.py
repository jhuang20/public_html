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

def csvWrite():
    fd = open('events.csv','a')
    title=FStoD()['title']
    date=FStoD()['date']
    time=FStoD()['time']
    duration=FStoD()['duration']
    size=FStoD()['size']
    myCsvRow=""+date+""+","+" "+title+" "+","+" "+time+","+duration+","+size+" \n"

    fd.write(myCsvRow)
    fd.close()
    pd=open(date+'.py','w')
    pd.write(makePage())
    pd.close()
    os.chmod(date+'.py', 0777)
    s=open(date+'-admin.py','w')
    s.write(makeAdmin())
    s.close()
    os.chmod(date+'-admin.py',0777)
    c=open(date+'.csv','w')
    c.close()
    os.chmod(date+'.csv',0777)
def makeAdmin():
    return """#!/usr/bin/python
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

        final=''.join(readlines("events.csv"))+'''<br><p> <b>Master Event List(temp)</b></p>'''
        return final
print makePage()
"""

def makePage():
    return """#!/usr/bin/python
import cgi,cgitb,os,csv
cgitb.enable()
form=cgi.FieldStorage()

print '''Content-type: text/html'''
print
def header():
    return '''<html>
        <title>"""+FStoD()['title']+"""</title>
        <body>
        <h1>"""+FStoD()['title']+"""</h1>
        <h3>Sign up for"""+FStoD()['date']+""" at """+FStoD()['time']+""" until """ +FStoD()['duration']+"""</h3>
<h3 id="event">Fill out this form!</h3>
<form action="submit.py">
<br>
First Name::<input name="firstName"></input>
Last Name::<input name="lastName"></input>
<br>
<br>Birthday:<input type="date" name="date"><br>
OSIS:<input name="osis"></input><br>
Email: <input name="contact"></input><br>
Other Comments:<input name="q">test</input><br>
<input type="hidden" id="file" name="file" value='"""+FStoD()['date']+"""'>
  <input type="submit">
</form>
<h2 id="eventmanage">Event Manager</h2>
        </body>
        </html>'''
print header()"""

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
csvWrite()
print user()
