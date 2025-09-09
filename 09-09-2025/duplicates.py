l=eval(input("Enter students list : "))
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for i in d:
    if d[i]>1:
        print(i,end=" ")