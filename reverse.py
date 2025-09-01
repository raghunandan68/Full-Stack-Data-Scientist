string=input("Enter string : ")
#print(''.join(reversed(string)))
i=0
j=len(string)-1
str_list=list(string)
while i<j:
    str_list[i],str_list[j]=str_list[j],str_list[i]
    i+=1
    j-=1
print(''.join(str_list))