# numbers = [1,2,3,4]
# max_num = numbers[0] 
# for num in numbers:
#     if num > max_num:
#         max_num = num
# print(max_num)

# for num in numbers:
# for second largest

my_list = [1, 5, 2, 7, 3, 9, 5]

largest = 0
second_largest = 0;

for num in my_list:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("The second largest element in the list is:", second_largest)