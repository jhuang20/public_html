#james huang
#INTROCS2 pd03
#2017-05-18
#HW52

##I got this code from a friend, my code didnt work at all and to be quite honest I don't understand what he did##
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

def htmlTable(L):
    
    table = "<!DOCTYPE html><body><p>This is a table of average SAT scores</p><table>"
    for row in listTable(L):#for each element in listTable(L)[for each line]
        table += "<tr>"#make a new row
        for i in row:#for each row
            i = i.replace("..", ", ")#replace the .. with commas in each element
            table += "<td>" + i + "</td>"
           
            #add that to your data
        table += "</tr>"#end the row when donw
    return table + "</table>" \
           "</body>"

def genTable(tablefile, filename):
    htmlfile = open(filename, "w")
    htmlfile.write(htmlTable(tablefile))#writes to file
    htmlfile.close()
genTable("SAT_Results.csv", "table.html")




