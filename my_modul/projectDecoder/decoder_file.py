from create_dict import c_dict
my_dict=c_dict()

#for encoding(ramz gozar) from one file to write onother file 
#print(my_dict)
#with open("/home/spyreza/Desktop/reza.txt","r") as r: 
 #   with open("/home/spyreza/Desktop/result.txt","w") as w:
  #      for x in r:
   #         for y in x:
    #            w.write(my_dict[y])
sum1=""
#########################################################################################################################
#for decoding(ramz gosha) from one file to write onother file
with open("/home/spyreza/Desktop/ramzgosha.txt","w") as w:
    with open("/home/spyreza/Desktop/result.txt","r") as r:
        for x in r:
            for y in x:
                sum1=sum1+y
                if len(sum1)==3:
                    w.write(my_dict[sum1])
                    sum1=""
                    
                
