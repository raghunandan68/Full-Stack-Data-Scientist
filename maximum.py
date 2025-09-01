n=eval(input("Enter the list: "))
res=n[0]
for i in n:
    if res<i:
        res=i
print("Maximum number : ",res)