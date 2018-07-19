#!/usr/bin/python
import cgi,cgitb,os
cgitb.enable()
form=cgi.FieldStorage()
print """Content-type: text/html\n\n"""
print
#this creates a new page!
def FStoD():
    '''
    Converts cgi.FieldStorage() return value into a standard dictionary
    '''
    d = {}
    formData = cgi.FieldStorage()
    for k in formData.keys():
        d[k] = formData[k].value
    return d
def getFile():
    file=FStoD()['file']
    return file
def csvWrite():
    fd = open(getFile()+'.csv','a')
    firstName=FStoD()['firstName']
    lastName=FStoD()['lastName']
    bday=FStoD()['date']
    osis=FStoD()['osis']
    contact=FStoD()['contact']
    myCsvRow=""+osis+""+","+" "+lastName+" "+","+" "+firstName+","+contact+","+bday+" \n"

    fd.write(myCsvRow)
    fd.close()
def isFull():
    fd=open(getFile()+'.csv','r')
    lines= fd.readlines()
    fd.close()
    cv=open('events.csv','r')
    find=cv.readlines()
    ting=0#finds the CAP of the event
    date=''
    time=''
    for j in find:
        ret=j.split(",")#gives you the DATE of the Event
        id=ret[0]
        if id==getFile():
            ping=ret[4]
	    ping=ping.strip('\n')
            ting=int(ping)
            date=ret[0]
            time=ret[2]
            break
    counter=0
    for i in lines:#count people
        counter+=1
    if counter>ting:
        return "you have been placed on the waitlist, stay in touch!"
    else:
        return "thanks for registering for the event! Keep the DATE:"+date+" and time:"+time+" in mind!"
        
        
def user():
    return """
      <!DOCTYPE html>
<html>
<head>
  <link rel="shortcut icon" type="image/png" href="logo.png" />
</head>
<title>Signup</title>
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
    <h4 class="w3-xxlarge w3-animate-top">"""+isFull()+"""</h4>
    <hr class="w3-border-grey" style="margin:auto;width:40%">
    <p class="w3-large w3-center"><a href="../index.html">Back to Homepage</a></p>
  </div>
  <div class="w3-display-bottomleft w3-padding-large w3-xxlarge">
    <a href="https://www.facebook.com/stuycommutes/"><i class="fa fa-facebook-official w3-hover-opacity"></i></a>
  </div>
</div>
</body>
</html>
 

"""
csvWrite()
print user()
