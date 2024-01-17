class Calculator:
    def __init__(self):
        pass

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            return "Cannot divide by zero"
        else:
            return num1 / num2

# Example Usage:
calc = Calculator()
print("Addition:", calc.add(7, 3))
print("Subtraction:", calc.subtract(20, 2))
print("Multiplication:", calc.multiply(5, 6))
print("Division:", calc.divide(30, 2))
