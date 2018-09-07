#!/usr/bin/python
import cgi,cgitb,os,csv
cgitb.enable()
form=cgi.FieldStorage()

print '''Content-type: text/html'''
print
def getnumber(): #retrieves # of people signed up
    csvfile=open('ITDirectorApplications.csv','r')
    lines=csvfile.readlines()
    csvfile.close()
    counter=0
    for i in lines:
	counter+=1
    return counter
def isFull():
    if getnumber()>1 :
	return "<p><em>this is currently full! If you sign up, you will be on waitlist</em></p>"
    else:
	return ""

def header():
    return '''<!DOCTYPE html>
<html>
<head>
  <link rel="shortcut icon" type="image/png" href="../logo.png" />
</head>
<title>IT Director Applications</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
body,h1,h2,h3,h4,h5,h6 {font-family: "Calibri", sans-serif;}
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
    background-image: url("IMG_4078.jpg");
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
.topnav {
  overflow: hidden;
  background-color: white;
}

.topnav a {
  float: left;
  display: block;
  color: black;
  text-align: center;
  padding: 8px 10px;
  text-decoration: none;
  font-size: 20px;
}

.active {
  background-color: white;
  color: black;
}

.topnav .icon {
  display: none;
}

.dropdown {
    float: left;
    overflow: hidden;
}

.dropdown .dropbtn {
    font-size: 17px;    
    border: none;
    outline: none;
    color: black;
    padding: 0px 10px;
    background-color: inherit;
    font-family: inherit;
    margin: 0;
}

.dropdown-content {
    display: none;
    position: absolute;
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

.topnav a:hover, .dropdown:hover .dropbtn {
  background-color: white;
  color: black;
}

.dropdown-content a:hover {
    background-color: white;
    color: black;
}

.dropdown:hover .dropdown-content {
    display: block;
}

@media screen and (max-width: 600px) {
  .topnav a:not(:first-child), .dropdown .dropbtn {
    display: none;
  }
  .topnav a.icon {
    float: right;
    display: block;
  }
}

@media screen and (max-width: 600px) {
  .topnav.responsive {position: relative;}
  .topnav.responsive .icon {
    position: absolute;
    right: 0;
    top: 0;
  }
  .topnav.responsive a {
    float: none;
    display: block;
    text-align: left;
  }
  .topnav.responsive .dropdown {float: none;}
  .topnav.responsive .dropdown-content {position: relative;}
  .topnav.responsive .dropdown .dropbtn {
    display: block;
    width: 100%;
    text-align: left;
  }
}
.centered {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}
.container {
    position: relative;
    text-align: center;
    color: white;
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
  <div class="w3-top">
<div class="topnav" id="myNavbar">
    <a href="../index.html" class="w3-bar-item w3-button">
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
      <a href="http://stuybikes.com/public_html/CitiBike/group.py">Group Rides/Day Pass</a>
      <a href="http://stuybikes.com/public_html/CitiBike/signup.py">Safety Classes/Membership</a>
      <a href="http://stuybikes.com/public_html/CitiBike/volunteer.py">Special Events/Positions</a>
    </div>
    </div>
    
    <a href="http://stuybikes.com/public_html/CitiBike/blog.html" style="text-decoration:none" class=""><i class="fa fa-user"></i> Blog</a>
      
        <a href="myAccount" style="text-decoration:none text-align:right">My Events</a>
 <a href="javascript:void(0);" style="font-size:15px;" class="icon" onclick="myFunction()"><i class="fa fa-bars"></i></a>
    
        
  </div>
  </div>
        
 <div id="body" class="w3-content w3-padding-64">
        <h1 class="w3-center">IT Director Applications</h1>
        <h3 class="w3-center">You are signing up for 2018-09-07 at N/A until N/A</h3>
<p>There are 1  spots</p>
<h3 id="event">Description</h3><p>Hey guys,

We're looking for a new IT Director to help manage our website! Experience with Python, JavaScript, HTML, and Databases is required. The time commitment of this position will be medium. Contact us here or on our Facebook page with any questions. </p>'''+isFull()+'''<form action="submit.py">
<br>
First Name::<input name="firstName" required="required"></input>
Last Name::<input name="lastName" required="required"></input>
<br>
<br>Birthday:<input type="date" name="date" required="required"><br>
OSIS:<input name="osis" required="required"></input><br>
Email: <input name="contact" required="required"></input><br>Describe the experience you've had with Python/JavaScript/HTML/Databases.<br><textarea name='q1' rows='10' cols='50'>Type Your Response Here</textarea><br><br>What are your other time commitments? When will you be available?<br><textarea name='q2' rows='10' cols='50'>Type Your Response Here</textarea><br>
<input type="checkbox" name="terms" value="agree" required="required"> I agree that I will not hold CitiBike, Stuyvesant High School, or CitiBike X Stuy liable for any injuries resulting from this program. I understand that I have to be 16 years old to use CitiBike.<br>
<input type="hidden" id="file" name="file" value='ITDirectorApplications'>
   <button class="w3-button w3-black w3-section w3-xxlarge" type="submit">
          <i class="fa fa-bicycle"></i>Register!
        </button>
</form>
</div>
<script>
function myFunction() {
    var x = document.getElementById("myNavbar");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}
</script>
<script>
// Change style of navbar on scroll

</script>
        </body>
	
        </html>'''
print header()