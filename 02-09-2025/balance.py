pin=int(input("Enter ATM PIN : "))
bal=int(input("Enter the balance amount : "))
withdraw=int(input("Enter withdraw amount : "))
if(bal<withdraw):
    print("PIN Verified")
    print("Transaction unsuccessfull.Not sufficient balance.")
else:
    print("PIN Verified")
    print("Transaction successfull.Reamining balance = ",bal-withdraw)