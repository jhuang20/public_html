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
quor=d['query']
query=quor.lower()
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


def search(query):
    returnStr='<span class="w3-center"><em>your search: '+query+'</em></span><br>'
    for i in lists:
        f=open(i,"r")
        s=f.read()
        f.close()
        x=s.find('input type="hidden"')
        z=s.find('">',x,x+175)
        finder=s[x+39:z]
        shre=finder.lower()
        if shre.find(query)!=-1:
            returnStr+='<b>Landmark Name </b><a href="'+i+'">'+finder+'</a><br>'
        if s.find(query)!=-1:
            returnStr+='<b>'+str(s.count(query))+' Matches in Text found: </b><a href="'+i+'">'+i+': '+query+'</a><br>'
    return returnStr

def result():
    if search(query)=='<span class="w3-center"><em>your search: '+query+'</em></span><br>':
        return 'No Results Found:Try a less specific query/search<br><a href="../Project/page1.py">Back to Search</a>'
    else:
        return '<a href="../Project/page1.py">Back to Search</a>'


#makes a link, link will include secure features if the user is logged in
def makeLink(page, text):
    return '<a href="'+page+'">'+text+'</a><br>'

def makeNavBar(page, name):
        return '<a class="info" href="' +page+'">'+name+'</a>\n'
def NavBar():
        return makeNavBar('../index.html', 'Home') + makeNavBar('page1.py', 'Places')+'<a class="info" href="#search">Search</a><a class="info" href="#list">Landmarks</a>'
def footer():
    return '''  </div><div class=" Reviews">


'''+search(query)+result()+'''
</div></body>
</html>   '''
def main():
    body = ""
    print header() + NavBar()+body + footer()
    return ""

print main()
