#!/usr/bin/python
print "Content-Type: text/html\n\n"
print ""
pback = '''
<!DOCTYPE html>
<html>
<head><title>
'''
import cgi
import os
fs = cgi.FieldStorage()
import cgitb
cgitb.enable()
form = cgi.FieldStorage()


def checkAddress(fs):
    if fs.getvalue('add_image') == None:
        return ''
    else:
        return fs.getvalue('add_image')

def remSpaces(name):
    newName = ''
    for char in name:
        if char in ['!',',','.',"'",' ', '/']:
            newName += ''
        else:
            newName += char.lower()
    return newName

pnext = '''
</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato">
<style>
<style>

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

body {
    background-image: url(
'''

pname = '''\
);
    min-height: 100%;
}

</style>
</head>
<body>

<div class="navbar">
  '''
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
        return makeNavBar('../../index.html', 'Home') + makeNavBar('../page1.py', 'Places')+'<a class="info" href="#search">Search</a><a class="info" href="#list">Landmarks</a><a class="info" href="#landmarkadd">Add Landmark</a>'
def footer():
    return '''  </div>

<div class="Name">
'''
ptype = '<span class="Type">'
paddress = '''\
</span></div>
<div class="address">
'''
pdesc = '''\
</div>
<div class="description">
'''
prev = '''\
</div>

<div class="Reviews" id="review">
    <u>Reviews:</u><br>
Reviews are Below </div>
<div id="review_write">

    </div>
<div class="Reviews w3-center" id="review_write">
<h3>Add a Review</h3>
<p class=""><em>What do you think of
'''
pfinal = '''\
</em></p>
<p>Just input the values in the form</p>
<br>
<form name="input" method="GET" action="reView.py">
<b>Rating:(out of 100) </b><br>
<input type="number" name="rating_value"><br>
<b>Title of your Review</b><br>
<input type="text" name="title" value="title"><br>
<b>Please Click if this Applies to you</b><br>
<input type="hidden" name="name" value="'''+fs.getvalue('landmark_name')+'''">
<input type="radio" name="type_visit" value="family">Family Visit<br>
<input type="radio" name="type_visit" value="business">Business Visit<br>
<input type="radio" name="type_visit"
value="tourism">tourism visit<br>
<input type="radio" name="type_visit" 
value="exploration">exploration<br>
<br><b>Your Review</b><br>
<textarea rows="6" cols="50" name="input">Enter Review Here...</textarea><br>

<input type="submit" name="Submit Review">
</form>
</div>


</body>
</html>
'''

body = ""

#determine if the user is properly logged in once. 
isLoggedIn = authenticate()

#attach a logout link only if logged in
if isLoggedIn:
    body+= '<a href="../index.html" class="w3-bar-item w3-button w3-hide-small w3-right w3-hover-red">LOGOUT</a>'
else:
    body+= '''<a href="../Login/create.html" class="w3-bar-item w3-button w3-hide-small w3-right w3-hover-green">REGISTER</a>
    <a href="../Login/login.html" class="w3-bar-item w3-button w3-hide-small w3-right w3-hover-blue">LOG IN</a>'''



def makePage(fileName, code):
    s = open(fileName, "w")
    s.write(code)
    s.close()
if isLoggedIn or 1==1:
    print '<!DOCTYPE html><html><body><meta http-equiv="refresh" content="0; url=Landmarks/'+remSpaces(fs.getvalue('landmark_name'))+'.html'+securefields()+'" />'+securefields()+'</body></html>'
#print pback + fs.getvalue('landmark_name') + pnext + checkAddress(fs) + pname + fs.getvalue('landmark_name') + ptype + fs.getvalue('type') + paddress +fs.getvalue('address') + pdesc + fs.getvalue('input') + prev + fs.getvalue('landmark_name') + pfinal
    code = pback + fs.getvalue('landmark_name') + pnext+checkAddress(fs)+ pname+NavBar()+body+footer()+ fs.getvalue('landmark_name') + ptype + fs.getvalue('type') + paddress +fs.getvalue('address') + pdesc + fs.getvalue('input') + prev + fs.getvalue('landmark_name') + pfinal
    lName = remSpaces(fs.getvalue('landmark_name'))
    fileName = lName + '.html'
    makePage('Landmarks/'+fileName, code)
    os.chmod('Landmarks/'+fileName,0777)
else:
    print '<!DOCTYPE html><html><body> You Need To Login, go back to login'+securefields()+'</body></html>'
