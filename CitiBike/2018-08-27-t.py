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
<div id="secure">
    <h1>Admin Console for Specified Event</h1>
    <h2>If you are not an admin, please send us a message on the contact page()</h2>
<h2 id="eventmanage">Who's Going?</h2>'''+getevent()+'''
</div>
<script>
function login() {
var x=document.getElementById("security");
if(x.elements[0].value=="CBXStuy18"){
document.getElementById("secure").style.display="block";
}
}
</script></body>
</html>
    '''
def getevent():

    csvfile = open('2018-08-27.csv', "r")#opens the file
    lines= csvfile.readlines()
    csvfile.close()
    final=' '
    final+="<form action='close.py'><input type='hidden' id='file' name='file' value='2018-08-27'><input type='submit' value='Close Form'></form>"
    final+="<form action='confirm.py'><input type='hidden' id='file' name='file' value='2018-08-27'><input type='submit' value='View Roster'></form>"
    count=0
    countAcceptance=0
    countConfirm=0
    countWaitlist=0
    for j in lines:
	count+=1
	meow=j.split(",")
	if str(meow[-1])=="accept \n":
	    countAcceptance+=1
	if str(meow[-1])=="confirm \n":
	    countConfirm+=1
	    final+=str(meow[3])+"<br>"
	if str(meow[-1])=="waitlist \n" or str(meow[-1])=="waitlist\n":
	    countWaitlist+=1
    final+="<p><b>"+str(count)+ "</b> people are signed up</p>"
    final+="<p><b>"+str(countAcceptance)+"</b> people have been accepted </p>"
    final+="<p><b>"+str(countConfirm)+"</b> people have been CONFIRMED</p>"
    final+="<p><b>"+str(countWaitlist)+"</b> people have been waitlisted</p>"
    final+="<p>Remove Person(enter OSIS):<form action='rmperson.py'><input type='text' name='osis'><input type='hidden' id='file' name='file' value='2018-08-27'><input type='submit' value='deleteperson'></form></p>"
    final+="<p>Accept person(Enter OSIS):<form action='accept.py'><input type='text' name='osis'><input type='hidden' id='file' name='file' value='2018-08-27'><input type='hidden' name='admit' value='1'><input type='submit' value='accept'></form></p>"
    final+="<p>APPROVE person(Enter OSIS):<form action='accept.py'><input type='text' name='osis'><input type='hidden' id='file' name='file' value='2018-08-27'><input type='hidden' name='admit' value='2'><input type='submit' value='approve'></form></p>"
    final+="<p>Reject Person(Enter OSIS):<form action='accept.py'><input type='text' name='osis'><input type='hidden' id='file' name='file' value='2018-08-27'><input type='hidden' name='admit' value='0'><input type='submit' value='reject'></form></p>"
    count=0
    final+="<table style='width:100%'>"
    final+='''<tr>
    <th>Waitlist</th>
    <th>OSIS</th>
    <th>last name</th> 
    <th>first name</th>
    <th>email</th>
    <th>birthday</th>
    <th>have used citibike before?</th>
    <th>frequency of use?</th>
    <th>accept/reject</th>
    <th>here?(check off)</th></tr>
    '''
    for show in lines:
    	final+="<tr>"
	counter=0
	how=show.split(",")
	if count<25:
	    final+="<td>No</td>"
	    counter=0
            for i in how:
	        if counter<7:
            	    final+="<td>"+str(i)+"</td>"
		else:
		    final+="<td>"+str(how[-1])+"</td>"
		    break
	        counter+=1
	else:
	    final+="<td>Yes</td>"
	    counter=0
            for i in how:
	        if counter<7:
            	    final+="<td>"+str(i)+"</td>"
		else:
		    final+="<td>"+str(how[-1])+"</td>"
		    break
		counter+=1
	if counter<7:
	    final+="<td>pending</td>"
	final+="</tr>"
	#final+="<td><form action='accept.py'><input type='hidden' name='osis' value='"+how[0]+"'><input type='hidden' name='file' value='2018-08-27'><input type='hidden' name='accept' value='1'><input type='submit' value='accept'></form></td>"
	#final+="<td><form action='accept.py'><input type='hidden' name='osis' value='"+how[0]+"'><input type='hidden' name='file' value='2018-08-27'><input type='hidden' name='accept' value='0'><input type='submit' value='reject'></td></tr>"
        count+=1

    return final
print makePage()
