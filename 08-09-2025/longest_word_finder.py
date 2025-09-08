s=input("Enter the string : ")
l=s.split(' ')
maximum=0
res=''
for i in l:
    if(maximum<len(i)):
        maximum=len(i)
        res=i
print(res)