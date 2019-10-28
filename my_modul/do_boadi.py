c=0
x=[x for x in range(18)]
satr=1 
tedad_soton=6 #baraye tayin kardane tedade soton motagayyer maibashad
while (c<len(x)): 
     if (c+(tedad_soton-1))<len(x): 
         for y in range(tedad_soton): 
             print(x[c+y],end="-") 
         print("satre ",satr) 
         c=c+tedad_soton 
         satr+=1 
     else: 
         while(c<len(x)): 
             print(c) 
             c+=1 
         break 
