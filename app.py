import sys

class BankingApp:
    def __init__(self):
        self.balance = 1000.0

    def check_balance(self):
        return f"Balance: ${self.balance}"

    def deposit(self, amount):
        if amount <= 0: return "Invalid"
        self.balance += amount
        return f"Deposited ${amount}"

    def withdraw(self, amount):
        if amount <= 0: return "Invalid"
        if amount > self.balance: return "Insufficient funds"
        self.balance -= amount
        return f"Withdrew ${amount}"

    def run(self):
        print("\n1. Balance\n2. Deposit\n3. Withdraw\n4. Exit")
        c = input("Choice: ")
        if c == '1': print(self.check_balance())
        elif c == '2': print(self.deposit(float(input("Amount: "))))
        elif c == '3': print(self.withdraw(float(input("Amount: "))))
        elif c == '4': sys.exit(0)

if __name__ == "__main__":
    app = BankingApp()
    while True: app.run()
