b="rex"
#شمارش اینکه که چند کلمه از  وجود دارد
def in_sen(a,b):
    #what time b reapet in a
    count=0
    for x in range(len(a)):
        if a[x]==b[0]:
            flag=True
            for y in range(len(b)):
                if (a[x+y]!=b[y]):
                    flag=False
            if (flag==True):
                count+=1
    return count
                    
