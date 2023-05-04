class BankAccount:
    all_accounts = []
    
    insufficient_funds = 5 
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def __repr__(self):
        return f'Balance = {self.balance}, int_rate = {self.int_rate}'
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'Your current balance: {self.balance}')
            
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient funds: Charging a $5 fee')
            self.balance -= self.insufficient_funds
        else:
            self.balance += amount
        return self

    def display_account_info(self):
        print(f'Account Information: {self}')
        return self

    def yield_interest(self):
        if self.balance > 0:
            user_int = self.balance * (self.int_rate)
            self.balance += user_int
        return self
    
    @classmethod
    def all_balances(cls):
        sum = 0
        for account in cls.all_accounts:
            sum += account.balance
        return sum

account1 = BankAccount(0.01, 50)
account2 = BankAccount(0.02, 100)
account3 = BankAccount(0.005, 75)
print(BankAccount.all_balances())

# print(account1.deposit(90).withdraw(220).yield_interest().display_account_info())
# print(account2.deposit(190).withdraw(320).yield_interest().display_account_info())
# print(account3.deposit(80).withdraw(120).yield_interest().display_account_info())


