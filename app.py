import sys
class BankingApp:
    def __init__(self):
        self.balance = 1000.0  
    def check_balance(self):
        return f"Your current balance is: ${self.balance:.2f}"
    def deposit(self, amount):
        if amount <= 0:
            return "Invalid deposit amount."
        self.balance += amount
        return f"Successfully deposited ${amount:.2f}. {self.check_balance()}"
    def run_menu(self):
        print("\n=== WELCOME TO THE BANK ===")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Exit")
        
        choice = input("Enter option (1-3): ")
        if choice == '1':
            print(self.check_balance())
        elif choice == '2':
            try:
                amt = float(input("Enter deposit amount: "))
                print(self.deposit(amt))
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '3':
            print("Thank you for banking with us!")
            sys.exit(0)
        else:
            print("Invalid option.")
if __name__ == "__main__":
    app = BankingApp()

    while True:
        app.run_menu()
