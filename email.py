#!/usr/bin/python
import cgi,cgitb,os
cgitb.enable()
form=cgi.FieldStorage()
print """Content-type: text/html\n\n"""
print
def FStoD():
    '''
    Converts cgi.FieldStorage() return value into a standard dictionary
    '''
    d = {}
    formData = cgi.FieldStorage()
    for k in formData.keys():
        d[k] = formData[k].value
    return d

def csvWrite():
    fd = open('document.csv','a')
    name=FStoD()['author']
    email=FStoD()['email']
    msg=FStoD()['message']
    myCsvRow="<br><b>"+name+" </b>"+","+" "+email+" "+","+" "+msg+" <br> \n"
    fd.write(myCsvRow)
    fd.close()
def user():
    return """
    <!DOCTYPE html>
<html>
<head>
  <link rel="shortcut icon" type="image/png" href="logo.png" />
</head>
<title>Stuy X CitiBike</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Raleway">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
body,h1 {font-family: "Raleway", sans-serif}
body, html {height: 100%}
.bgimg {
    background-image: url('Citi-Bike.jpg');
    min-height: 100%;
    background-position: center;
    background-size: cover;
}
</style>
<body>

<div class="bgimg w3-display-container w3-animate-opacity w3-text-white">
  <div class="w3-display-topleft w3-padding-large w3-xlarge">
    <img src="logo.png" height=50 width=100>
  </div>
  <div class="w3-display-middle">
    <h1 class="w3-jumbo w3-animate-top">Message Submitted!</h1>
    <hr class="w3-border-grey" style="margin:auto;width:40%">
    <p class="w3-large w3-center"><a href="index.html">Back to Homepage</a></p>
  </div>
  <div class="w3-display-bottomleft w3-padding-large w3-xxlarge">
    <a href="https://www.facebook.com/stuycommutes/"><i class="fa fa-facebook-official w3-hover-opacity"></i></a>
  </div>
</div>

</body>
</html>"""
csvWrite()
print user()
