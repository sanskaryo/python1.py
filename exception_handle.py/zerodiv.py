def divide_numbers():
 try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
 except ValueError:
    print("Error: Please enter valid numbers.")
 except ZeroDivisionError:
    print("Error: Division by zero!")
 else:
    print("Result:", result)
divide_numbers()
