#addFront() addRear() removeFront() removeRear() size() isEmpty()
class Deque:
    def __init__(self):
        self.deque=[]
    def append(self,item):
        self.deque.append(item)
    def add_Front(self,item):
        self.deque.insert(0,item)
    def add_Rear(self,item):
        self.deque.append(item)
    def rem_Front(self):
        self.deque.pop(0)
    def rem_Rear(self):
        self.deque.pop(-1)
    def show(self):
        print(self.deque)
    def isEmpty(self):
        print(len(self.deque)==[])
    def size(self):
        print(len(self.deque))
deque1=Deque()
deque1.append(4)
deque1.append(8)
deque1.append(2)
deque1.show()
deque1.add_Front(5)
deque1.show()
deque1.add_Front(9)
deque1.show()
deque1.add_Rear(-87)
deque1.show()
deque1.rem_Front()
deque1.show()
deque1.rem_Rear()
deque1.show()
# this is the implemetation of our DEQUE