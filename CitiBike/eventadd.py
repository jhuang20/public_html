#!/usr/bin/python
import cgi,cgitb,os
import time
import datetime

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

def newCode():
    title=FStoD()['title']
    content=FStoD()['content']
    tag=FStoD()['tag']
    tiempo= datetime.datetime.now()
    return "<div id='"+tag+"'> <h3 class='w3-center'>"+title+"</h3><br><p id='body' class='w3-left'>"+content+"""</p>
      <br><p class="w3-small w3-left">"""+str(tiempo.strftime("%Y-%m-%d %H:%M"))+"</p></div><br><br><br>"
def addToBlog():
    fd = open('blog.html','r+')
    icon=fd.read()
    p=icon.find("id='blog'")
    header=icon[:p+11]
    footer=icon[p+11:]
    fd.truncate(0)
    hey=header+newCode()+footer
    fd.write(hey)
    fd.close()


def user():
    return """
    <!DOCTYPE html>
<html>
<head>
  <link rel="shortcut icon" type="image/png" href="logo.png" />
</head>
<title>Dashboard</title>

<body>

<h1>You submitted a blog post!</h1>
<p><a href="dashboard.py">back to dashboard</a></p>

</body>
</html>"""
addToBlog()
#csvWrite()
print user()
