OutStream=open('table.html','w')
l=open('testdata.csv','r')
m=l.read()
l.close()


def grouch():
    M="<!DOCTYPE html><html><body><table>"
    L=m.split('\n')
    for i in L:
        M+='<tr>'
        j=i.split(',')
        for k in j:
            M+='<td>'+str(k)+'</td>'
        M+='</tr>'
    print M
    return M
    print M
N=grouch()
N+='</table></body></html>'
x=str(N)
OutStream.write(N)
        
OutStream.close()
