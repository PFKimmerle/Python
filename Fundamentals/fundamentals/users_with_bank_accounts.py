# Python script for Users with Bank Accounts demonstrating OOP principles, multiple accounts, and transfer functionality.

## BankAccount Class Definition (from the previous task)
class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

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

## User Class Definition with Association to BankAccount
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        # Allowing multiple accounts
        self.accounts = {'checking': BankAccount(int_rate=0.02, balance=0)}

    def make_deposit(self, amount, account_type='checking'):
        self.accounts[account_type].deposit(amount)
        return self

    def make_withdrawal(self, amount, account_type='checking'):
        self.accounts[account_type].withdraw(amount)
        return self

    def display_user_balance(self, account_type='checking'):
        print(f"{self.name}'s {account_type} account balance:")
        self.accounts[account_type].display_account_info()
        return self

    # Bonus: Method to transfer money between user accounts
    def transfer_money(self, amount, other_user, account_type='checking', other_account_type='checking'):
        if self.accounts[account_type].balance >= amount:
            self.accounts[account_type].withdraw(amount)
            other_user.accounts[other_account_type].deposit(amount)
            print(f"Transferred ${amount} from {self.name}'s {account_type} account to {other_user.name}'s {other_account_type} account.")
        else:
            print("Insufficient funds for transfer.")
        return self

    # Bonus: Add a new account type for the user
    def add_account(self, account_type, int_rate=0.02, balance=0):
        self.accounts[account_type] = BankAccount(int_rate, balance)
        return self

## Creating User Instances and Using Methods with Chaining and Transfers

# Create two user instances
user1 = User("John Doe", "johndoe@example.com")
user2 = User("Jane Smith", "janesmith@example.com")

# Transactions with chaining
user1.make_deposit(500).make_deposit(300, 'savings').make_withdrawal(100).display_user_balance()

# Adding a new account and performing transactions
user1.add_account('savings', 0.03, 1000)
user1.make_deposit(100, 'savings').make_withdrawal(50, 'savings').yield_interest().display_user_balance('savings')

# Transferring money between users
user2.make_deposit(200).transfer_money(100, user1, 'checking', 'savings')

## Displaying final balances
user1.display_user_balance()
user1.display_user_balance('savings')
user2.display_user_balance()

## Bonus: Displaying user info after transfers and multiple transactions
user1.transfer_money(50, user2, 'savings', 'checking').display_user_balance('savings')
user2.display_user_balance()
