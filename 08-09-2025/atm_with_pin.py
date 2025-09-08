class ATM:
    def __init__(self,balance,pin):
        self.balance=balance
        self.pin=pin
    def login(self,p):
        if(p==self.pin):
            return "Login successfull"
        else:
            print("Wrong pin entered")
            exit(1)
    def check_balance(self):
        return self.balance
    def deposit(self,amount):
        self.balance+=amount
        return "Deposited successfully",self.balance
    def withdraw(self,amount):
        if(amount>self.balance):
            return "Insufficient funds"
        else:
            self.balance-=amount
            return "Withdrew ",amount
atm = ATM(500,1234)
print(atm.login(1234))
print(atm.deposit(200))
print(atm.withdraw(100))
print("Balance = ",atm.check_balance())