list1 = [1,3,63,6,46,3]


to_delete = int(input("enter the no to delete: "))

if to_delete in list1:
    list1.remove(to_delete)
    print("after removig element" , list1)
else:
    print("element no found in list")

# for element in list1:
    
