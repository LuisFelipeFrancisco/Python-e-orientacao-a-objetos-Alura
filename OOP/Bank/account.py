

class Account:
    
    def __init__(self, number, holder, balance, limit):
        self.number = number
        self.holder = holder
        self.balance = balance
        self.limit = limit
        
    def extract(self):
        print(f"Account number: {self.number}, Holder: {self.holder}, Balance: {self.balance}, Limit: {self.limit}")
        
    def deposit(self, value):
        self.balance += value
        
    def withdraw(self, value):
        self.balance -= value