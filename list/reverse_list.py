# num_list = [1,2,3,4,5]
# num_list.sort(reverse = True)
# print(num_list)
# print(num_list[-1])
my_list= []
num_items = int(input("enter the value: "))
for i in range(num_items):
    item = input(f"enter the input {i + 1}: ")
    my_list.append(item)
    
    
    
my_list = [1, 2, 3, 4, 5]

reversed_list = my_list[::-1]
print(reversed_list)

