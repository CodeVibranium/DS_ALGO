numbs=[1,2,-1,3,4,10,10,-10,-1]
count=1
list1=[]
for i  in range(len(numbs)):
    list1.append(sum(numbs[0:count]))
    count+=1
    if len(list1)==len(numbs):
        print(max(list1))