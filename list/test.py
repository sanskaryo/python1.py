# Assignment 3: Factorial Calculator
# Problem: Create a program that calculates the factorial of a given number.
# The factorial of a number is the multiplication of 
# all the numbers between 1 and the number itself

num = int(input("Enter a number: "))
factorial = 1
for i in range(1,num+1):
   factorial = factorial * i
print("The factorial of", num, "is", factorial)
