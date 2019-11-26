
a_time = [] # arrival time
s_time = [] # service time
p_name = []
finish_time = []

for x in range(int( input("تعداد پردازش : ") )):
    p_name.append(input("procss name : "))
    a_time.append( int(input("arrival time : ")) )
    s_time.append( int(input("service time : ")) )
    if len(finish_time) == 0:
        finish_time.append(a_time[0] + s_time[0])
        continue
    finish_time.append( finish_time[x-1] + s_time[x] )


Tr_time = [finish_time[x] - a_time[x] for x in range(len(a_time))]

def p_f(text, l):
    print(text,end = "  ")
    c = 0
    for x in l:
        print(f"procss {p_name[c]} => ", x, end = "  ")
        c +=1

p_f("Finish time : ", finish_time)
print()
p_f("Tr_time : ", Tr_time)
print()
print("Tr/Ts : ", end = "  ")
for x in range( len(Tr_time) ):
    print(round(Tr_time[x]/s_time[x], 2), end = "  ")

print()
