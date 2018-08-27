#!/usr/bin/python
import cgi,cgitb,os
cgitb.enable()
form=cgi.FieldStorage()

print """Content-type: text/html"""
print
print """
<!DOCTYPE html>
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
<title>FAQ</title>
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
    <a href="index.html" class="w3-bar-item w3-button">
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

<!-- First Parallax Image with Logo Text -->
<div class="bgimg-1 w3-display-container w3-opacity-min" id="home">
  <div class="w3-display-middle">
    <!-- keep track of appearing and disappearing text in main page! -->
    <div class="w3-display-middle">
      <span class="w3-xxlarge w3-text-white w3-wide">Frequently Asked Questions</span>
    </div>




  </div>

    <!--<span class="w3-center w3-padding-large w3-xlarge w3-wide w3-animate-opacity"><img src="logo.png" height=100 width=250>-->
  </div>
</div>

<!-- Container (About Section) -->
<div class="w3-content w3-container w3-padding-64" id="about">
  <h3 class="w3-center">Choose a Topic</h3>
  <p class="w3-center"><em>As of now, this page is still in beta. Sorry!</em></p>
  <p><p class="w3-xlarge">Q: How long will it be free for?</p><br>
A: The entire 2018-2019 School year, and possibly even longer.<br>
<p class="w3-xlarge">Q: How can I sign up?</p><br>
A: The administration and I have agreed that everyone who wants to have a free membership will need to take a safety class, both to obtain practical skill and knowledge about CitiBike. While it may sound stupid and unnecessary, any injury can end this program(this is, after all, a pilot program). Upon completion of the safety class, you will recieve free swag, a helmet, and access to CitiBike 100% free 24/7/365.
<p class="w3-xlarge">Q: How long will the safety class be?</p><br>
A; Around 3 hours. The first hour or so will be lecture based, the next 2 hours will be a fun group ride/ practicing the skills you've learned. These classes would be 25 people each, and would be held on weekends and off days in September and perhaps October. A more detailed schedule will come out in August.
<p class="w3-xlarge">Q: Is it SAFE to ride?</p><br>
A: Yes. Especially after taking a safety class, it is safe to ride a bike on NYC streets. Just be careful and signal your turns! In fact, only 3 people have been killed by CitiBikes out of over 15 million rides.
<br><p class="w3-xlarge">Q: If I'm an alumni/adult connected to the school, can I access the same program?</p>
A: That's something we're still working on.
<br><p class="w3-xlarge">Q: What's the future of this program?</p>
A: Assuming this program is highly utilized, its possible that the NYCDOE Office of Pupil Transportation will subsidize this in an "opt-in" program. This would allow for free access for ANY NYC High School Student, assuming they opt in. </p>



<!-- Footer -->
<footer class="w3-center w3-black w3-padding-64">
  <a href="#home" class="w3-button w3-light-grey"><i class="fa fa-arrow-up w3-margin-right"></i>To the top</a>
  <div class="w3-xlarge w3-section">
    <a href="https://www.facebook.com/stuycommutes/"><i class="fa fa-facebook-official w3-hover-opacity"></i></a>

  </div>
  <p>Powered by <a href="https://www.w3schools.com/w3css/default.asp" title="W3.CSS" target="_blank" class="w3-hover-text-green">w3.css</a></p>
</footer>

<!-- Add Google Maps -->
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

</body>
</html>


"""
