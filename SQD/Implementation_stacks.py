# Implementation of stacks
class Stackz:
    def __init__(self):
        self.stackz=[]
    def push(self,item):
        self.stackz.append(item)
    def pop(self):
        self.stackz.pop()
    def peek(self):
        print(self.stackz[-1])
    def isEmpty(self):
        print(len(self.stackz)==[])
    def show(self):
        print(self.stackz)
stack1=Stackz()
stack1.show()
stack1.push(5)
stack1.show()
stack1.push(9)
stack1.show()
stack1.push(7)
stack1.show()
stack1.peek()
stack1.isEmpty()
stack1.pop()
stack1.show()