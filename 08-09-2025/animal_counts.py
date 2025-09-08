d={}
n=int(input("Enter number of dictionaries : "))
for i in range(n):
    k=eval(input(f"Enter dictionary {i+1} : "))
    if isinstance(k,dict):
        d[i]=k
    else:
        print("Enter valid dictionary")
count=0
s=input("Enter string to find out in dictionary : ")
for key,value in d.items():
    for j in value:
        if(j==s):
            count+=value.get(j)
print("Total pupppies = ",count)