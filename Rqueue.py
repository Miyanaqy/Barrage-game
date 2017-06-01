class Data():
    def __init__(self,image,pos,bool, number):
        self.image = image
        self.pos = pos
        self.bool = bool
        self.next = None
        self.number = number
    def loop(self,rq):
        if self.number > 0:
            self.number -= 1
            rq.adds(self)
        

class Rqueue():
    rqueue = None
    def __init__(self):
        self.head = None
        self.fail = None
        
    def add(self,image,pos,number,bool = False):
        data = Data(image,pos,bool,number)
        if self.head == None:
            self.head = data
            self.fail = data
            return
        self.fail.next = data
        self.fail = data
        
    def adds(self,data):
        self.fail.next = data
        self.fail = data
        
    def remove(self):
        if self.head == None:
            return
        data = self.head
        if self.head.next == None:
            self.head = None
            self.fail = None
            return data
        self.head = self.head.next
        return data

    @classmethod
    def creatRq(cls):
        if Rqueue.rqueue:
            Rqueue.rqueue = Rqueue()
        return Rqueue.rqueue
            

    

