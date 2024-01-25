import random

class Banking:

    def __init__(self):
        self.balance = 0
        self.transactions = []

    def deposit(self):
        deposit_amount = float(input("Enter the amount you want to deposit: Rs "))
        self.balance += deposit_amount
        transaction_id = random.randint(10000, 99999)  
        self.transactions.append((transaction_id, "Deposit", deposit_amount))
        print(f"Deposited: Rs {deposit_amount}, Transaction ID: {transaction_id}")

    def withdraw(self):
        if self.balance == 0:
            print("Sorry, the balance is NIL")
        else:
            withdraw_amount = float(input("Enter the amount you want to withdraw: Rs "))
            if withdraw_amount > self.balance:
                print(f"Not sufficient. Current balance: Rs {self.balance}")
            else:
                self.balance -= withdraw_amount
                transaction_id = random.randint(10000, 99999)  
                self.transactions.append((transaction_id, "Withdrawal", -withdraw_amount))
                print(f"Withdrew: Rs {withdraw_amount}, Transaction ID: {transaction_id}")

    def check_balance(self):
        print(f"Your current balance is Rs {self.balance}")

    def display_transactions(self):
        print("All Transactions:")
        for transaction in self.transactions:
            if transaction[1] == "Deposit":
                print(f"Transaction ID: {transaction[0]}, Type: {transaction[1]}, Amount: Rs {transaction[2]}")
            else:
                print(f"Transaction ID: {transaction[0]}, Type: {transaction[1]}, Amount: Rs {abs(transaction[2])}")

obj1 = Banking()

print('''1. Deposit Money
2. Withdraw Money
3. Check Current Balance
4. Display All Transactions
5. Exit''')

while True:
    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        obj1.deposit()
    elif choice == 2:
        obj1.withdraw()
    elif choice == 3:
        obj1.check_balance()
    elif choice == 4:
        obj1.display_transactions()
    elif choice == 5:
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
