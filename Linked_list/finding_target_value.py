class Node:
    def __init__(self,value):
        self.Value=value
        self.Pointer=None

def find(Object,Skip):
    var1=a
    var2=None
    count=0
    for i in range(1,Skip):
        count+=1
        var1=var1.Pointer
        #print(f'{var1.Value} is the value of Node {count}')
        var2=var1.Pointer
        count+=1
        #print(f'{var2.Value} is the value of Node {count}')
    if Skip==1:
        return var1.Value
    else:
        return var2.Value
a=Node(2)
b=Node(4)
c=Node(8)
d=Node(10)
e=Node(12)
f=Node(-1)
g=Node(-9)
h=Node(3)
i=Node(11)
j=Node(15)

a.Pointer=b
b.Pointer=c
c.Pointer=d
d.Pointer=e
e.Pointer=f
f.Pointer=g
g.Pointer=h
h.Pointer=i
i.Pointer=j
x=find(a,5)
print(f'{x} is the value after given skips')
