from account import Account

account = Account(123, "Felipe", 55.0, 1000.0)
account.extract()

account2 = Account(321, "Luis", 100.0, 1000.0)
account2.extract()

account.deposit(50.0)
account.extract()

account2.withdraw(10.0)
account2.extract()