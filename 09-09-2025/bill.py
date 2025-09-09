d={}
n=int(input("Enter no. of items : "))
for i in range(n):
    a,b=list(map(str,input(f"Enter item {i+1} name and price seperated by space : ").split(" ")))
    d[a]=b
bill=0
for i in d:
    bill+=int(d[i])
print("Total bill = ",bill)