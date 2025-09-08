vowels=['a','e','i','o','u','A','E','I','O','U']
s=input("Enter the string : ")
l=list(s)
countv=0
countc=0
for i in l:
    if i in vowels:
        countv+=1
    else:
        countc+=1
print("Vowels = ",countv," Consonants = ",countc)