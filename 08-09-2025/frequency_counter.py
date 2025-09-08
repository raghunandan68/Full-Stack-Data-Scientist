from collections import Counter
s=input("Enter the string : ")
l=s.split(" ")
print(dict(Counter(l)))