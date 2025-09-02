l=eval(input("Enter 5 subject marks : "))
percentage=(sum(l)/5)
print("Percentage = ",percentage,"%")
if(percentage>=90):
    print("Grade A")
elif(percentage>=75):
    print("Grade B")
elif(percentage>=50):
    print("Grade C")
else:
    print("Fail")