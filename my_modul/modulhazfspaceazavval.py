#این اسکریپت فایلها رو میخونه و هر سط رو بدون اسپیس در لیست میریزه  

f=open("/home/spyreza/Desktop/nwe.txt");l=[]
#print(f.read(),end="")
counter=1
for line in f:
    l.append("row {0}  is {1}".format(counter,line.strip()))
    counter+=1
print(l)
