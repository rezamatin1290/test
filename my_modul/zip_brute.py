from zipfile import ZipFile
zf=ZipFile("/home/spyreza/Desktop/name of your zip file","r")
for x in range(1,1290124):
    x=str.encode(str(x))
    try:
        zf.extractall(pwd=x)
        #print("pass is ",x)
        break
    except:
        pass
        #print("wrong",x)
print(x)    


