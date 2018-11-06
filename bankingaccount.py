class Account:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def __str__(self):
        return ("Account Name: %s\nAccount Number: %d\nAccount Balance: $%.2f" %
                (self.name, self.account_number, self.balance))

    def deposit(self, deposit_amount):
        self.balance += deposit_amount

    def withdraw(self, withdraw_amount, fee):
        self.balance -= withdraw_amount
        self.balance -= fee


if __name__ == "__main__":
    account1 = Account("Daffy Duck", 90453889, 100)
    account2 = Account("Donald Duck", 83504837, 100)
    account3 = Account("Daisy Duck", 74773321, 100)
    print(account1)
    print(account2)
    print(account3)
    account1.deposit(25.85)
    account2.deposit(75.50)
    account3.deposit(50)
    print(account1)
    print(account2)
    print(account3)
    account1.withdraw(25.85, 2.50)
    account2.withdraw(75.50, 1.50)
    account3.withdraw(50.00, 2.00)
    print(account1)
    print(account2)
    print(account3)
