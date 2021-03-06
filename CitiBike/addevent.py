#!/usr/bin/python
import cgi,cgitb,os
cgitb.enable()
form=cgi.FieldStorage()
print("""Content-type: text/html\n\n""")
print()
#this creates a new page for an event!
#this function converts key values to dictionary
def FStoD():
    '''
    Converts cgi.FieldStorage() return value into a standard dictionary
    '''
    d = {}
    formData = cgi.FieldStorage()
    for k in formData.keys():
        d[k] = formData[k].value
    return d
#this function writes to the events.csv file, should've used parameters LOL
def csvWrite():
    fd = open('events.csv','a')
    title=FStoD()['title']
    date=FStoD()['date']
    time=FStoD()['time']
    duration=FStoD()['duration']
    size=FStoD()['size']
    description=FStoD()['description']
    description=description.replace(', ','_')
    description=description.replace('\n',' ')
    description=description.replace('\r',' ')
    type=FStoD()['type']
    if type=="volunteering": #establishes special cases
	typeCode=3
    elif type=="safetyclass":
	typeCode=1
    else:
	typeCode=2
    myCsvRow=date+","+title+","+time+","+duration+","+size+","+description+","+str(typeCode)+" \n" #writes out event to events.csv file, so that people can see it.

    fd.write(myCsvRow)
    fd.close()
    if typeCode==3: #special code to differentiate volunteerCode
	pd=open(date+'-v.py','w')
        pd.write(makePage())
        pd.close()
	os.chmod(date+'-v.py',0777)
	s=open(date+'-v-admin.py','w')
        s.write(makeAdmin())
        s.close()
        os.chmod(date+'-v-admin.py',0777)
        c=open(date+'-v.csv','w')
        c.close()
        os.chmod(date+'-v.csv',0777)
    else: #makes 3 files, one user front end, one csv for data, and one user backend
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
#makes admin (backend side)
def makeAdmin():
    date=FStoD()['date'] #the filename is the date of the event
    return """#!/usr/bin/python
import cgi,cgitb,os
cgitb.enable()
form=cgi.FieldStorage()

print('''Content-type: text/html''')
print()
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

    csvfile = open('"""+det(date)+""".csv', "r")#opens the file
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
    if '"""+FStoD()['type']+"""'!='safetyclass':
        final+="<p><b>"+str(count-"""+FStoD()['size']+""")+"</b> people are on waitlist</p>" #lists number of people who are signup up and waitlisted
    final+="<p>Remove Person(enter OSIS):<form action='rmperson.py'><input type='text' name='osis'><input type='hidden' id='file' name='file' value='"""+FStoD()['date']+"""'><input type='submit' value='deleteperson'></form></p>"
    if '"""+FStoD()['type']+"""'=='safetyclass':
	final+="<p><b>"+str(countAcceptance)+" people have been accepted</b></p>"
	final+="<p>Accept person(Enter OSIS):<form action='accept.py'><input type='text' name='osis'><input type='hidden' id='file' name='file' value='"""+FStoD()['date']+"""'><input type='hidden' name='admit' value='1'><input type='submit' value='accept'></form></p>"
        final+="<p>Reject Person(Enter OSIS):<form action='accept.py'><input type='text' name='osis'><input type='hidden' id='file' name='file' value='"""+FStoD()['date']+"""'><input type='hidden' name='admit' value='0'><input type='submit' value='reject'></form></p>"
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
print(makePage())
"""
def form(abacus): #adds options to form if this is a safety class
    if FStoD()['type']=='safetyclass':
	return """Have you used CitiBike before?<br>
<select name="firsttime" size="2">
<option value="yes">yes</option>
<option value="no">no</option></select><br>
How frequently will you use CitiBike, if you were given the opportunity to?(very frequently is defined as 2+ times a day, frequently 5 times a week, infrequently less than 3 times a week)<br>
<select name="willuse" size="3">
<option value="3">very frequently</option>
<option value="2">frequently</option>
<option value="1">infrequently</option></select><br>"""
    else:
	return ""
def det(abacus):
    if FStoD()['type']=="volunteering":
	return abacus+'-v'
    else:
	return abacus
#makes user page
def makePage():
    return """#!/usr/bin/python
import cgi,cgitb,os,csv
cgitb.enable()
form=cgi.FieldStorage()

print '''Content-type: text/html'''
print
def getnumber(): #retrieves # of people signed up
    csvfile=open('"""+det(FStoD()['date'])+""".csv','r')
    lines=csvfile.readlines()
    csvfile.close()
    counter=0
    for i in lines:
	counter+=1
    return counter"""+appendUser()+pager()
def appendUser(): #adds info to the page IF certain conditions are met
    str="""
def isFull():
    if getnumber()>"""+FStoD()['size']+""":
	return "<p><em>this is currently full! If you sign up, you will be on waitlist</em></p>"
    else:
	return ""
"""
    if FStoD()['type']=="safetyclass": #if the event is a safety class, then the waitlist message will NOT appear
	return """
def isFull():
    return ""
"""
    else:
        return str
