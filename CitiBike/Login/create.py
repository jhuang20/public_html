#!/usr/bin/python
import cgi,cgitb,os,random,hashlib
cgitb.enable()

def header():
    return """content-type: text/html

<!DOCTYPE HTML>
<html>
<head>
<title>Register</title>
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
	<a href="create.html" class="w3-bar-item w3-button w3-hide-small w3-right w3-hover-red">REGISTER</a>
	<a href="login.html" class="w3-bar-item w3-button w3-hide-small w3-right w3-hover-blue">LOG IN</a>
  </div>
</div>
<div class="bgimg-1 w3-display-container w3-opacity-min" id="">
<div class="w3-content w3-container w3-padding-64" id="">
<br><br>
<font color="black"><h1>Let's get started</h1></font>
"""

def footer():
    return """<table>
<tr><td>
 <h3>Register with Username and Password</h3>
 <form action="create.py">
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
   <td>Password again:</td>
   <td> <input type="password" name="pass2"></td>
  </tr>
  <tr>
   <td></td><td><input type="submit" name="status" value="create"></td>
  </tr>
 </table>
 If you have an account, <a href = "login.html"><b>login here</b></a>.
</form>
</div>
</div>
</body></html>"""

def md5Pass(password):
    m = hashlib.md5()
    m.update(password)
    return m.hexdigest()

def checkIfNameExists(user):
    text = open('users.txt','r').readlines()
    for line in text:
        if line.split(",")[0]==user:
            return True
    return False

def valid(s):
    for c in s:
        if not (c >= 'a' and c <= 'z' or c >= 'A' and c <= 'Z' or c >= '0' and c <= '9'):
            return False
    return True

def createAccount(form):
    result = "<br>"
    if "user" in form and "pass" in form and "pass2" in form:
        user = form['user'].value
        password = form['pass'].value
        password2 = form['pass2'].value
        if checkIfNameExists(user):
            result += "Username "+ user +" has been taken.<br>"
        elif password != password2:
            result += "Passwords do not match!<br>"
        elif not valid(user):
            result += "Username contains invalid characters<br>"
        else:
            result += "account "+user+' created! login here: <a href="login.html">login page</a><br>'
            f = open('users.txt','a')
            password = md5Pass(password+user)
            f.write(user+","+password+"\n")
            f.close()
    else:
        result+="Invalid form submission, please fill in all fields"
    return result


    


def notFilledIn():
    return '''You need to create an account using the form found <a href="create.html">here</a>\n'''

def main():
    form = cgi.FieldStorage()
    body = ""
    if len(form)==0:
        body += notFilledIn()
    else:
        body += createAccount(form)
    print header() + '<font color="red">' + body + '</font>' + footer()

main()


