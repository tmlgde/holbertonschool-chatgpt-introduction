class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        if amount <= 0:
            print("❌ Deposit amount must be greater than 0.")
            return
        self.balance += amount
        print("✅ Deposited ${:.2f}".format(amount))
        print("💰 Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Withdrawal amount must be greater than 0.")
            return
        if amount > self.balance:
            print("❌ Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("✅ Withdrew ${:.2f}".format(amount))
            print("💰 Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        print("💰 Current Balance: ${:.2f}".format(self.balance))

def main():
    cb = Checkbook()
    while True:
        action = input("\nWhat would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()

        if action == 'exit':
            print("👋 Exiting. Thank you for using the Checkbook!")
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("❌ Invalid amount. Please enter a numeric value.")
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("❌ Invalid amount. Please enter a numeric value.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("❌ Invalid command. Please try again.")

if __name__ == "__main__":
    main()

