f=input("enter ")
if(f=="y"):
    f=open("/home/spyreza/Desktop/nwe.txt")

a=[];counter=1
for line in f:
    a.append("satre{0}  matn   {1}".format(counter,line.strip())) 
    counter+=1
for x in range(len(a)):
    if a[x]=='satre8  matn   ':
        del a[x]
print(a)
