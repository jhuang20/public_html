#!/usr/bin/python
print "Content-Type: text/html\n"
f=open("lit.txt")
r= f.read()
f.close()
print "<!DOCTYPE html>"
print '''<html><head><title>Storify</title><style> body {background-size:100%}</style></head><body background = "https://media2.giphy.com/media/nYmXj4wLAgd7W/giphy.gif">'''
print '''<a href="lit.txt">lit</a>'''
print '<h1>Most Frequent Words</h1><table><tr><th>Word</th><th>Frequency</th>'
blackmail=['to','i','we','has','have','was','can','be','he','the','of','a','in','it','that','she','is','for','but','and','him','her']
def context(text):
    newT = text[text.find("PRIDE"):] #finds the start of the story and splice it and removes everything before the story
    newT = newT[:newT.find("End of the Project Gutenberg EBook of Pride and")-1] #finds the end of the story and removes everything after the end
    return newT

def wordonly(i):
     i = i.strip() #removes any extra spaces and new lines
     i = i.strip('".!,?:;') #removes the puncuation
     i = i.lower() #makes everything lowercase
     return i
    
def instance(story):#our search function
    d={}
    L=(context(story)).split(" ") #takes the modify story and splits it into a list base on the spaces
    for i in L:
        i = wordonly(i)
        if i in d.keys():
            d[i]+=1#if i is already in dictionary add to the number of occurences(<value>) in dictionary
        else:
            d[i]=1#if it is first occurence, add a new thing (i ) to dictionary
    return d

def top30(r):
    d = instance(r)
    L=d.values()
    M=d.keys()
    counter=0
    newstr=''
    while counter<30:
        if M[L.index(max(L))] in blackmail:
            M.pop(L.index(max(L))) #removes the largest variable to find the 2nd largest
            L.pop(L.index(max(L)))
        else:
            newstr+="<tr>"+"<td>"+M[L.index(max(L))]+"</td><td>"+str(max(L))+"</tr> \n"
            M.pop(L.index(max(L))) #removes the largest variable to find the 2nd largest
            L.pop(L.index(max(L)))
            counter+=1
    return newstr    
print top30(r)
print "</table>"
print "</body> </html>"
