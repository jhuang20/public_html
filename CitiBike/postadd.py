#!/usr/bin/python
import cgi,cgitb,os
cgitb.enable()
form=cgi.FieldStorage()
print """Content-type: text/html\n\n"""
print
#this creates a new page for an event!
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
    fd = open('events.csv','a')
    title=FStoD()['title']
    date=FStoD()['date']
    time=FStoD()['time']
    duration=FStoD()['duration']
    size=FStoD()['size']
    description=FStoD()['description']
    description=description.replace(', ','_')
    description=description.replace('\n',' ')
    description=description.replace('\r',' ')
    type=FStoD()['type']
    if type=="volunteering":
	typeCode=3
    elif type=="safetyclass":
	typeCode=1
    else:
	typeCode=2
    myCsvRow=date+","+title+","+time+","+duration+","+size+","+description+","+str(typeCode)+" \n"

    fd.write(myCsvRow)
    fd.close()
    if typeCode==3:#special code to differentiate volunteerCode
	pd=open(date+'-v.py','w')
        pd.write(makePage())
        pd.close()
	os.chmod(date+'-v.py',0777)
	s=open(date+'-v-admin.py','w')
        s.write(makeAdmin())
        s.close()
        os.chmod(date+'-v-admin.py',0777)
        c=open(date+'-v.csv','w')
        c.close()
        os.chmod(date+'-v.csv',0777)
    else:
	pd=open(date+'.py','w')
        pd.write(makePage())
        pd.close()
        os.chmod(date+'.py', 0777)
        s=open(date+'-admin.py','w')
        s.write(makeAdmin())
        s.close()
        os.chmod(date+'-admin.py',0777)
        c=open(date+'.csv','w')
        c.close()
        os.chmod(date+'.csv',0777)
def makeAdmin():
    date=FStoD()['date']
    return """#!/usr/bin/python
import cgi,cgitb,os
cgitb.enable()
form=cgi.FieldStorage()

print '''Content-type: text/html'''
print
def makePage():
    return '''<!DOCTYPE html>
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
    <title>Console</title>
    <body>

    <h1>Admin Console for Specified Event</h1>
    <h2>If you are not an admin, please send us a message on the contact page()</h2>
<h2 id="eventmanage">Who's Going?</h2>'''+getevent()+'''
</body>
</html>
    '''
def getevent():

    csvfile = open('"""+det(date)+""".csv', "r")#opens the file
    lines= csvfile.readlines()
    csvfile.close()
    final=' '
    count=0
    for j in lines:
	count+=1
    final+="<p><b>"+str(count)+ "</b> people are signed up</p>"
    final+="<p><b>"+str(count-"""+FStoD()['size']+""")+"</b> people are on waitlist</p>"
    count=0
    final+="<table style="width:100%">
    final+='''<tr>
    <th>Waitlist</th>
    <th>OSIS</th>
    <th>last name</th> 
    <th>first name</th>
    <th>email</th>
    <th>birthday</th>
    <th>first time?</th></tr>
    '''
    for show in lines:
    	final+="<tr>"
	if count<"""+FStoD()['size']+""":
	    final+="<td>No</td>"
            for i in show:
            	final+="<td>"+str(i)+"</td>"
	else:
	    final+="<td>Yes</td>"
            for i in show:
            	final+="<td>"+str(i)+"</td>"
	final+="</tr>"
        count+=1

    return final
print makePage()
"""
def form(abacus):#adds options to form if this is a group ride
    if FStoD()['type']=='safetyclass':
	return """Are you a first time rider?<br>
<select name="firsttime" size="2">
<option value="yes">yes</option>
<option value="no">no</option></select><br>"""
    else:
	return ""
def det(abacus):
    if FStoD()['type']=="volunteering":
	return abacus+'-v'
    else:
	return abacus
def makePage():
    return """#!/usr/bin/python
import cgi,cgitb,os,csv
cgitb.enable()
form=cgi.FieldStorage()

print '''Content-type: text/html'''
print
def getnumber():
    csvfile=open('"""+det(FStoD()['date'])+""".csv','r')
    lines=csvfile.readlines()
    csvfile.close()
    counter=0
    for i in lines:
	counter+=1
    return counter
def isFull():
    if getnumber()>"""+FStoD()['size']+""":
	return "<p><em>this is currently full! If you sign up, you will be on waitlist</em></p>"
    else:
	return ""
def header():
    return '''<!DOCTYPE html>
<html>
<head>
  <link rel="shortcut icon" type="image/png" href="../logo.png" />
</head>
<title>"""+FStoD()['title']+"""</title>
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
    <a href="http://homer.stuy.edu/~jhuang20/index.html#FAQ" class="w3-black w3-button w3-hide-small"><i class="fa fa-question"></i> INFORMATION </a>
    <a href="#contact" class="w3-black w3-button w3-hide-small"><i class="fa fa-envelope"></i> CONTACT</a>
  </div>
  <!-- Navbar on small screens -->
  <div id="navDemo" class="w3-bar-block w3-white w3-hide w3-hide-large w3-hide-medium">
    <a href="index.html" class="w3-bar-item w3-button w3-hide-small">
        <img src="logo.png" height=40 width=100>
    </a>
    <a href="#home" class="w3-black  w3-button">HOME</a>
<a href="#about" class="w3-black w3-button "><i class="fa fa-building"></i> OUR MISSION</a>
    <a href="signup.html" class="w3-black w3-button "><i class="fa fa-bicycle"></i> SIGN UP</a>
    <a href="blog.html" class=" w3-black w3-button "><i class="fa fa-user"></i> BLOG</a>
    <a href="../#FAQ" class="w3-black w3-button "><i class="fa fa-question"></i> Information </a>
    <a href="../#contact" class="w3-black w3-button "><i class="fa fa-envelope"></i> CONTACT</a>
  </div>
</div>
        
 <div id="body" class="w3-content w3-padding-64">
        <h1 class="w3-center">"""+FStoD()['title']+"""</h1>
        <h3 class="w3-center">You are signing up for """+FStoD()['date']+""" at """+FStoD()['time']+""" until """ +FStoD()['duration']+"""</h3>
<p>There are '''+str("""+FStoD()['size']+"""-getnumber())+'''  spots available out of  """+FStoD()['size']+"""</p>
<h3 id="event">Description</h3><p>"""+FStoD()['description']+"""</p>'''+isFull()+'''<form action="submit.py">
<br>
First Name::<input name="firstName" required="required"></input>
Last Name::<input name="lastName" required="required"></input>
<br>
<br>Birthday:<input type="date" name="date" required="required"><br>
OSIS:<input name="osis" required="required"></input><br>
Email: <input name="contact" required="required"></input><br>"""+form(FStoD()['type'])+"""
<input type="checkbox" name="terms" value="agree" required="required"> I agree that I will not hold CitiBike, Stuyvesant High School, or CitiBike X Stuy liable for any injuries resulting from this program. I understand that I have to be 16 years old to use CitiBike.<br>
<input type="hidden" id="file" name="file" value='"""+det(FStoD()['date'])+"""'>
   <button class="w3-button w3-black w3-section w3-xxlarge" type="submit">
          <i class="fa fa-bicycle"></i>Register!
        </button>
</form>
</div>
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
	
        </html>'''
print header()"""

def user():
    return """
    <!DOCTYPE html>
<html>
<head>
  <link rel="shortcut icon" type="image/png" href="logo.png" />
</head>
<title>Dashboard</title>

<body>

<h1>U submitted an event!</h1>
<p><a href="dashboard.py">back to dashboard</a></p>

</body>
</html>"""
csvWrite()
print user()
