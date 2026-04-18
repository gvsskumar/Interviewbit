# Create a BankAccount class that raises a custom exception when a withdrawal amount exceeds the account balance.
# Custom Exception
class InsufficientBalanceError(Exception):
    pass


# BankAccount Class
class BankAccount:
    
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        try:
            if amount > self.balance:
                raise InsufficientBalanceError("Withdrawal amount exceeds account balance.")
            
            self.balance -= amount
            print("Withdrawal successful.")
            print("Remaining Balance:", self.balance)

        except InsufficientBalanceError as e:
            print("Custom Exception:", e)


# Create account
account = BankAccount(5000)

# Withdraw money
account.withdraw(2000)   # Valid withdrawal
account.withdraw(4000)   # Exceeds balance