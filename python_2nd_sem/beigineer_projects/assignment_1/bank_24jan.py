class Bank:
    def __init__(self, name, acc_num, balance=0):
        self.name = name
        self.balance = balance
        self.acc_num = acc_num

    def deposit(self, amount):
        print("Amount Deposited =", amount)
        self.balance = self.balance + amount
        print(self.check_balance())

    def withdraw(self, amount):
        if amount <= self.balance:
            print("Amount Withdrawn =", amount)
            self.balance = self.balance - amount
            print("Balance Left")
            print(self.check_balance())
        else:
            print("Not sufficient Balance")

    def check_balance(self):
        return f'''
Name of Account Holder = {self.name}
Account Balance = {self.balance}
'''


class SavingAccount(Bank):
    def __init__(self, name, acc_num, balance=0, interest_rate=.04):
        super().__init__(name, acc_num, balance)
        self.interest_rate = interest_rate

    def addInterest(self):
        amount = self.balance * self.interest_rate
        self.balance += amount


class CheckingAccount(Bank):
    def __init__(self, name, acc_num, balance, overdraft=100):
        super().__init__(name, acc_num, balance)
        self.overdraft = overdraft

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft:
            self.balance -= amount
        else:
            print('Insufficient balance')
            
    
    
    account = []
    count = 0
    while 1:
        print('''
        welcome to GLA bank
        which account you want to open 
            1. Saving Account
            2. Checking Account
            3. Current Account
            4. Exit
        ''')
        choice = int(input("Enter your choice 1/2/3"))
        if choice == 1:
            ac = SavingAccount(10000001,'ravi', 100)
            account.append(ac)
            
            while 1:
                print('''
                    Menu
                    
            1. Deposit
            2. Withdraw
            3. Check Ba
            4. Exit
        ''')
                


    # saving_account1 = SavingAccount('ravi', 1230099, 100)
    # checking_account1 = CheckingAccount('saket', 113133, 1200)














































# class bank:
#     def _init_(self,name,acc_num,balance=0):
#         self.name=name
#         self.balance=balance
#         self.acc_num=acc_num
# class SavingAccount(bank) :
#     def __init__(self, name,acc_num,balance=0,intrest_rate=.04):
#         self.intrest_rate= intrest_rate
#         super().__init__(name,acc_num,balance)
        
#     def addIntrest(self):
#         amount = self.balance * self.intrest_rate
#         self.balance += amount
        
# class CheckingAccount(bank):
#     def __init__(self,name,acc_num,balance,overdraft=100):
#         super().__init__(name,acc_num,balance)
#         self.overdraft = overdraft
    
#     def withdraw(self,amount):
#         if amount <= self.balance + self.overdraft:
#             self.balance -= amount
#         else:
#             print('insufficient balance')
            


# # if __name__ == '__main__' :
#     saving_account1 = SavingAccount(1230099, 'ravi' , 100)
#     CheckingAccount1 = CheckingAccount(113133, 'saket',1200)    

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

#     def deposit(self,amount):
#             print("Amount Deposited =",amount)
#             self.balance=self.balance+amount
#             print(per1.check_balance())
    
#     def withdraw(self,amount):
#         if amount<=self.balance:
#             print("Amount Withdraw =",amount)
#             self.balance=self.balance-amount
#             print("Balance Left")
#             print(per1.check_balance())
#         else:
#             print("Not sufficient Balance")
    
#     # def last_transactions(self):
        


#     def check_balance(self):
#         return f'''
# Name of Account Holder = {self.name}
# Account Balance = {self.balance}
# '''
    
# acc_holder=input("Enter the name of Account Holder")
# initial_amount=eval(input("Enter the initial amount"))
# per1=bank(acc_holder,initial_amount)



# while 1:
#     op = eval(input("Enter the Operation you want to perform [1:Deposit   2:Withdraw    3:Check Balance  4:Last Transaction]"))
#     if op==1:
#         Deposite_amount=eval(input("Enter the Amount to be deposited"))
#         per1.deposit(Deposite_amount)
#     elif op==2:
#         WithDraw_amount=eval(input("Enter the Amount to be withdrawn"))
#         per1.withdraw(WithDraw_amount)
#     elif op==3:
#         print(per1.check_balance())
    
#     else:
#            print("Wrong Operation")