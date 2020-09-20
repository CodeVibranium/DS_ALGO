characterz=input('Enter : ')
for i in characterz:
    x=characterz.count(i)
    if x>1:
        print('Not unique')
        break
else:
    print('Every char is unique')
   