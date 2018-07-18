#!/usr/bin/python
import cgi,cgitb,os,csv
cgitb.enable()
form=cgi.FieldStorage()

print '''Content-type: text/html'''
print
def getnumber():
    csvfile=open('1212-12-12.csv','r')
    lines=csvfile.readlines()
    csvfile.close()
    counter=0
    for i in lines:
	counter+=1
    return counter
def header():
    return '''<html>
        <title>Stuybikes!</title>
        <body>
        <h1>Stuybikes!</h1>
        <h3>Sign up for1212-12-12 at 12:00 until 03:00</h3>
<p>There are'''+str(25-getnumber())+'''  spots available out of  25</p>
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
<input type="hidden" id="file" name="file" value='1212-12-12'>
  <input type="submit">
</form>
<h2 id="eventmanage">Event Manager</h2>
        </body>
        </html>'''
print header()