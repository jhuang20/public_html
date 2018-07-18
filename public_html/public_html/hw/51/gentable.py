OutStream=open('table.html','w')
l=open('testdata.csv','r')
m=l.read()
l.close()
M="<!DOCTYPE html><html><body>"

def gentable():
    M="<!DOCTYPE html><html><body>"
    counter=3
    for i in m:
        if counter<3:
            M+='<td>'+str(i)+'</td>'
            counter+=1
        else:
            counter=0
            M+='<tr>'
    return M
            
gentable()
M+='</body></html>'
OutStream.write(M)
OutStream.close()
