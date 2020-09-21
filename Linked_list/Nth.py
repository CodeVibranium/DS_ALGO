class Node:
    def __init__(self,value):
        self.Value=value
        self.Pointer=None

def nth_to_last_node(n, head):
    
    left_pointer  = head
    right_pointer = head

    # Set right pointer at n nodes away from head
    for i in range(n-1):
        
        # Check for edge case of not having enough nodes!
        if not right_pointer.Pointer:
            raise LookupError('Error: n is larger than the linked list.')

        # Otherwise, we can set the block
        right_pointer = right_pointer.Pointer

    # Move the block down the linked list
    while right_pointer.Pointer:
        left_pointer  = left_pointer.Pointer
        right_pointer = right_pointer.Pointer

    # Now return left pointer, its at the nth to last element!
    return left_pointer
a=Node(2)
b=Node(4)
c=Node(8)
d=Node(10)
e=Node(12)

a.Pointer=b
b.Pointer=c
c.Pointer=d
d.Pointer=e
print(nth_to_last_node(1, a).Value)