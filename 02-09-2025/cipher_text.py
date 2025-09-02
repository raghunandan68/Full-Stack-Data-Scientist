s=input("Enter string : ")
shift=int(input("Enter the shift value : "))
res=''
for i in s:
    res+=chr(ord(i)+3)
print("Cipher text = ",res)