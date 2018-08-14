#!/usr/bin/python
import cgi,cgitb,os,csv
cgitb.enable()
form=cgi.FieldStorage()
globs='null'  #personalization, says hi to you!
numero=0 #if num is 1, adds specific message for safety class
admit=0
print '''Content-type: text/html'''
print

def FStoD():
    '''
    Converts cgi.FieldStorage() return value into a standard dictionary
    '''
    d = {}
    formData = cgi.FieldStorage()
    for k in formData.keys():
        d[k] = formData[k].value
    return d
def getType(num):
    if num==3:
	global numero
	numero=0
	return "volunteer"
    if num==2:
	global numero
	numero=0
        return "group ride"
    if num==1:
	global numero
	numero=1
	return "safety class(membership)"
    else:
	return "application"
def getStatus(counter,line):
    p=line #which row in csv file
    csvfile=open("../CitiBike/events.csv","r")
    lines=csvfile.readlines()
    csvfile.close()
    ping=0
    currentLoc=0
    for row in lines:
	if currentLoc==line:
	    ret=row.split(",")
	    ping=int(ret[4]) #returns capacity
	    break
	else:
	    currentLoc+=1
    if admit==2 and numero==1:
	global admit
	admit=0
	return "accepted, monitor email"
    if admit==3 and numero==1:
	global admit
	admit=0
	return "rejected"
    if numero==1:
	return "pending, check email and the status page"
    if ping<int(counter):
	return "waitlisted, you will be emailed if accepted, check this page periodically"+str(ping)
    else:
	return "accepted, monitor email"
def getDetail(name):
    return "Hi,"+name
def getevent():
    fill=""
    csvfile = open("../CitiBike/events.csv", "r")#opens the file
    lines= csvfile.readlines()
    csvfile.close()
    counter=0
    rowC=0
    for row in lines:#look at each event, see if there is a match
        ret=row.split(",")#gives you the DATE of the Event
        ping=ret[0]
        vfile= open("../CitiBike/"+ping+".csv","r")#opens csv of THIS file
        vline=vfile.readlines()
	vfile.close()
        counter=0 #counts the number of people there are
        for person in vline:
            per=person.split(",")#gives you list of OSIS
            osisM=per[0]
            if FStoD()['osis']==osisM:
		if str(per[-1])=='accept \n':
		    global admit
		    admit=2
		if str(per[-1])=='reject \n':
		    global admit
		    admit=3
	        global globs
	        if globs=='null':
	            global globs
	            globs=getDetail(per[2])
		    break
                fill+="<tr><td>"+ret[0]+"</td><td> "+getType(int(ret[6]))+"</td><td>"+ret[2]+"</td><td>"+getStatus(int(counter),int(rowC))+"</td>"
                fill+="<td><form action='rmperson.py'><input type='hidden' id='osis' name='osis' value='"+FStoD()['osis']+"'><input type='hidden' id='file' name='file' value="+ret[0]+"><input type='submit' value='De-register for event'></form></td></tr>"
            counter+=1
        rowC+=1
    if fill=="":
        return "no events found"
    else:
        return fill
print '''<!DOCTYPE html>
<html>
<head>
  <link rel="shortcut icon" type="image/png" href="../logo.png" />
</head>
<title>Your Profile</title>
<meta charset="UTF-8">
<div hidden>'''+getevent()+'''</div>
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
    padding: 14px 15px;
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
        <a href="../myAccount" style="text-decoration:none">My Account</a>
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
        <h1 class="w3-center">Event Schedule for '''+FStoD()['osis']+'''</h1>
        <h3 class="w3-center">You can remove events here, and also see all the events you have signed up for. You will also be able to see whether you have been accepted for positions/selective classes(in a future update)</h3>
        <h4>'''+globs+'''</h4>
        <h4>Events</h4><table style="width:100%"><tr><th>date</th><th>type</th><th>start time</th><th>status</th><th>delete event</th></tr><p>'''+getevent()+'''</table>
 </div>
<script>
// Change style of navbar on scroll
window.onscroll = function() {myFunction()};
function myFunction() {
    var navbar = document.getElementById("myNavbar");
    if (document.body.scrollTop > 25 || document.documentElement.scrollTop > 25) {
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
        </body>'''
