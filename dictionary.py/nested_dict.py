course={
    'solidity':{'platform':'coursera','duration':'4weeks'},
    'python':{'platform':'udacity','duration':'2weeks'},
    'java':{'platform':'udemy','duration':'3weeks'},
}

print(course)
print()P
print(course['python']['platform'])

print()

for x,y in course.items():
    print(x,y)

# def sum_numbers(start, end):
#     even_sum = 0
#     odd_sum = 0

#     for number in range(start, end + 1):
#         if number % 2 == 0:
#             even_sum += number
#         else:
#             odd_sum += number

#     return even_sum, odd_sum

# start = int(input("Enter the start of the range: "))
# end = int(input("Enter the end of the range: "))

# even_sum, odd_sum = sum_numbers(start, end)

# print("The sum of even numbers in the range is:", even_sum)
# print("The sum of odd numbers in the range is:", odd_sum)













# for k,v in course.items():
#     print(k,v)
# for k1,v1 in v.items():
#         print(k1,v1)
    