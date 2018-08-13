#!/usr/bin/python
import cgi,cgitb,os,csv
cgitb.enable()
form=cgi.FieldStorage()

print '''Content-type: text/html'''
print
def getnumber():
    csvfile=open('2018-08-27.csv','r')
    lines=csvfile.readlines()
    csvfile.close()
    counter=0
    for i in lines:
	counter+=1
    return counter
def isFull():
    if getnumber()>25:
	return "<p><em>this is currently full! If you sign up, you will be on waitlist</em></p>"
    else:
	return ""
def header():
    return '''<!DOCTYPE html>
<html>
<head>
  <link rel="shortcut icon" type="image/png" href="../logo.png" />
</head>
<title>Stuybikes!</title>
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
        <h1 class="w3-center">Stuybikes!</h1>
        <h3 class="w3-center">You are signing up for 2018-08-27 at 12:00 until 03:00</h3>
<p>There are '''+str(25-getnumber())+'''  spots available out of  25</p>
<h3 id="event">Description</h3><p>"Stuybikes!" is a 3 hour comprehensive safety course taught by experienced instructors. Participants will learn all about using CitiBike, road riding, and safety tips, and will get to practice these skills in a group ride//a controlled environment. Upon completion of the course, participants will recieve a helmet, some swag, and of course a FREE CitiBike annual membership(Normal Price:$169). Priority will be given to those who haven't used CitiBike in the past, and those who will likely use CitiBike frequently.</p>'''+isFull()+'''<form action="submit.py">
<br>
First Name::<input name="firstName" required="required"></input>
Last Name::<input name="lastName" required="required"></input>
<br>
<br>Birthday:<input type="date" name="date" required="required"><br>
OSIS:<input name="osis" required="required"></input><br>
Email: <input name="contact" required="required"></input><br>Have you used CitiBike before?<br>
<select name="firsttime" size="2">
<option value="yes">yes</option>
<option value="no">no</option></select><br>
How frequently will you use CitiBike, if you were given the opportunity to?(very frequently is defined as 2+ times a day, frequently 5 times a week, infrequently less than 3 times a week)<br>
<select name="willuse" size="3">
<option value="3">very frequently</option>
<option value="2">frequently</option>
<option value="1">infrequently</option></select><br>
<input type="checkbox" name="terms" value="agree" required="required"> I agree that I will not hold CitiBike, Stuyvesant High School, or CitiBike X Stuy liable for any injuries resulting from this program. I understand that I have to be 16 years old to use CitiBike.<br>
<input type="hidden" id="file" name="file" value='2018-08-27'>
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
print header()
