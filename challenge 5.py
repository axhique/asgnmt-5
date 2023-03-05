class account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    
    def withdrawal(self, amount):
        self.balance-=amount

    def deposit(self, amount):
        self.balance +=amount
        
    def getBalance(self):
       return self.balance

class savingsaccount(account):
    def __init__(self, title=None, balance=0, interestrate=0):
        super().__init__(title,balance)
        self.interestrate = interestrate
    
    def interestamount(self):
        return (f'{(self.balance*self.interestrate)//100}')
    
a=savingsaccount('aash',5000,10)
print(a.balance)
a.deposit(1000)
a.withdrawal(400)
print(a.balance)
print(a.interestamount())
