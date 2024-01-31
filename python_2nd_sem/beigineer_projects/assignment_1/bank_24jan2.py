class Bank:
    def __init__(self, name, acc_num, balance=0):
        self.name = name
        self.balance = balance
        self.acc_num = acc_num

    def deposit(self, amount):
        print("Amount Deposited =", amount)
        self.balance += amount
        print(self.check_balance())

    def withdraw(self, amount):
        if amount <= self.balance:
            print("Amount Withdrawn =", amount)
            self.balance -= amount
            print("Balance Left")
            print(self.check_balance())
        else:
            print("Not sufficient Balance")

    def check_balance(self):
        return f'''
Name of Account Holder: {self.name}
Account Balance: {self.balance}
'''


class SavingAccount(Bank):
    def __init__(self, acc_num, name, balance=0, interest_rate=0.04):
        super().__init__(name, acc_num, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        amount = self.balance * self.interest_rate
        self.balance += amount
        print(f"Interest added: {amount}, New balance: {self.balance}\n")


class CheckingAccount(Bank):
    def __init__(self, acc_num, name, balance, overdraft=100):
        super().__init__(name, acc_num, balance)
        self.overdraft = overdraft

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft:
            self.balance -= amount
            print(f"Withdraw: {amount}, New Balance: {self.balance}\n")
        else:
            print('Insufficient balance\n')


if __name__ == '__main__':
    accounts = []

    while True:
        print('''
        Welcome to GLA bank
        Which account do you want to open?
            1. Saving Account
            2. Checking Account
            3. Display All Saving Accounts
            4. Display All Checking Accounts
            5. Exit
        ''')
        choice = int(input("Enter your choice (1/2/3/4/5): "))

        if choice == 1:
            acc_num = int(input("Enter account number: "))
            name = input("Enter account holder's name: ")
            initial_balance = float(input("Enter initial balance: "))
            saving_account = SavingAccount(acc_num, name, initial_balance)
            accounts.append(saving_account)

            while True:
                print('''
                    Menu
                    
                1. Deposit
                2. Withdraw
                3. Add Interest
                4. Check Balance
                5. Display All Saving Accounts
                6. Exit
                ''')
                operation = int(input("Enter your choice (1/2/3/4/5/6): "))

                if operation == 1:
                    amount = float(input("Enter the amount to deposit: "))
                    saving_account.deposit(amount)
                elif operation == 2:
                    amount = float(input("Enter the amount to withdraw: "))
                    saving_account.withdraw(amount)
                elif operation == 3:
                    saving_account.add_interest()
                elif operation == 4:
                    print(saving_account.check_balance())
                elif operation == 5:
                    for acc in accounts:
                        if isinstance(acc, SavingAccount):
                            print(acc.check_balance())
                elif operation == 6:
                    break
                else:
                    print("Invalid choice. Please enter a valid option.")

        elif choice == 2:
            acc_num = int(input("Enter account number: "))
            name = input("Enter account holder's name: ")
            initial_balance = float(input("Enter initial balance: "))
            checking_account = CheckingAccount(acc_num, name, initial_balance)
            accounts.append(checking_account)

            while True:
                print('''
                    Menu
                    
                1. Deposit
                2. Withdraw
                3. Check Balance
                4. Display All Checking Accounts
                5. Exit
                ''')
                operation = int(input("Enter your choice (1/2/3/4/5): "))

                if operation == 1:
                    amount = float(input("Enter the amount to deposit: "))
                    checking_account.deposit(amount)
                elif operation == 2:
                    amount = float(input("Enter the amount to withdraw: "))
                    checking_account.withdraw(amount)
                elif operation == 3:
                    print(checking_account.check_balance())
                elif operation == 4:
                    for acc in accounts:
                        if isinstance(acc, CheckingAccount):
                            print(acc.check_balance())
                elif operation == 5:
                    break
                else:
                    print("Invalid choice. Please enter a valid option.")

        elif choice == 3:
            for acc in accounts:
                if isinstance(acc, SavingAccount):
                    print(acc.check_balance())

        elif choice == 4:
            for acc in accounts:
                if isinstance(acc, CheckingAccount):
                    print(acc.check_balance())

        elif choice == 5:
            break

        else:
            print("Invalid choice. Please enter a valid option.")
