#AAAABBBBCCDDD->A4B4C2D3
line='ABBCDDD'
list1=[]
for i in line:
    x=line.count(i)
    if i not in list1:
        list1.append(i)
        list1.append(x)
x=''
for i in list1:
    x+=str(i)
print(x)
    
    