s=input("Enter a string : ")
s_list=list(s.strip())
c=0
for i in range(len(s_list)-1):
    if(s_list[i]==' ' and s_list[i+1]!=' '):
        c+=1
print("No.of words = ",c+1)