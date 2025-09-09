p=input("Enter the password : ")
u=False
l=False
d=False
s=False
if(len(p)>=8):
    for i in p:
        if(i.isupper()):
            u=True
        elif(i.islower()):
            l=True
        elif(i.isdigit()):
            d=True
        elif(not i.isalnum()):
            s=True
    if(u and l and d and s):
        print("Password is Strong")
    else:
        print("Password is weak.")
else:
    print("Password must be of length 8.")