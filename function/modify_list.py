# def modify_list(lst):
#     lst.append(4)
#     lst[0] = 99
#     print("Inside the Function : "  ,lst)
    
# numbers = [1,2,3]
# modify_list(numbers)
# print("Outside the function", numbers)
    
    
def list_square(num):
    squares = [x ** 2 for x in num]
    return squares
    
print(list_square([5, 10,15]))


    
    