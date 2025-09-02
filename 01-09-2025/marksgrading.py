marks=int(input("Enter the marks between 1-100 : "))
if(marks<1 or marks>100):
    print("Please enter valid marks")
    exit(0)
if(marks>=90 and marks<=100):
    print("Grade A")
elif(marks>=75 and marks<=89):
    print("Grade B")
elif(marks>=50 and marks<=74):
    print("Grade C")
else:
    print("Fail")