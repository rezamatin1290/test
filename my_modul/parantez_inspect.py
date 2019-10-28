#this is for parantez inspect
a=input("Enter:")
flag=False
flag1=False
b1=0
b2=0
for x in a:
    if x==")":
        b1+=1
    elif x=="(":
        b2+=1
if b2==b1:
    for x in range(len(a)):
        if a[x]=="(":
            flag=False
            for y in range(x+1,len(a)):
                if a[y]==")":
                    flag=True
                    break
    for x in range(len(a)):
        if a[x]==")":
            flag1=False
            for y in range(x-1,-1,-1):
                if a[y]==")":
                    flag1=True
                    break    
    if flag==True and flag1==True:
        print("baste shode")
    else:
        print("baste nashde")
else:
    print("invalid")
