#!/usr/bin/python
import random
import cgi,cgitb,os

cgitb.enable()

#the field storage is a global variable.
#Since your page has exactly one, you can
#just acccess it from anywhere in the program.
form = cgi.FieldStorage()

def header():
        return """content-type: text/html

<!DOCTYPE html>
<html>
<head>
<title>Stuy Bikes</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato">
<style>
body,h1,h2,h3,h4,h5,h6 {font-family: "Lato", sans-serif;}
body, html {
    height: 100%;
    color: #777;
    line-height: 1.8;
}

/* Create a Parallax Effect */
.bgimg-1, .bgimg-2, .bgimg-3 {
    background-attachment: fixed;
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
}
.bgimg-1 {
    background-image: url("Citi-Bike.jpg");
    min-height: 100%;
}

/* Second image (Portfolio) */
.bgimg-2 {
    background-image: url("Stuyvesant-Chambers.jpg");
    min-height: 400px;
}

/* Third image (Contact) */
.bgimg-3 {
    background-image: url("IMG_1800.jpg");
    min-height: 400px;
}
body,h1,h2,h3,h4,h5,h6 {font-family: "Lato", sans-serif;
    margin:0;
}

body {
    background-attachment: fixed;
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
}

.navbar {
  overflow: hidden;
  background-color: transparent;
  position: fixed;
  top: 0;
  width: 100%;
}

.navbar a {
  display: block;
  text-align: center;
  color: dimgray;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 17px;
}

.info {
    float:left;
    }
.info:hover {
    background-color: #d3d3d3;
    color: whitesmoke;
    }
.login {
    float:right;
    }
.register{
    float:right;
    }
.login:hover {
    background-color: #8EA2FF;
    color: whitesmoke;
    }
.register:hover {
    background-color: #FF8E8E;
    color: whitesmoke;
    }
.Name {
    margin: 12% 15% 3% 15%;
    background-color: white;
    padding: 10px;
    font-size: 30px;
    color: dimgray;
    text-align: left;
}

.address {
    margin: 0% 15% 15% 15%;
    background-color: white;
    padding: 10px;
    font-size: 20px;
    color: dimgray;
    text-align: center;
    }

.description {
    margin: 35% 15% 15% 15%;
    background-color: white;
    padding: 10px;
    font-size: 25px;
    color: dimgray;
    text-align: left;
    }

.Type {
    color: darkgray;
    float: right;
    }

.Reviews {
    margin: 10% 15% 15% 15%;
    background-color: white;
    padding: 10px;
    font-size: 25px;
    color: black;
    text-align: left;
    }

.reviewHeader {
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
</head>
<body>
<div class="navbar w3-top">"""


def footer():
    return """</div>

<div class="bgimg-1 w3-display-container w3-opacity-min" id="home">
  <div class="w3-display-middle" style="white-space:nowrap;">
    <span class="w3-center w3-padding-large w3-black w3-xlarge w3-wide w3-animate-opacity"><a href="Project/page1.py">Click to Explore</span></a>
  </div>
</div>
<div class="w3-content w3-container w3-padding-64" id="">
  <h3 class="w3-center">ABOUT THE TEAM</h3>
  <p class="w3-center"><em>Welcome to CitiBike X Stuy</em></p>
  <p>We're looking forward to bringing you free CitiBike memberships, starting september 5th<br> This homepage uses a template from w3 schools, and in other pages we will use the same thing. Hope you enjoy this website!</p>
  <div class="w3-row">
    <div class="w3-center w3-padding-large">
      <p><b><i class="fa fa-user w3-margin-center"></i>The Development Team!!!</b></p><br>
      <img src=""IMG_1800.jpg"" class="w3-round w3-image w3-opacity w3-hover-opacity-off" alt="Photo of Us" width="600" height="450">
    </div>
</body>
</html>"""


def authenticate():
    if 'user' in form and 'magicnumber' in form:
        #get the data from form, and IP from user.
        user = form['user'].value
        magicnumber = form['magicnumber'].value
        IP = 'NULL'
        if 'REMOTE_ADDR' in os.environ:
            IP = os.environ["REMOTE_ADDR"]
        #compare with file
        text = open('Login/loggedin.txt').readlines()
        for line in text:
            line = line.strip().split(",")
            if line[0]==user:#when you find the right user name
                if line[1]==magicnumber and line[2]==IP:
                    return True
                else:
                    return False
        return False#in case user not found
    return False #no/missing fields passed into field storage


#either returns ?user=__&magicnumber=__  or an empty string.
def securefields():
    if 'user' in form and 'magicnumber' in form:
        user = form['user'].value
        magicnumber = form['magicnumber'].value
        return "?user="+user+"&magicnumber="+magicnumber
    return ""

#makes a link, link will include secure features if the user is logged in
def makeLink(page, text):
    return '<a href="'+page+securefields()+'">'+text+'</a><br>'

def makeNavBar(page, name):
        return '<a class="info" href="' +page+securefields()+'">'+name+'</a>\n'
def makeLogo(page, logo):
        return '<img src="img_girl.jpg" alt="Girl in a jacket" width="100" height="50"></img>'
def NavBar():
        return makeNavBar('index.py', 'Home') + makeNavBar('Project/page1.py', 'Blog')+makeNavBar('hw','Sign Up')
def main():
    body = ""

    #determine if the user is properly logged in once.
    isLoggedIn = authenticate()

    #attach a logout link only if logged in
    if isLoggedIn:
        body+= '<a href="../index.html" class="w3-bar-item w3-button w3-hide-small w3-right w3-hover-red">LOGOUT</a>'
    else:
        body+= '''<a href="Project/Login/create.html" class="w3-bar-item w3-button w3-hide-small w3-right w3-hover-green">REGISTER</a>
    <a href="Project/Login/login.html" class="w3-bar-item w3-button w3-hide-small w3-right w3-hover-blue">LOG IN</a>'''

    #finally print the entire page.
    print header() + NavBar()+body + footer()
main()
