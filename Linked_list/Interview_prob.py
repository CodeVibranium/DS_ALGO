# Boolean for Cycle_check # SOLVED
class Node:
    count=0
    def __init__(self,value):
        self.value=value
        self.point=None
        Node.count+=1
        self.Count=Node.count
        
def check(Object):
    if Object.point==None:
        print('Not a cicular linked list')
    else:
        print('Circularly linked list ',Object.point.value)
    
a=Node(5)
b=Node(13)
c=Node(10)
a.point=a
b.point=b
c.point=a
check(c)