#!/usr/bin/python
import cgi,cgitb,os
cgitb.enable()
form=cgi.FieldStorage()

print """Content-type: text/html"""
print
#The ADMIN user will be able to add events
#Adds event
#def eventAdd():

#form for adding blog posts
#def postAdd():
def getevent():

        final=''.join(readlines("events.csv"))+"""<br><p> <b>Master Event List(temp)</b></p>"""
        return final

#gets message, email, and ADMIN can use it to send a message back via. email
def getmessage():
        final=''.join(readlines("../document.csv"))+"""<br><p> <b>no further messages!</b></p>"""
        return final
def readlines(File):
    csvfile = open(File, "r")#opens the file
    lines = csvfile.readlines()#returns single line by single line
    csvfile.close()
    return lines #returns line by line


#prints dashboard GUI interface
def main():
    return """<!DOCTYPE html>
    <html>
    <head>
      <link rel="shortcut icon" type="image/png" href="../logo.png" />
    </head>
    <title>Dashboard</title>
    <body>

    <h1>Control Center</h1>
    <h2>If you are not an admin, please send us a message on the contact page()</h2>
    <p><a href="#blog">Make blog post</a></p><p><a href="#msg">Look at MSG</a></p><p><a href="#event">Create event</a></p><p><a href="#eventmanage">Manage Event</a></p>
<h2><a href="http://homer.stuy.edu/~jhuang20">LINK TO MAIN PAGE</a></h2>
    <h3 id="blog">Make a Blog Post</h3>
    <h4>NOTE: you cannot delete blog posts</h4>
    <form action="eventadd.py">
    <br>
    Title:<input name="title"></input>
    <br>
  <textarea name="content" rows="10" cols="30">update!</textarea>
  <br>
  Tag:<input name="tag"></input>
  <br>
  <input type="submit">
</form><br><h2 id="msg"> Message Dashboard</h2>"""+getmessage()+"""
<h3 id="event">Make an Event</h3>
<form action="postadd.py">
<br>
Title::<input name="title"></input>
<br>
<select name="type" size="2" multiple>
  <option value="volunteering">Volunteering</option>
  <option value="safetyclass">Safety Class</option>
  </select>
<br>Pick a date:<input type="date" name="date"><br>
Pick a start time(format 00:00 (24hr clock)):<input name="time"></input><br>
Endtime(format 00:00, hh:mm): <input name="duration"></input><br>
  <input type="submit">
</form>
<h2 id="eventmanage">Event Manager</h2>"""+getevent()+"""
</body>
</html>
    """

#prints other part of GUI interface
#def footer():

print main()
