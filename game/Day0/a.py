class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds.")

    def get_balance(self):
        print(f"Balance for {self.name}: ${self.balance}")


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, initial_balance=0):
        if name not in self.accounts:
            self.accounts[name] = Account(name, initial_balance)
            print(f"Account created for {name} with an initial balance of ${initial_balance}.")
        else:
            print("Account already exists.")

    def get_account(self, name):
        if name in self.accounts:
            return self.accounts[name]
        else:
            print("Account does not exist.")
            return None


def main():
    bank = Bank()

    while True:
        print("\nWelcome to the Python Bank!")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter account holder's name: ")
            initial_balance = float(input("Enter initial balance: "))
            bank.create_account(name, initial_balance)
        elif choice == '2':
            name = input("Enter account holder's name: ")
            account = bank.get_account(name)
            if account:
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
        elif choice == '3':
            name = input("Enter account holder's name: ")
            account = bank.get_account(name)
            if account:
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
        elif choice == '4':
            name = input("Enter account holder's name: ")
            account = bank.get_account(name)
            if account:
                account.get_balance()
        elif choice == '5':
            print("Thank you for banking with us. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
