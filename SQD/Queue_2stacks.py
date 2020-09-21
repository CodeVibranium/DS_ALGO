# implementig queue using two stacks
class Queue2stacks:
    def __init__(self):
        self.stack_in=[]
        self.stack_out=[]
    def Enqueue(self,item):
        self.stack_in.append(item)
        return self.stack_in
    def Dequeue(self):
        x=self.stack_in.pop()
        self.stack_out.append(x)
        return x
queue1=Queue2stacks()
for i in range(11):
    queue1.Enqueue(i)
print(queue1.Enqueue(2))
for i in range(11):
    print(queue1.Dequeue())
#print(queue1.Dequeue())
