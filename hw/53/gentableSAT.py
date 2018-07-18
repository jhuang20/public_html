#james huang
#INTROCS2 pd03
#2017-05-18
#HW53

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

def htmlTable(L):#this is the thing that makes our table
    Z=[]
    Y=[]
    X=[]
    W=[]#these variables are for gathering stats
    counter=0
    head="<!DOCTYPE html><head><title>SAT SCORES,2014</title><style>table,tr,td { border: 1px solid black }</style></head><body><p>This is a table of average SAT scores with the inclusion of a basic statistical indicator</p><table>"
    table = "<table>"
    for row in listTable(L):#for each element in listTable(L)[for each line]
        table += "<tr>"#make a new row
        if row[4]!='s':
            Z+=[row[4]]#adds appropriate data to appropriate data places
            Y+=[row[5]]
            X+=[row[3]]
            if "S" in row[4]:
                W+=[0]
            else:
                W+=[int(row[4])+int(row[5])+int(row[3])]#add the categories together to get the total score
        counter+=1
        for i in row:#for each row
            i = i.replace("..", ", ")#replace the .. with commas in each element
            if counter==1:
                table+="<th>"+i+"</th>"#if we r on first row(category headings), make it bold
            else:
                table += "<td>" + i + "</td>"#otherwise just add the data in the right place
            
            #add that to your data
        table += "</tr>"#end the row when done
    return head+rowStat(Z,Y,X,W)+"<br><h1>This is the Full Data</h1><br>"+table+ "</table>" +"</body>"
           

def genTable(tablefile, filename):
    htmlfile = open(filename, "w")
    htmlfile.write(htmlTable(tablefile))#writes to file
    htmlfile.close()#close 
genTable("data_SAT2014.csv", "statsSAT.html")
