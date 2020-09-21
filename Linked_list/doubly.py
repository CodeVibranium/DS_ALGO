class Doubly:
    def __init__(self,value):
        self.value=value
        self.Prev=None
        self.Next=None
a=Doubly(1)
b=Doubly(8)
c=Doubly(0)
d=Doubly('v')
a.Next=b
b.Prev=a
b.Next=c
c.Prev=b
c.Next=a
a.Prev=c
