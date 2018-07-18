import cgi
info = cgi.FieldStorage

#Takes the form data and make it into a link with the info
def FStoD():
    '''
    Converts cgi.FieldStorage() return value into a standard dictionary
    '''
    d = {}
    formData = cgi.FieldStorage()
    for k in formData.keys():
        d[k] = formData[k].value
    return d
info=FStoD()
def createPage(info):
    returnValue=headline()
    """returnValue+=Name(info)
    returnValue+=Image(info)
    returnValue+=Type(info)
    returnValue+=Description(info)
    returnValue+=Address(info)
    
    
    returnValue+=Rest_stuff()"""
    return returnValue

def headline():
    return '''<!DOCTYPE html>
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
    background-image: url('lower_manhattan.jpg');
    min-height: 100%;
}
</style>
</head>
<body>
<div class="w3-top">
  <div class="w3-bar" id="myNavbar">
  
    <a href="website.html"
    class="w3-bar-item w3-button w3-hide-small w3-animate-opacity">
    <p style="color:white">
    <h4 style="color:black">Stuy Tourism</h4></p></a>
    
    <a href="mainpage.html"
    class="w3-bar-item w3-button w3-hide-small w3-animate-opacity">
    <p style="color:black">
    Places-></p></a>'''
def Name(info):
    return '''a href="template.html"
class="w3-bar-item w3-button w3-hide-small w3-animate-opacity">
<p style="color:black">'''+str(d['landmark_name'])+'''</p></a>'''

"""def createData(info, lName):
    code = ''"""
    

#This is a function to make the webpage name for each different place        
def remSpaces(name):
    newName = ''
    for char in name:
        if char in ['!',',','.',"'",' ', '/']:
            newName += ''
        else:
            newName += char.lower()
    print newName
    return newName

lName = info['landmark_name']
lName = remSpaces(lName)

fileName = lName + '.html'


def makePage(code, fileName):
    s = open(fileName, "w")
    s.write(code)
    s.close()

#functionality NEEDED to add the page name to a master list of pages so that duplicates are not created
html = createPage(info)
makePage(html, fileName)
