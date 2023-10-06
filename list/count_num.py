# my_list = [1, 2, 3, 2, 1, 4, 2, 5]
# # element = input("enter the input")
# find_num = 2

# count = my_list.count(find_num)

# print(f"the ocurrence of {find_num} is: {count}")



my_list = [1, 2, 3, 2, 1, 4, 2, 5]
num_find = int(input("Enter the number for which you have to find occurene: "))

count = 0
for num in my_list:
    if num == num_find:
        count += 1

print(f"The occurrence of {num_find} is: {count}")