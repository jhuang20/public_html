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
      <!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-122645396-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-122645396-1');
</script>

    </head>
    <title>Console</title>
    <style>
#secure {
display: none;
}
</style>
    <body>
    <form id="security">
Enter Passcode:<input type="text" name="password">
</form>
<input type="button" value="Login" onclick="login()">
<div class="secure">
    <h1>Admin Console for Specified Event</h1>
    <h2>If you are not an admin, please send us a message on the contact page()</h2>
<h2 id="eventmanage">Who's Going?</h2>'''+getevent()+'''
</div>
<script>
function login() {
var x=document.getElementById("security")
if(x.elements[0].value=="CBXStuy18") {
document.getElementById("secure").style.display="block";
}
}
</script>
</body>
</html>
    '''
def getevent(): #retreives event data

    csvfile = open('RideToSchool.csv', "r")#opens the file
    lines= csvfile.readlines()
    csvfile.close()
    final=' '
    count=0
    countAcceptance=0
    for j in lines:
	count+=1
	isAccept=j.split(",")
	if isAccept[-1]=="accept /n": #counts number of acceptances(should use strip function )
	    countAcceptance+=1
    final+="<p><b>"+str(count)+ "</b> people are signed up</p>"
    if 'specialevent'!='safetyclass':
        final+="<p><b>"+str(count-100)+"</b> people are on waitlist</p>" #lists number of people who are signup up and waitlisted
    final+="<p>Remove Person(enter OSIS):<form action='rmperson.py'><input type='text' name='osis'><input type='hidden' id='file' name='file' value='RideToSchool'><input type='submit' value='deleteperson'></form></p>"
    if 'specialevent'=='safetyclass' or 'specialevent'=='specialevent':
	final+="<p><b>"+str(countAcceptance)+" people have been accepted</b></p>"
	final+="<p>Accept person(Enter OSIS):<form action='accept.py'><input type='text' name='osis'><input type='hidden' id='file' name='file' value='RideToSchool'><input type='hidden' name='admit' value='1'><input type='submit' value='accept'></form></p>"
        final+="<p>Reject Person(Enter OSIS):<form action='accept.py'><input type='text' name='osis'><input type='hidden' id='file' name='file' value='RideToSchool'><input type='hidden' name='admit' value='0'><input type='submit' value='reject'></form></p>"
    count=0 #the three lines above provide the ability to delete a person, accept a person, or reject a person. 
    final+="<table style='width:100%'>" #backend table for easy access
    final+='''<tr>
    <th>Waitlist</th>
    <th>OSIS</th>
    <th>last name</th> 
    <th>first name</th>
    <th>email</th>
    <th>birthday</th>
    <th>have used citibike b4?</th>
    <th>frequency of use?</th>
    <th> accept/reject</th>
    <th>here?(check off)</th></tr>
    '''
    for show in lines:
    	final+="<tr>"
	how=show.split(",")
	if count<25:
	    final+="<td>No</td>"
            for i in how:
            	final+="<td>"+str(i)+"</td>"
	else:
	    final+="<td>Yes</td>"
            for i in how:
            	final+="<td>"+str(i)+"</td>"
	final+="</tr>"
        count+=1

    return final
print makePage()
