try:
    balance=int(input("Enter bank balance : "))
    withdraw=int(input("Enter withdraw amount : "))
    if(withdraw>balance):
        raise Exception("Insufficient funds")
    else:
        print("Transaction successfull.")
except Exception as e:
    print(e)