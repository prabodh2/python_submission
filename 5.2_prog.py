# bank_module.py

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrawal successful. Remaining balance: {self.balance}"
        else:
            return "Invalid withdrawal amount or insufficient funds."

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposit successful. New balance: {self.balance}"
        else:
            return "Invalid deposit amount."
# main_script.py

# Import the Bank module
from bank_module import BankAccount

# Create a BankAccount instance
account = BankAccount()

# Perform operations
print(f"Initial Balance: {account.check_balance()}")

withdraw_amount = float(input("Enter the withdrawal amount: "))
withdraw_result = account.withdraw(withdraw_amount)
print(withdraw_result)

deposit_amount = float(input("Enter the deposit amount: "))
deposit_result = account.deposit(deposit_amount)
print(deposit_result)

# Check the final balance
print(f"Final Balance: {account.check_balance()}")
