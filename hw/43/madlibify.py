#!/usr/bin/python
print "Content-Type: text/html\n"
print ""
""" How did your team deal with punctuation?
Our team used a helper list with common punctuation and we stored the punctuation in a separate part of our helper function!"

How did at least 2 other teams deal with punctuation differently than you?
Team Cow Gou isolated their punctuation, dealt with the placeholder word, and re added the punctuation
team CJ did an if statement and then if there was punctuation at the end of the placeholder, they would modify it appropriately. 

Which approach do you prefer and why?
I preferred Cow Gou's approach as it was easier to read and understand it. It also is probably faster as it is modular by design.
"""
print "<!DOCTYPE html>"
print "<html><head><title>Madlibification</title></head><body> h3 {font-family: Verdana, Arial, Helvetica, sans-serif;}"
import random
story="There was once a <ADJ> couple from <PLACE>. \n\
There was also a <N> and this was where the couple <NA> and <NA2> <V>. \n\
It was a <ADJ> day and <NA> <V> while <NA2> <ADV> followed. \n\
They <V> a <ADJ> way when they found a hidden <N>. <NA2> <V> it, and they found a large gold <N>. \n\
The <ADJ> <NA> and <ADJ> <NA2> <ADV> went home and became rich, and lived happily ever after!"
NA=['James','Mihad','David','Joe','Jack']
NA2=['Lauren','Katie','Samantha','Olivia','Hanna']
N=['park','tree','coffeeshop','museum','event','airport',\
       'school','library','beach']
V=['play','climb','wander','surf','discover','walk','explore','relax']
ADJ=['beautiful','ugly','nice','great','terrible','disastrous']
ADV=['closely','quickly','quietly','illegally']#master list of words that we can replace placeholders with
PLACE=['New York','Chicago','Stuyvesant High School','the streets','the CSDOJO']
THINGS=[N,V,ADJ,ADV,PLACE]#reference list
ref=["<N>","<V>","<ADJ>","<ADV>","<PLACE>"]

thing=''

def replace(thing,litt,punch):
                converter=ref.index(thing)
                which=THINGS[converter]
                vu=which[random.randrange(len(which))]
               
               #these three functions 1. convert placeholder to a variable which stores a list and then 2. get a random word from appropriate placeholder list
                
                if litt[litt.index(thing+punch)-1]!="to" and thing=="<V>":#..and is a non-infinitive
                    if vu[-1]=='e':
                        litt[litt.index(thing+punch)]="<b>"+vu+"d"+punch+"</b>"#add ed to a random verb from the list(to make it pAst tense)
                    else: 
                        litt[litt.index(thing+punch)]="<b>"+vu+"ed"+punch+"</b>"
               #if there is a "to" just extract a random verb! or if its a regular verb
                else:
                    litt[litt.index(thing+punch)]="<b>"+vu+punch+"</b>"
                
                return litt
def madLibify(story):
    punc=[',','.','?','!']
    L=story.split(' ')#listified story
    character1=NA[random.randrange(len(NA))]
    character2=NA2[random.randrange(len(NA2))]#characters!!
    for i in L:#going thru each element
        if i in ref or i[:-1] in ref:
            if i[-1] in punc:
                replace(i[:-1],L,i[-1])
        
            else:
                replace(i,L,'')
        elif i=="<NA>":
          L[L.index(i)]=character1
        elif i=="<NA2>":
          L[L.index(i)]=character2
                #helper function
    
    s=' '       #new string!
    print "<p>"+s.join(L)#join the elements of list into a string ("s")
madLibify(story)
print "</p> </body> </html>"
