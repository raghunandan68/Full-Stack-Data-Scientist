s=input("Enter a sentence : ")
vc=0
cc=1
s_list=list(s)
for _ in range(len(s_list)):
    cc+=1
print("Character Count = ",cc)
print("Word Count = ",len(s.strip().split(" ")))
vowels=['a','e','i','o','u','A','E','I','O','U']
for i in s_list:
    if i in vowels:
        vc+=1
print("Vowels Count = ",vc)
