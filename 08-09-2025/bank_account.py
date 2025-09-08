class Bank:
    def __init__(self,balance,owner):
        self.balance=balance
        self.owner=owner
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        self.balance-=amount
    def getBalance(self):
        return self.balance
b=Bank(1000,"Raghu")
b.deposit(2000)
b.withdraw(2000)
print("Balance in the account = ",b.getBalance())