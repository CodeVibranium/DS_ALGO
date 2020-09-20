string1=input("Enter the first string : ")
string2=input('Enter the second string : ')
x=string1.replace(" ","").lower()
y=string2.replace(" ","").lower()
count=0
if len(x)==len(y):
    for i in range(len(x)):
        alpha=x[i]
        if alpha in y :
            alpha_count_x=x.count(alpha)
            alpha_count_y=y.count(alpha)
            if alpha_count_x==alpha_count_y:
                count+=1
        else:
            print(f"{string1} and {string2} are not anagrams")
            break
else:
    print(f"{string1} and {string2} are not anagrams")
    
if count==len(x):
    print(f"{string1} and {string2} both are anagrams")