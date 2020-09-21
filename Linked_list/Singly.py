class SLL:
    def __init__(self,value):
        self.value=value
        self.pointer=None 
a=SLL(2)
b=SLL(3)
c=SLL(9)
a.pointer=b
b.pointer=c
c.pointer=a
x=a.pointer.value
print(x)