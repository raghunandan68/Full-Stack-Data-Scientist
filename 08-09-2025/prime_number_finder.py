prime=set({})
n=int(input("Enter the range : "))
for i in range(2,n+1):
    flag=True
    for j in range(2,i):
        if(i%j==0):
            flag=False
            break
    if(flag):
        prime.add(i)
print(prime)