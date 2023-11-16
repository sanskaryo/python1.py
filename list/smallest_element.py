
my_list = [4, 2, 9, 5, 1]
my_list.sort()
print(my_list)
smallest = my_list[0]

for element in my_list:
    if element < smallest:
        smallest = element

print(smallest)