def pager(): #returns the rest of the page
    return """
def header():
    return '''<!DOCTYPE html>
<html>
<head>
  <link rel="shortcut icon" type="image/png" href="../logo.png" />
</head>
<title>"""+FStoD()['title']+"""</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
body,h1,h2,h3,h4,h5,h6 {font-family: "Lato", sans-serif;}
body, html {
    height: 100%;
    color: #000000;
    line-height: 1.8;
}

/* Create a Parallax Effect */
.bgimg-1, .bgimg-2, .bgimg-3 {
    background-attachment: fixed;
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
}

/* First image (Logo. Full height) */
.bgimg-1 {
    background-image: url("Citi-Bike.jpg");
    min-height: 100%;
}

/* Second image (Portfolio) */
.bgimg-2 {
    background-image: url("Citi-Bike.jpg");
    min-height: 400px;
}

/* Third image (Contact) */
.bgimg-3 {
    background-image: url("IMG_2705.jpg");
    min-height: 400px;
}
.navpad {
  font-size: 20px;    
    border: none;
    outline: none;
    color: black;
    padding: 14px 16px;
    background-color: inherit;
    font-family: inherit;
    margin: 0;
  }
.centered {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}
.test {
    color:black;
}
.dropdown {
    float: left;
  overflow: hidden;
    
}

.dropdown .dropbtn {
    font-size: 20px;    
    border: none;
    outline: none;
    color: black;
    padding: 14px 16px;
    background-color: inherit;
    font-family: inherit;
    margin: 0;
}

.dropdown-content {
    display: none;
    position: fixed;
    background-color: white;
    min-width: 160px;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    z-index: 1;
}

.dropdown-content a {
    float: none;
    color: black;
    padding: 12px 16px;
    text-decoration: none;
    display: block;
    text-align: left;
}

.dropdown-content a:hover {
    background-color: #959595;
}

.dropdown:hover .dropdown-content {
    display: block;
}
.container {
    position: relative;
    text-align: center;
    color: black;
}
.w3-wide {letter-spacing: 10px;}
.w3-hover-opacity {cursor: pointer;}

/* Turn off parallax scrolling for tablets and phones */
@media only screen and (max-device-width: 1024px) {
    .bgimg-1, .bgimg-2, .bgimg-3 {
        background-attachment: scroll;
    }
}

</style>
<body>
  <!-- keep track of appearing and disappearing text in main page! -->

<!-- Navbar (sit on top) -->
  <header>
<div class="w3-top">
  <div class="w3-bar" id="myNavbar">
    <a href="../index.html" class="w3-bar-item w3-button w3-hide-small">
        <img src="logo.png" height=40 width=100>
    </a>
    <div class="dropdown">
      <button class="dropbtn"><a href="http://stuybikes.com" style="text-decoration:none">Home</a>
      <i class="fa fa-caret-down"></i>
    </button>
    <div class="dropdown-content">
      <a href="../#about">Our Mission</a>
      <a href="../#FAQ">Information</a>
      <a href="../#contact">Contact</a>
    </div>
    </div>
    <div class="dropdown">
  <button class="dropbtn"><a href="http://stuybikes.com/public_html/CitiBike/signup.html" style="text-decoration:none"><i class="fa fa-bicycle"></i>Sign up</a>
      <i class="fa fa-caret-down"></i>
    </button>
    <div class="dropdown-content">
      <a href="http://stuybikes.com/public_html/CitiBike/group.py">Group Ride</a>
      <a href="http://stuybikes.com/public_html/CitiBike/signup.py">Membership</a>
      <a href="http://stuybikes.com/public_html/CitiBike/volunteer.py">Volunteer</a>
    </div>
    </div>
    <div class="navpad">
    <a href="../CitiBike/blog.html" style="text-decoration:none" class="w3-hide-small navpad"><i class="fa fa-user"></i> BLOG</a>
      <div class="w3-right">
        <a href="myAccount" style="text-decoration:none">My Account</a>
      </div>
    </div>
        
    </div>
  </div>
  </header>

  <!-- Navbar on small screens -->
  <div id="navDemo" class="w3-bar-block w3-white w3-hide w3-hide-large w3-hide-medium">
    <a href="index.html" class="w3-bar-item w3-button w3-hide-small">
        <img src="logo.png" height=40 width=100>
    </a>
    <a href="http://stuybikes.com/public_html/CitiBike/blog.html" class=" w3-black w3-button"><i class="fa fa-user"></i> BLOG</a>
</div>
        
 <div id="body" class="w3-content w3-padding-64">
        <h1 class="w3-center">"""+FStoD()['title']+"""</h1>
        <h3 class="w3-center">You are signing up for """+FStoD()['date']+""" at """+FStoD()['time']+""" until """ +FStoD()['duration']+"""</h3>
<p>There are """+FStoD()['size']+""" spots</p>
<h3 id="event">Description</h3><p>"""+FStoD()['description']+"""</p>'''+isFull()+'''<form action="submit.py">
<br>
First Name::<input name="firstName" required="required"></input>
Last Name::<input name="lastName" required="required"></input>
<br>
<br>Birthday:<input type="date" name="date" required="required"><br>
OSIS:<input name="osis" required="required"></input><br>
Email: <input name="contact" required="required"></input><br>"""+form(FStoD()['type'])+"""
<input type="checkbox" name="terms" value="agree" required="required"> I agree that I will not hold CitiBike, Stuyvesant High School, or CitiBike X Stuy liable for any injuries resulting from this program. I understand that I have to be 16 years old to use CitiBike.<br>
<input type="hidden" id="file" name="file" value='"""+det(FStoD()['date'])+"""'>
   <button class="w3-button w3-black w3-section w3-xxlarge" type="submit">
          <i class="fa fa-bicycle"></i>Register!
        </button>
</form>
</div>
<script>
// Change style of navbar on scroll
window.onscroll = function() {myFunction()};
function myFunction() {
    var navbar = document.getElementById("myNavbar");
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        navbar.className = "w3-bar" + " w3-card" + " w3-animate-top" + " w3-white";
    } else {
        navbar.className = navbar.className.replace(" w3-card w3-animate-top w3-white", "");
    }
}
function toggleFunction() {
    var x = document.getElementById("navDemo");
    if (x.className.indexOf("w3-show") == -1) {
        x.className += " w3-show";
    } else {
        x.className = x.className.replace(" w3-show", "");
    }
}
</script>
        </body>
	
        </html>'''
print(header())"""

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
print(user())
