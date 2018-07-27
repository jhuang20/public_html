#!/usr/bin/python
import cgi,cgitb,os
cgitb.enable()
form=cgi.FieldStorage()

print """Content-type: text/html"""
print

def getEvent():#gets event DATE
    csvfile = open("events.csv", "r")#opens the file
    lines= csvfile.readlines()
    csvfile.close()
    final='  <div class="w3-row-padding w3-center w3-text-black">'
    counter=0
    for row in lines:
        ret=row.split(",")#gives you the DATE of the Event
        ping=ret[0]
        final+="""
<div class="w3-col m3 container w3-text-black">"""
        if int(ret[5])==3:
            final+="""<a href="""+ping+"""-v-admin.py>"""+str(ret)+"""</a>"""
        else:
            final+="""<a href="""+ping+"""-admin.py>"""+str(ret)+"""</a>"""
        final+="""<form action="remove.py">
<input type="hidden" id="file" name="file" value='"""+str(ping)+"""'>
  <input type="submit" value="Delete Event">
</form></div>
        """
        counter+=1
    return final+"</div>"

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
<h2><a href="http://stuybikes.com">LINK TO MAIN PAGE</a></h2>
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
Title::<input name="title" required="required"></input>
<br>
<select name="type" size="3" required="required">
  <option value="volunteering">Volunteering</option>
  <option value="safetyclass">Safety Class</option>
  <option value="groupride">Group Ride</option>
  </select>
<br>Pick a date:<input type="date" name="date" required="required"><br>
Pick a start time(format 00:00 (24hr clock)):<input name="time" required="required"></input><br>
Endtime(format 00:00, hh:mm): <input name="duration" required="required"></input><br>
Capacity: <input name="size"></input><br>
Description:<textarea name="description" rows="10" cols="30">This is an Event Description...</textarea><br>
  <input type="submit">
</form>
<h2 id="eventmanage">Event Manager</h2>"""+getEvent()+"""
</body>
</html>
    """

#prints other part of GUI interface
#def footer():

print main()
