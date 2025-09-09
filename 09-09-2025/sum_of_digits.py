n=int(input("Enter the number : "))
res=0
while n>0:
    rem=n%10
    res+=rem
    n//=10
print(res)