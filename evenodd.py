# n = int(input("Enter the number: "))

# sum_odd = 0
# sum_even = 0

# for i in range(1, n+1):
#     if i % 2 == 0:
#         sum_even += i
#         print(f"{i} is an even number")
#         print(f"The sum of the first {i} even numbers is {sum_even}")
#     else:
#         sum_odd += i
#         print(f"{i} is an odd number")
#         print(f"The sum of the first {i} odd numbers is {sum_odd}")

n = int(input("Enter the number: "))

sum_odd = 0
sum_even = 0

for i in range(1, n+1):
    if i % 2 == 0:
        sum_even += i
        print(f"{i} is an even number. The sum of the first {i//2} even numbers is {sum_even}")
    else:
        sum_odd += i
        print(f"{i} is an odd number. The sum of the first {(i+1)//2} odd numbers is {sum_odd}")




# # n = int(input("enter the number: "))

# # sum = 0
# # even = 0
# # for i in range(1, n+1):
# #     if i%2==0:
# #         print(f"{i} is even number")
# #         even += i
# #         print(f"the sum of first  {n}   number is {even} ")
# #     else:
# #         sum  += i
# #         print(f"the sum of first  {n} odd  number is {sum} ")
    
        