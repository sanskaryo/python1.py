# # num1 = int ("Enters the number"())
# list1 = [1, 2, 3, 4, 5]
# listadd = (input("Enter the number to add: "))  
# list1.append(listadd)  
# sum1 = sum(list1)
# print(list1)

# for _ in range()
# # sum1 = sum(numbers)
# # print(sum1)
numbers = [1, 2, 3, 4, 5]
listadd = int(input("Enter the number to add: "))
numbers.append(listadd)

sum_of_numbers = 0

for num in numbers:
    sum_of_numbers += num

print("The sum is:", sum_of_numbers) 
