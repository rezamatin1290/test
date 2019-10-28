def manipu(item_mix,num_array,index,results):#item_mix item for blend #num_array number of seat
    for x in item_mix:
        num_array=list(num_array)
        num_array[index]=x
        num_array="".join(num_array)
        if not (num_array in results):
            results.append(num_array)
            print(num_array)
        #else:
         #   print("found in list")


def gen_aalm():
    results=[]
    item_mix=list(input("Enter a item for blend:"))
    num_array=(item_mix[0])*(int(input("Enter number of position")))
    results.append(num_array)
    print(item_mix,num_array)
    m=0
    limit_gen=(len(item_mix))**(len(num_array))
    while len(results)!=limit_gen:
            for x in results:
                for y in range(-1,-len(x)-1,-1):
                    manipu(item_mix,x,y,results)
    return results

#call gen_elm
#contain returns
gen_aalm()
