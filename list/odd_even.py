# write a program in python to count number of odd numbers and even numbers in a list



my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_count = 0
even_count = 0

for num in my_list:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(" odd numbers:", odd_count)
print("even numbers:", even_count)