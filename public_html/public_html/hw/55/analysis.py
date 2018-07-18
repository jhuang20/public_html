#james huang and tony chen-the cs meisters
#INTROCS2 pd03
#2017-05-22
#HW55
'''
Devlog
2017-05-23 <8:00>
James and Tony 
-Basic coding that outputs the data is complete from last friday
-Search online to find data related to our data, AP scores
-Brainstorms and creates the basic plan for approaching correlation of the 2 datasets
2017-05-24 <10:00>
James and Tony 
-Create code that allows us to add new columns to the table
-Adds the AP pass rates in decimal form
2017-05-24 <8:00>
James and Tony
-Both attempted codes for ranking seperately
2107-05-24 <9:00>
James and Tony
-Code for a ranking funtion that will rank the AP data based on the scores and the SAT da
-Code for a function that will take the rankings of the pass rate of AP and SAT and find a correlation if it is with a certain range or near each other.
'''
##new and improved, with a lot more modular design!!!##
def readlines(File):
    csvfile = open(File, "r")#opens the file
    lines = csvfile.readlines()#returns single line by single line
    csvfile.close()
    return lines #returns line by line

def listTable(L):
    table = []
    counter=0#empty table
    for row in readlines(L):#reads line by line
        row = row.strip()#strips of unnecessary characters
        row = row.replace(", ", "..")#replaces commas with .., CSV commas have no space
        row = [row.split(",")]#split it by csv commas
        table += row#adds the row to table
        counter+=1
    return table

def mean(numbers):#function to determine mean
    mean=0
    counter=0
    for i in numbers:
        i=int(i)
        mean+=i
        counter+=1
    return str(mean/counter)
    
def freq(numeros):#function to determine mode
    d={}
    for i in numeros:
        if i in d.keys():
            d[i]+=1#if i is already in dictionary add to the number of occurences(<value>) in dictionary
        else:
            d[i]=1#if it is first occurence, add a new thing (i ) to dictionary
    L=d.values()
    M=d.keys()
    return str(M[L.index(max(L))])#returns the most frequently appearing number

def rowStat(english,math,writing,total):#returns stats
    statchoice=[english,math,writing,total]#this list stores the SAT scores for all areas
    choice=['ENGLISH','MATH','WRITING','TOTAL']#stores different scores in string form for inserting into table headings
    counter=0#counter(will be used later)
    returnValue="<table>"#this is what we will return
    returnValue+="<tr><th>NYC SAT AVR SCORE,2014</th><th>Mean</th><th>Median</th><th>Mode</th><th>Min</th><th>Max</th><tr>"#the heading for the stat table
    Z=[]
    Y=[]
    X=[]
    W=[]#the empty lists we will use for editing the base lists for later
    while counter<4:
        Z=statchoice[counter]#we extract the desired list of scores for appropriate catagory(as dictated by the counter)
        Y=choice[counter]#for the purpose of the heading, we find the correct catagory name for the table row
        X=sorted(Z)#we sort list Z
        M=X[:-1]#and then remove the text data (its at the end)
        returnValue+="<tr><td><b>SAT AVR "+Y+" SCORE</td><td>"+mean(M)+"</td><td>"+str(X[len(X)/2])+"</td><td>"+freq(M)+"</td><td>"+str(M[-1])+"</td><td>"+str(M[1])+"</td></tr>"
        counter+=1#the line above is the data inputing

    returnValue+="</table>"
    
    return returnValue

def ranking(a,b,c): #takes SAT scores, AP scores, and the names of the school
    returnValue=0
    counter=0
    L=sorted(a)[::-1]
    M=sorted(b)
    d=[]#stores the index for the SAT rankings
    e=[] #stores the index for the AP rankings
    for i in a:
        d+=[L.index(i)]
        
    for j in b:
        e+=[M.index(j)]
        
    for i in d: #this checks for the correlation
        check=counter-5
        while check<counter+5 and check<len(e):
            if i==e[check]:
                returnValue+=1
            check+=1
        counter+=1

    return str(float(returnValue)/179+float(499-179)/499) #calculates the correlation percentage
        
        
def FinalCorr(L1,L2,Lcommon):
    d={} #dictionary to store SAT values
    e={} #dictionary to store ap values
    counter=0
    correlation='<br>This is the strength of the correlation '
    for i in Lcommon: #adds values and keys to the list
        if counter<len(L1):
            d[i]=L1[counter]
        if counter<len(L2):
            e[i]=L2[counter]
        counter+=1 #keeps track of index
    
    
    L=d.values()#returns a list scores
    M=e.values()
    correlation+=ranking(L,M,Lcommon)
    print correlation
    
    return correlation+"</br>"

def correlate(File):
    final=[]
    returnValue=[]
    names=[]
    lines=listTable(File)[1:]
    first_term=['ap pass rate(decimal)']
    for row in lines:
        names+=[row[1]]
        if row[4]!='s': #disregard the s because the dont add numbers and will cause errors
            final+=[float(row[4])/float(row[3])] #divides the ap pass over ap taken to find the pass rate
        else:
            final+=[0]
    return first_term+final
correlate("AP_results.csv")

def htmlCell(i):
    table=''
    i = i.replace("..", ", ")#replace the .. with commas in each element
    table += "<td>" + i + "</td>"#otherwise just add the data in the right place
    return table

def htmlRow(row):
    table= "<tr>"#make a new row
    for i in row:#for each row
        table+=htmlCell(i)
    table+="</tr>"
    return table
    

    
def htmlTable(L):#this is the thing that makes our table
    Z=[]
    Y=[]
    X=[]
    names=[]
    merge=correlate("AP_results.csv")
    W=[]#these variables are for gathering stats
    counter=0
    head="<!DOCTYPE html><head><title>SAT SCORES,2014</title><style>table,tr,td { border: 1px solid black }</style></head><body><p>This is a table of average SAT scores with the inclusion of a basic statistical indicator</p><table>"
    table = "<table>"
    for row in listTable(L):#for each element in listTable(L)[for each line]
        if counter<len(merge):
            row+=[str(merge[counter])]
        names+=[row[0]]
        if row[4]!='s':
            Z+=[row[4]]#adds appropriate data to appropriate data places
            Y+=[row[5]]
            X+=[row[3]]
            if "S" in row[4]:
                W+=['TOTAL SAT SCORE']
            else:
                W+=[int(row[4])+int(row[5])+int(row[3])]#add the categories together to get the total score
        else:
            W+=[0]
        row+=[str(W[counter])]
        counter+=1
        
        table+=htmlRow(row)#end the row when done
    return head+str(FinalCorr(merge,W,names))+rowStat(Z,Y,X,W)+"<br><h1>This is the Full Data</h1><br>"+table+ "</table>" +"</body>"
           

def genTable(tablefile, filename):
    htmlfile = open(filename, "w")
    htmlfile.write(htmlTable(tablefile))#writes to file
    htmlfile.close()#close 
genTable("data_SAT2014.csv", "analysis.html")
