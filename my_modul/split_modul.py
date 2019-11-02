def split(string, spliter):
    list1=[]
    temp=""
    for x in range(len(string)):
        if string[x] != spliter:
            temp = temp + string[x]
        elif string[x] == spliter:
            if (temp not in list1):
                list1.append(temp)
                temp=""
    if len(temp)>0:
        list1.append(temp)
        temp=""
    return list1
