class BankAccount:
    def _init_(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposit of ${amount} successful. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount. Please enter a positive value."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrawal of ${amount} successful. New balance: ${self.balance}"
        elif amount <= 0:
            return "Invalid withdrawal amount. Please enter a positive value."
        else:
            return "Insufficient funds for withdrawal."

# Example usage:
if __name__ == "__main__":
    # Create a new account
    account1 = BankAccount("Smrutirupa Mishra", 9000)

    # Check initial balance
    print(f"Initial balance for {account1.account_holder}: ${account1.check_balance()}")

    # Make a deposit
    print(account1.deposit(500))

    # Check updated balance
    print(f"Updated balance: ${account1.check_balance()}")

    # Make a withdrawal
    print(account1.withdraw(200))

    # Check final balance
    print(f"Final balance: ${account1.check_balance()}")