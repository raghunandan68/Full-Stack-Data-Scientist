string=input("Enter a string : ")
vowels=['a','e','i','o','u']
countv=0
countc=0
for i in string:
    if i in vowels:
        countv+=1
    else:
        countc+=1
print("Vowels = ",countv," Consonants = ",countc)