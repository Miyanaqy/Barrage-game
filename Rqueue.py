class Data():
    def __init__(self,image,pos,bool = False):
        self.image = image
        self.pos = pos
        self.bool = bool
        self.next = None

class Rqueue():
    def __init__(self):
        self.head = None
        self.fail = None
    def add(self,image,pos,bool = False):
        data = Data(image,pos,bool)
        if self.head == None:
            self.head = data
            self.fail = data
            return
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



