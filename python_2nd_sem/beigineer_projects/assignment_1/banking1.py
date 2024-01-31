import uuid

class Banking:

    def __init__(self, account_no):
        self.balance = 0
        self.transactions = {}

    def deposit(self):
        deposit_amount = float(input("Enter the amount you want to deposit: Rs "))
        self.balance += deposit_amount
        transaction_id = uuid.uuid4()
        self.transactions[transaction_id] = deposit_amount
        print(f"Deposited: Rs {deposit_amount}, Transaction ID: {transaction_id}")

    def withdraw(self):
        if self.balance == 0:
            print("Sorry, the balance is NIL")
        else:
            withdraw_amount = float(input("Enter the amount you want to withdraw: Rs "))
            if withdraw_amount > self.balance:
                print(f"Not sufficient funds. Current balance: Rs {self.balance}")
            else:
                self.balance -= withdraw_amount
                transaction_id = uuid.uuid4()
                self.transactions[transaction_id] = -withdraw_amount
                print(f"Withdrew: Rs {withdraw_amount}, Transaction ID: {transaction_id}")

    def check_balance(self):
        print(f"Your current balance is Rs {self.balance}")

obj1 = Banking()

print('''1. Deposit Money
2. Withdraw Money
3. Check Current Balance
4. Exit''')

while True:
    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        obj1.deposit()
    elif choice == 2:
        obj1.withdraw()
    elif choice == 3:
        obj1.check_balance()
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
