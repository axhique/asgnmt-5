class account:
    def __init__(self,title=None,balance=0):
        self.title=str(title)
        self.balance=balance

class savingsaccount(account):
    def __init__(self, title=None,balance=0,interestrate=0):
        super().__init__(title,balance)
        self.interestrate = interestrate
            


a=savingsaccount('aash',5077,8)
print(a.balance)
print(a.title)
print(a.interestrate)