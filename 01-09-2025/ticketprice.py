price=float(input("Enter ticket price : "))
age=int(input("Enter age : "))
status=input("Enter student status(yes/no) : ").lower()
if(age>=60):
    price-=price*0.1
    print("Final ticket price = ",price)
elif(status=="yes"):
    price-=price*0.2
    print("Final ticket price = ",price)
elif(status=="no"):
    print("Final ticket price = ",price)