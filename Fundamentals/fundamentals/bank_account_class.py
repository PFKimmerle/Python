# Python script for a BankAccount class demonstrating OOP principles and method chaining.

## BankAccount Class Definition
class BankAccount:
    # Class-level attribute to keep track of all accounts (Bonus feature)
    all_accounts = []

    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)  # Adding the new account to the list of all accounts

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

    # Classmethod to display info for all accounts (Ninja Bonus)
    @classmethod
    def display_all_accounts_info(cls):
        for account in cls.all_accounts:
            account.display_account_info()

## Creating and Using BankAccount Instances with Method Chaining

# Create two accounts
account1 = BankAccount(0.02, 100)
account2 = BankAccount(0.03)

# Perform transactions on the first account and use chaining
account1.deposit(150).deposit(50).deposit(250).withdraw(200).yield_interest().display_account_info()

# Perform transactions on the second account and use chaining
account2.deposit(300).deposit(200).withdraw(50).withdraw(25).withdraw(100).withdraw(50).yield_interest().display_account_info()

## BONUS: Display information for all accounts
BankAccount.display_all_accounts_info()
