#!/usr/bin/python
print 'Content-type: text/html\n'
print ''

import cgi,cgitb,os,random,hashlib

cgitb.enable()

def header():
        return """
    <!DOCTYPE HTML>
<html>
<head>
<title>Login</title>
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
.bgimg-1, .bgimg-2, .bgimg-3 {
    background-attachment: fixed;
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
}
.bgimg-1 {
    background-image: url('Register.jpg');
    min-height: 100%;
}
</style>
</head>
<body>
<div class="w3-top">
  <div class="w3-bar" color="1B1B1B" id="myNavbar">
    <a href="../../index.html" class="w3-opacity-min w3-bar-item w3-button w3-animate-opacity">HOME</a>
    <a href="../page1.py" class="w3-bar-item w3-button w3-hide-small">PLACES</a>	
	<a href="create.html" class="w3-bar-item w3-button w3-hide-small w3-right w3-hover-green">REGISTER</a>
	<a href="login.html" class="w3-bar-item w3-button w3-hide-small w3-right w3-hover-blue">LOG IN</a>
  </div>
</div>
<div class="bgimg-1 w3-display-container w3-opacity-min" id="">
<div class="w3-content w3-container w3-padding-64" id="">
<br><br>
<font color="black"><h1>Welcome back</h1></font>
    """
    
def footer():
    return """<table>
<tr><td>
 <h3>Login</h3>
 <form action="login.py" method="POST">
 <table>
  <tr>
   <td>User Name:</td>
   <td><input type="text" name="user"></td>
  </tr>
  <tr>
   <td>Password:</td>
   <td> <input type="password" name="pass"></td>
  </tr>
  <tr>
   <td></td><td><input type="submit" name="status" value="login"></td>
  </tr>
 </table>
 If you don't have an account, <a href = "create.html"><b>create one</b></a>.
 </div>
 </div>
 </form>
</body>
</html>"""

def md5Pass(password):
    m = hashlib.md5()
    m.update(password)
    return m.hexdigest()

def checkIfNameExists(user):
    text = open('users.txt', 'r').readlines()
    print text
    for line in text:
        if line.split(",")[0]==user:
            return True
    return False

def authenticate(user,password):
    password = md5Pass(password+user) # you can make this different, but still unique md5Pass(password+user)
    text = open('users.txt', 'r').readlines()
    for line in text:
        line = line.strip().split(",")
        if line[0]==user:
            if line[1]==password:
                return True
            else:
                return False
    return False

#the following code takes care of making sure the user is recognized
#as being logged in on other parts of the website
#remove a user, only do this if they successfully authenticated
#since this does not check to see if you have the right person
def remove(user):
    infile = open('loggedin.txt','r')
    text = infile.read()
    infile.close()
    if (user+",") in text:
        #remove code
        outfile = open('loggedin.txt','w')
        lines = text.split('\n')
        for i in range(len(lines)):
            lines[i]=lines[i].split(",")
            if len(lines[i]) > 1:
                if(lines[i][0] != user):
                    outfile.write(','.join(lines[i])+'\n')
        outfile.close();


#only meant to be run after password authentication passes.
#uses call to remove(user) that will remove them no matter what.
def logInUser(username):
    magicNumber = str(random.randint(1000000,9999999))
    remove(username)
    outfile = open('loggedin.txt','a')
    IP = "1.1.1.1"
    if "REMOTE_ADDR" in os.environ :
        IP = os.environ["REMOTE_ADDR"]
    outfile.write(username+","+magicNumber+","+IP+"\n")
    outfile.close()
    return magicNumber
            
def login(form):
    result = ""
    if not ('user' in form and 'pass' in form):
        return "Username or password not provided"
    user = form['user'].value
    password = form['pass'].value
    if authenticate(user,password):
        result += "Success!<br>\n"
        #add user to logged in status
        magicNumber = logInUser(user)
        result += '<a href="../page1.py?user='+user+'&magicnumber='+str(magicNumber)+'">Click here to go to the main site!</a>'
    else:
        result += "Failed to log in, authentication failure"
    return result


def notLoggedIn():
    return '''You need to login, <a href="login.html">here</a>\n'''

def main():
    form = cgi.FieldStorage()
    body = ""
    if len(form)==0:
        body += notLoggedIn()
    else:
        body += login(form)
    print header() + '<font color="red">' + body + '</font>' + footer()

main()
