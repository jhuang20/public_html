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

<body>

<h1>"""+isFull()+"""</h1>
<p><a href="../index.html">back home</a></p>

</body>
</html>"""
csvWrite()
print user()
