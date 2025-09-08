l=eval(input("Enter list of items : "))
maximum=max(l)
smax=0
for i in range(len(l)):
    if(smax<l[i] and l[i]!=maximum):
        smax=l[i]
print("Second Maximum = ",smax)