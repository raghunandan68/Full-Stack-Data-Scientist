n=int(input("Enter the number : "))
temp=n
res=0
length=len(str(n))
while temp>0:
    rem=temp%10
    res+=rem**length
    temp//=10
if(n==res):
    print(n," is a armstrong number")
else:
    print(n," is not a armstrong number")