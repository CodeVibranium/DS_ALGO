# Reverse a linked list  https://bit.ly/3klzDSJ
class Node:
    count=0
    def __init__(self,value):
        self.value=value
        self.pointer=None
        Node.count+=1
def reverse(Object):
    for i in range(Node.count):
        cur=Object.pointer.value
        assign=Object.value
        