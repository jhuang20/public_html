#!/usr/bin/python
import cgi,cgitb,os,csv
cgitb.enable()
form=cgi.FieldStorage()

print """Content-type: text/html"""
print
#main printing function
def getmessage():
    return ''.join(readlines("events.csv"))+"""<br><p> <b>Master Event List(temp)</b></p>"""

def readlines(File):
    csvfile = open(File, "r")#opens the file
    lines = csvfile.readlines()#returns single line by single line
    csvfile.close()
    return lines #returns line by line
def getevent(row):
    csvfile = open("events.csv", "r")#opens the file
    lines= csvfile.readlines()
    csvfile.close()
    final=' '
    counter=row
    count=0

    for show in lines:
        if count==counter:
            ret=show.split(",")#gives you the DATE of the Event
            ping=ret[0]
            final+=ping
        else:
            count+=1
    return final
def getEventCSV():#gets event DATE
    csvfile = open("events.csv", "r")#opens the file
    lines= csvfile.readlines()
    csvfile.close()
    final='  <div class="w3-row-padding w3-center w3-text-black">'
    counter=0
    for row in lines:
        ret=row.split(",")#gives you the DATE of the Event
        num=ret[6]
        num=num.strip('\n')
        check=int(num)
        if check==1:
            ping=ret[0]
            final+="""
<div class="w3-col m3 container w3-text-black">
        <a href="""+ping+""".py><button class="w3-button w3-black  w3-section" onmouseover="expand("""+str(counter)+""")">"""+ping+"""</button></a></div>
        """
        counter+=1
    return final+"</div>"
def getEvent():
    return ""
def main():
    return """
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
<title>Sign Up</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
body,h1,h2,h3,h4,h5,h6 {font-family: "Lato", sans-serif;}
body, html {
    height: 100%;
    color: black;
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
    background-image: url("../Citi-Bike.jpg");
    min-height: 100%;
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
  <div class="w3-bar" id="myNavbar">
    <a class="w3-bar-item w3-button w3-hover-black w3-hide-medium w3-hide-large w3-right" href="javascript:void(0);" onclick="toggleFunction()" title="Toggle Navigation Menu">
      <i class="fa fa-bars"></i>
    </a>
    <a href="../index.html" class="w3-bar-item w3-button w3-hide-small">
        <img src="../logo.png" height=40 width=100>
    </a>
    <a href="../index.html" class="w3-black  w3-button">HOME</a>
    <a href="../CitiBike/signup.html" class="w3-black w3-button w3-hide-small"><i class="fa fa-bicycle"></i> SIGN UP</a>
    <a href="../CitiBike/blog.html" class=" w3-black w3-button w3-hide-small"><i class="fa fa-user"></i> BLOG</a>
    <a href="../index.html#FAQ" class="w3-black w3-button w3-hide-small"><i class="fa fa-question"></i> INFORMATION </a>
    <a href="../#contact" class="w3-black w3-button w3-hide-small"><i class="fa fa-envelope"></i> CONTACT</a>

  </div>

  <!-- Navbar on small screens -->
  <div id="navDemo" class="w3-bar-block w3-white w3-hide w3-hide-large w3-hide-medium">
    <a href="../index.html" class="w3-bar-item w3-button w3-hide-small">
        <img src="logo.png" height=40 width=100>
    </a>
    <a href="../#home" class="w3-black  w3-button">HOME</a>
<a href="../#about" class="w3-black w3-button "><i class="fa fa-building"></i> OUR MISSION</a>
    <a href="../CitiBike/signup.html" class="w3-black w3-button "><i class="fa fa-bicycle"></i> SIGN UP</a>
    <a href="../CitiBike/blog.html" class=" w3-black w3-button "><i class="fa fa-user"></i> BLOG</a>
    <a href="../#FAQ" class="w3-black w3-button "><i class="fa fa-question"></i> Information </a>
    <a href="../#contact" class="w3-black w3-button "><i class="fa fa-envelope"></i> CONTACT</a>
  </div>
</div>

<!-- First Parallax Image with Logo Text -->
<div class="bgimg-1 w3-display-container w3-opacity-min" id="home">
  <div class="w3-display-middle">
    <!-- In the future, have tags and various types of posts -->
    <div class="w3-display-middle">
      <span class="w3-xxlarge w3-animate-opacity w3-text-white w3-wide">Signup here!</span>
    </div>




  </div>

    <!--<span class="w3-center w3-padding-large w3-xlarge w3-wide w3-animate-opacity"><img src="logo.png" height=100 width=250>-->
  </div>
</div>

<!-- Container (About Section) -->
<div class="w3-content w3-container w3-padding-64" id="about">
  <h3 class="w3-center w3-xxlarge">Choose an available class!</h3>
  <p class="w3-center"><a href="blog.html#StaySafe"><em>Why do I have to take a safety class?</em></a></p>
  """+getEventCSV()+"""<div class="w3-row-padding w3-center w3-text-white">"""+"""</div><div class="w3-content w3-container" id="choose">
<div id="attrib">
</div>

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
</script>
<script>
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
</html>


"""

print main()
