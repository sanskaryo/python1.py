# Input of Principal Amount
principal = eval(input("Enter Principal amount (p) : $"))

# Input of Annual Interest rate
rate = float(input("Enter Annual Interest rate (r) "))

# Input of Loan term
n = float(input("Enter Loan term in years (n) "))

# Conversion of Annual interest rate into Monthly interest rate
r = (rate/12)/100

# Conversion of loan terms in years into total number of payment
n = n*12

# Formula to calculate Monthly payment
M = (principal * r * ((1+r)**n))/(((1+r)**n)-1)

# Output
print("Monthly payment:"," %.2f"%M,"Dollars")

