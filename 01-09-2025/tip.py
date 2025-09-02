amount=float(input("Enter bill amount : "))
if(amount<500):
    amount+=amount*0.05
    print("Total amount given = ",amount)
elif(amount>=500 and amount<=1000):
    amount+=amount*0.1
    print("Total amount given = ",amount)
elif(amount>1000):
    amount+=amount*0.15
    print("Total amount given = ",amount)