def c_dict():
    from modul_generation_bruteforce_pass import gen_aalm
    a=gen_aalm()
    l={}
    #l["\t"]=a[-1]
    #l["\n"]=a[-2]
    c=0
    for x in range(1,126):
        if not(chr(x) in l):
            l[chr(x)]=a[c]
            l[a[c]]=chr(x)
            c+=1
    return l

#dictinary tolid shode far here
#k="""asdkhksf"""
#code for decode and code for encode remain
