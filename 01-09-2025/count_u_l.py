s=input("Enter a string : ")
uc=0
lc=0
s_list=list(s)
for i in s_list:
    if(i.isupper()):
        uc+=1
    else:
        lc+=1
print("Uppercase = ",uc," Lowercase = ",lc)