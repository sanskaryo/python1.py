def deposit(self,amount):
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