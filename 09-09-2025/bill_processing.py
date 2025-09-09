try:
    units=int(input("Enter the total units consumed : "))
    if(units<=100):
        print("Total bill amount = ",units*5)
    elif(units<=200):
        print("Total bill amount = ",500+(units-100)*7)
    else:
        print("Total bill amount = ",500+700+(units-200)*10)
except(ValueError):
    print("Invalid Input")
finally:
    print("Bill Processing Finished")