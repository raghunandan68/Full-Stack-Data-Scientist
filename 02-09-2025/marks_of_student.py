l=eval(input("Enter the student marks : "))
print("Highest Marks = ",max(l))
print("Lowest Marks = ",min(l))
res=0
for i in l:
    res+=i
print("Average Marks = ",res/len(l))