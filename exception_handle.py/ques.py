# 5. What will be the output of the following program?
# Rewritten code to handle exceptions

def func1(i):
  try:
    return i/0
  except ZeroDivisionError as e:
    print("Division by zero error:", e)

def func2():
  try:  
    raise Exception("Raising exception")
  except Exception as e:
    print("Exception raised in func2:", e)

def func3():

  try:
    func1(5)
  except Exception as e:  
    print("Exception in func1:", e)

  try:  
    func2()
  except Exception as e:
    print("Exception in func2:", e)

func3()

