s=input("Enter the string : ")
l=list(s.lower())
for i in l:
    if i==' ':
        l.remove(i)
s=''.join(l)
if(s==s[::-1]):
    print(s," is a palindrome")
else:
    print(s," is not a palindrome")