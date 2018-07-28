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
    <body>

    <h1>Admin Console for Specified Event</h1>
    <h2>If you are not an admin, please send us a message on the contact page()</h2>
<h2 id="eventmanage">Who's Going?</h2>'''+getevent()+'''
</body>
</html>
    '''
def getevent():

    csvfile = open('2018-08-27.csv', "r")#opens the file
    lines= csvfile.readlines()
    csvfile.close()
    final=' '
    count=0
    for j in lines:
	count+=1
    final+="<p><b>"+str(count)+ "</b> people are signed up</p>"
    final+="<p><b>"+str(count-25)+"</b> people are on waitlist</p>"
    count=0
    final+="<table style='width:100%'>"
    final+='''<tr>
    <th>Delete Person</th>
    <th>Waitlist</th>
    <th>OSIS</th>
    <th>last name</th> 
    <th>first name</th>
    <th>email</th>
    <th>birthday</th>
    <th>first time?</th>
    <th>here?(check off)</th></tr>
    '''
    for show in lines:
    	final+="<tr>"
	how=show.split(",")
	if count<25:
	    final+="<td><form action='rmperson.py'><input type='hidden' name='file' value='2018-08-27'></input><input type='hidden' name='osis' value="+how[0]+"></input><input type='submit' value='deleteperson'></input></td>"
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
