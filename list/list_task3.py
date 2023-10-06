my_list = []
num_items = int(input("enter the no items : "))

for i in range(num_items):
    item = input(f"Enter item{i+1}:")
    my_list.append(item)
    
print("final list", my_list)