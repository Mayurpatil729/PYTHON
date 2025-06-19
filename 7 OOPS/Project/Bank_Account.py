# Bank Account
class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount {amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Amount {amount} withdrawn successfully.")
        else:
            print("Insufficient balance. Withdrawal not allowed.")

    def display_info(self):
        print(f"Depositor Name: {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")


# Example usage
account = BankAccount(name="Mayur Patil",
                      account_number="123456", balance=1000)

account.display_info()

account.deposit(500)
account.display_info()

account.withdraw(200)
account.display_info()

account.withdraw(1500)
account.display_info()
