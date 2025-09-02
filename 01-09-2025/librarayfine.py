late_days=int(input("Enter the late days : "))
if(late_days>=1 and late_days<=5):
    print("10/- fine")
elif(late_days>=6 and late_days<=10):
    print("50/- fine")
else:
    print("100/- fine")