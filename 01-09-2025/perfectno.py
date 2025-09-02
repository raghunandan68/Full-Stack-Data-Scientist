n=int(input("Enter the number : "))
res=0
for i in range(1,n):
    if(n%i==0):
        res+=i
if(res==n):
    print(n," is a perfect number")
else:
    print(n," is not a perfect number")