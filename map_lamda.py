# user_input = input("enter numbers seprated by spaces: ")

numbers = list(map(int, input().split()))

squared_numbers = list(map(lambda x: x ** 2, numbers))
cubic_numbers = list(map(lambda x: x ** 3, numbers))

print("original_numbers" , numbers)

print()

print("squared_numbers" , squared_numbers)

print()

print("cubic_numbers" , cubic_numbers)

even_odd_check = list(map(lambda x : "even" if x % 2 == 0 else "odd" , numbers))

print("Result:", even_odd_check)
