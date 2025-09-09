pin=1234
attempts=3
while attempts>0:
    i=int(input("Enter ATM PIN : "))
    if(i==pin):
        print("Access Granted")
        break
    else:
        print("Entered wrong pin try again.")
    attempts-=1