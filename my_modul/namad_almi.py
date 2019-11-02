def bend(a):
    for x in range(len(a)):
        if a[x] != "0" and a[x] != ".":
            print(a[x]+"."+a[x+1:],"(10**-",x-1,")",sep="")
            break
while(True):
    try:
        a = input("Enter: ")
        a = float(a)
    except:
        print("enter a number:")
    else:
        a = str(a);
        if "e" in a:
            print(a[:str(a).index("e")]+"(*10**-"+a[str(a).index("e")+2:]+")");break
        if a[0] == "0":
            bend(a)
            break
        b=a.index(".")
        if b!=1:
            a=a[:b]+a[b+1:]
            a=a[:1]+"."+a[1:]
            print("%s*(10**%s)"%(a,b-1))
        elif b==1:
            print("%s*(10**0)"%(a))
        break
