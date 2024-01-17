def modify_set(s):
    s.add(4)
    print("Inside the function: ", s)
    
my_set = {1,2,3}
modify_set(my_set)
print("Outside the function", my_set)