#!/usr/bin/python
import cgi,cgitb,os,csv
cgitb.enable()
form=cgi.FieldStorage()

print '''Content-type: text/html'''
print
def header():
    return '''<html>
        <title>r</title>
        <body>
        <h1>r</h1>
        <h3>Sign up for2001-12-19 at 12:00 until 03:00</h3>
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
<input type="hidden" id="file" name="file" value='2001-12-19'>
  <input type="submit">
</form>
<h2 id="eventmanage">Event Manager</h2>
        </body>
        </html>'''
print header()