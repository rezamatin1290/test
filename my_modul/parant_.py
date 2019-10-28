from re import findall
st="(klsjd))f())("
a=list()
x=0
while(x<len(st)):
    while(x<len(st)):
        if(st[x]=="("):
            a.append(st[x])
        elif(st[x]==")"):
            break
        x+=1
    #print(x,a)
    while(x<len(st)):
        if(st[x]==")"):
            a.append(st[x])
        elif(st[x]=="("):
            print(a)
            break
        x+=1
print(a)



"""
print(a)
if(len(a)%2==1):
    print("marhale avval","eshtebah")
else:
    for x in range(len(a)//2):
        #print(x,a[x])
        if(a[x]==")"):
            print("wrong",x)
            #break#print("eshtebah dar marhale dovvom")
        elif(a[x]=="("):
            b=len(a)-x-1
            #print("b is ",b)
            if(a[b]!=")"):
                print("eshtebah",x,b)"""
