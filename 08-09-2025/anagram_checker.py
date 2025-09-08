from collections import Counter
str1=input("Enter 1st string : ")
str2=input("Enter 2nd string : ")
if(Counter(str1)==Counter(str2)):
    print(str1," and ",str2," are anagrams")
else:
    print(str1," and ",str2," are not anagrams")