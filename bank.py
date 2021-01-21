class Account:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.deposits = []
        self.withdrawals = []

    def deposit(self, amount):
        self.deposits.append(amount)

    def withdraw(self, amount):
        if amount > self.total():
            print("Sorry, but you do not have enough money in your account")
        else:
            self.withdrawals.append(amount)

    def total(self):
        sum_dep = sum(self.deposits)
        sum_withd = sum(self.withdrawals)
        return sum_dep - sum_withd

account = Account("Ibrahim", "Smith")
account.deposit(100)
account.deposit(96)
account.withdraw(100)

print(account.total())