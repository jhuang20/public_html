#!/usr/bin/python
import cgi
import time
import calendar
import cgitb#imports the necessary modules we need in the python code
cgitb.enable()
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
name=d['name']#we will use this variable to store the name of the file we need to retrieve
deliniator='Reviews are Below'#this is the text that tells us where to add the "review"
filename=name.replace(" ","")+'.html'#this makes the file name!!!
def reviewMake(d):#makes the html code that contains the various parts of the review
    if 'rating_value' in d and 'type_visit' in d and 'input' in d and 'title' in d:#if all the forms are filled out, write the review
        revStr='\n <br><h2><b>'+d['title'][:80]+'</b></h2>'
        revStr+='<h3><em>'+str(d['rating_value'])+'/100</em></h3><br>'
        revStr+='<p>'+str(d['input'])+'<p>'
        revStr+='<b>Type of Visit</b><br>'+str(d['type_visit'])+'<br>'
        revStr+='<p>This review was submitted by'+'at'+time.strftime("%c")+'DST</p><br>\n'
        revStr+='../.. Your review has been successfully submitted'#this part is the part we return as a confirmation that the review is submitted
    else:#otherwise say its not avalid review
        revStr='../..Not a valid Review, please input the appropriate values/boxes in the "write a review section"'
    return revStr
x=reviewMake(d)#store the html code for review in variable

def Conf(x):#this makes the confirmation message for the review
    loc=x.find('../..')#find the deliniator that tells us where the texy for this page is
    return x[loc+5:]#return the text we need to return for the confirmation message
confirmation=Conf(x)#store this in a variable

def revisePage(page):#this retrieves the html code from the landmark page
    r= open(page,"r")
    s=r.read()
    r.close()
    return s#return the contents of the file
s=revisePage('templatelandmark.html')#store the contents of the file in a variable

def appendToCode(x,s):
    location=s.find(deliniator)#find the area where we need to insert the review code,x
    y=x.find('../..')
    z=x[:y]#eliminate the "confirmation message" part of string
    if y>10:#if the review code actually has an actual review
        return s[:location+17]+z+s[location+17:]#place the review html right below the deliniator, then add the rest of the code after the review
    else:#otherwise just return the original string(no change)
        return s

    
revcode=appendToCode(x,s)#store this revised code in var
f=open(filename,'w')
f.write(revcode)#rewrite the file's html with its revised code(w/ review)
f.close()

print "Content-Type: text/html\n\n" #NOTE there are 2 '\n's !!! 
print """<!DOCTYPE html><html><head>
<title>Stuy Tourism!!</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato">
<style>
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
    margin: 20% 15% 15% 15%;
    background-color: white;
    padding: 5px;
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
    background-image: url(https://www.jimcutler.com/wp-content/uploads/2015/06/Cutler-2015-06-21-untitled-187-Edit_1000-960x619.jpg);
    min-height: 100%;
}

</style>

<body>
<div class="navbar">
  <a class="info" href="#template.html">Home</a>
  <a class="info" href="#website.html">Places</a>
  <a class="info" href="#review">Reviews</a>
  <a class="info" href="#write_review">Write A Review</a>
  <a class="register" href="#register">Register</a>
  <a class="login" href="#login">Login</a>
</div>


<div class="address" id="review_write">

<br><br><h3 style="color:black">"""+confirmation+"""</h3>
<br><p><a href="""+filename+""">Back to landmark page</a></p></div></body></html>"""#this is the code for the reView.py page itself that just returns a confirmation message!

