from bankaccount import BankAccount

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
        
        
    def make_deposit(self, amount):
        self.account.deposit(amount)
        
            

    def make_withdrawl(self, amount):
        self.account.withdraw(amount)

    def display_user_balance(self, amount):
        self.account.display_account_info(amount)

user1 = User('Jojo', 'jojo@email.com')
user1.make_deposit(100)
user1.account.display_account_info()
