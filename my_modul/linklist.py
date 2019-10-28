class Reza(object):
    first=""
    last=""
    def __init__(self,name):
        if Reza.first=="" and Reza.last=="":
            Reza.last=Reza.first=self;
            self.name=name
        else:
            Reza.last.next=self
            Reza.last=self
            self.name=name
    def pirint(self):
        try:
            temp=Reza.first
            while (True):
                print(temp.name)
                temp=temp.next
        except:
            pass
