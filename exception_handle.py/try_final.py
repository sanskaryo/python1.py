try:
 file = open("abc.txt", "r")
 content = file.read()
 # Intentionally causing an error
 result = 10 / 0
except ZeroDivisionError:
 print("Error: Division by zero!")
finally:
 # This block will be executed regardless of whether an exception occurred
    file.close()
    print("File closed.")