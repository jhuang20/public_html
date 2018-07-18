#!/usr/bin/python
import random
import cgi,cgitb,os
import glob

lists= glob.glob("Landmarks/*.html")

#the field storage is a global variable.
#Since your page has exactly one, you can
#just acccess it from anywhere in the program.
form = cgi.FieldStorage()
def FStoD():
    '''
    Converts cgi.FieldStorage() return value into a standard dictionary
    '''
    d = {}
    formData = cgi.FieldStorage()
    for k in formData.keys():
        d[k] = formData[k].value
    return d
d=FStoD()#this is the dictionary of query strings

def header():
        return """content-type: text/html

    
<!DOCTYPE html>
<html>
<head>
<title>Stuy Tourism!!</title>
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
    background-image: url(https://www.jimcutler.com/wp-content/uploads/2015/06/Cutler-2015-06-21-untitled-187-Edit_1000-960x619.jpg);
    min-height: 100%;
}

/* Second image (Portfolio) */
.bgimg-2 {
    background-image: url("Stuyvesant-Chambers.jpg");
    min-height: 400px;
}

/* Third image (Contact) */
.bgimg-3 {
    background-image: url("test_blur.jpg");
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
  background-color: white;
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
<div class="navbar w3-top">
   """


def extractname():
    returnStr=''
    for i in lists:
        f=open(i,"r")
        s=f.read()
        f.close()
        x=s.find('input type="hidden"')
        z=s.find('">',x,x+175)
        returnStr+='<tr><td><a href="'+i+securefields()+'">'+s[x+39:z]+'</a></td>'
        
        b=s.find('class="Type"')
        returnStr+='<td>'+s[b+13:s.find('</span>',b,b+175)]+'</td><tr>\n'
        
        
    return returnStr


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
def NavBar():
        return makeNavBar('../index.html', 'Home') + makeNavBar('page1.py', 'Places')+'<a class="info" href="#search">Search</a><a class="info" href="#list">Landmarks</a><a class="info" href="#landmarkadd">Add Landmark</a>'
if authenticate():
    floof='<input type="submit" name="Submit">'
else:
    floof='<p class="w3-red">Please <a href="Login/login.html">Login</a> to complete this form</p>'

def footer():
    return '''  </div>


<div class="bgimg-1 w3-display-container w3-opacity-min" id="home" usemap="#attractionsmap">
<map name="attractionsmap">
<area shape="circle" coords="0,0,1000" href="landmarktemplate.html">
</map>

  <div class="w3-display-middle" id="#search" style="white-space:nowrap;">
    <span class="w3-center w3-padding-large w3-xlarge w3-wide w3-animate-opacity"><form name="search" method="GET" action="search.py'''+securefields()+'''">
<input type="text" name="query">
<input type="submit" name="Search" value="Search">
</form>
</span>
  </div>
</div>
<div class="w3-content w3-container w3-padding-64" id="list">

<h3 class="w3-center">List of Landmarks</h3>
<table class="w3-center w3-table-all"><tr><th>Landmark Name</th><th>Type</th></tr>
'''+extractname()+'''</table><br>

<h3 class="w3-center" id="landmarkadd">Add Landmark(Login Necessary)</h3>
<p class="w3-center"><em>Here You can Add Landmarks</em></p>
<div class="w3-center">
<p>Just input the values in the form</p>
<br>
<form name="input" method="GET" action="makePage.py'''+securefields()+'''">
<b>Name of landmark: </b><br>
<input type="text" name="landmark_name"><br>
<b>Type of landmark:</b><br>
<input type="radio" name="type" value="skyscraper">skyscraper<br>
<input type="radio" name="type" value="park">park<br>
<input type="radio" name="type"
value="activity">activity<br>
<input type="radio" name="type" 
value="food">food<br>
<b>Address</b><br>
<input type="text" name="address">
<br><b>Description</b><br>
<textarea rows="6" cols="50" name="input">Enter Descripton Here...</textarea><br>
<b>Add Image Link</b><br>
<input type="text" name="add_image"><br>'''+floof+'''
</form>
</div>
</div>

</body>
</html>   '''

def main():
    body = ""

    #determine if the user is properly logged in once. 
    isLoggedIn = authenticate()

    #attach a logout link only if logged in
    if isLoggedIn:
        body+= '<a href="../index.html" class="w3-bar-item w3-button w3-hide-small w3-right w3-hover-red">LOGOUT</a>'
    else:
        body+= '''<a href="Login/create.html" class="w3-bar-item w3-button w3-hide-small w3-right w3-hover-green">REGISTER</a>
    <a href="Login/login.html" class="w3-bar-item w3-button w3-hide-small w3-right w3-hover-blue">LOG IN</a>'''

    #finally print the entire page.
    print header() + NavBar()+body + footer()

print main()
