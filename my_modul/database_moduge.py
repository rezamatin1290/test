def count_column(database="all_event",table="all_e"): #full count
    import mysql.connector as db
    conn=db.connect(user="spyreza",passwd="1290123",host="localhost")
    cur=conn.cursor()
    cur.execute("select count(*) from {}.{};".format(database,table))
    for x in cur:
        conn.close()
        return x[0]
#-------------------------------------------------------------------------------------
def insert_in(database="all_event",table="all_e",*arg): # for insert
    import mysql.connector as db
    conn=db.connect(user="spyreza",passwd="1290123",host="localhost")
    cur=conn.cursor()
    for x in arg:
        try:
            cur.execute("INSERT INTO {0}.{1} VALUES('{2}');".format(database,table,x))
            conn.commit()
        except:
            pass
    conn.close()
#insert_in("all_event","all_e","jkdlsff")
#------------------------------------------------------------------------------------------
def is_in(database,table,arg):
    import mysql.connector as db
    conn=db.connect(user="spyreza",passwd="1290123",host="localhost")
    cur=conn.cursor()
    cur.execute("select count(*) from {}.{} where id='{}';".format(database,table,arg))
    for x in cur:
        if(x[0]==0):
            conn.close()
            return False
        else:
            conn.close()
            return True
def select_all(database="all_event",table="all_e"):
    import mysql.connector as db
    conn=db.connect(user="spyreza",passwd="1290123",host="localhost")
    cur=conn.cursor()
    cur.execute("select * from {}.{};".format(database,table))
    for x in cur:
        yield x[0]    
def dum(item,x):
    for l in range(0,len(x)):
        for y in item:
            if not (is_in("all_event","all_e",x[:l]+y+x[l+1:])):insert_in("all_event","all_e",x[:l]+y+x[l+1:])
item=["r","e","2"]
num_pos=5

insert_in("all_event","all_e",item[0]*num_pos)
while(count_column()<(len(item)**num_pos)):
    for x in select_all():
        dum(item,x)
 
