#!/usr/bin/python
import cgi,cgitb,os,csv
cgitb.enable()
form=cgi.FieldStorage()

print '''Content-type: text/html'''
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
def getEvent():
    fill="You are not registered for any events."
    csvfile = open("../CitiBike/events.csv", "r")#opens the file
    lines= csvfile.readlines()
    csvfile.close()
    counter=0
    for row in lines:#look at each event, see if there is a match
        ret=row.split(",")#gives you the DATE of the Event
        ping=ret[0]
        vfile= open("../CitiBike/"+ping+".csv","r")#opens csv of THIS file
        vline=vfile.readlines()
        for person in vline:
            per=person.split(",")#gives you list of OSIS
            osisM=per[0]
            if "208947879"==osisM:
                fill+="REGISTERED FOR "+ret[1]+" on "+ret[0]+" starting at "+ret[2]+"<br>Event Description:"+ret[5]+"<br><br>"
                break
               
            
            
    return fill
def header():
    return '''<!DOCTYPE html>
<html>'''+getEvent()+'''

	
        </html>'''

print header()
