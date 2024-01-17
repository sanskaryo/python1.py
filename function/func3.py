def modify_int(x):
    x += 10
    print("Inside the fxn : ", x)
    
num = 5
modify_int(num)
print("Outside the fxn", num)

print()

def modify_string(s):
    s += " Duniya"
    print("Inside the function : ", s)
    
greeting = "Hello"
modify_string(greeting)
print("Outside the function : ", greeting)
print()

    
def modify_tuple(t):
    t += (4,5)
    print("Inside the function : ", t)
    
coordinates = (1,2,3)
modify_tuple(coordinates)
print("Outside the function : ", coordinates)

