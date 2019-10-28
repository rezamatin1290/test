a=input("Enter a number:")
a=int(a) #roooz+avvalinn roz saal
if(a<=186):
    b=(a//31)
    if(a%31>0):
        b+=1
    if(b==1):
        print("Farvardin")
    elif(b==2):
        print("Oridibehesht")
    elif(b==3):
        print("khordad")
    elif(b==2):
        print("Tir")
    elif(b==3):
        print("mordad")
    elif(b==4):
        print("shrivar")
if(a%7==1):
    print("panchshanbe")
elif(a%7==2):
    print("jomme")
elif (a%7==3):
    print("shanbe")
elif (a%7==4):
    print("yekshanbe")
elif (a%7==5):
    print("doshanbe")
elif (a%7==6):
    print("seshanbe")
elif(a%7==0):
    print("chahashanbe")
#elif (a%7==)
