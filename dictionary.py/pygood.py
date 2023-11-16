

x = int(input("Enter the starting element: "))
y = int(input("Enter the ending element: "))


for i in range(x,y+1):
    if i%2==0 and i%3==0:
        print(i,": Good Student!")
    elif i%2==0 and i%3!=0:
        print(i,": Good")
    elif i%2!=0 and i%3==0:
        print(i,": Student")
    else:
        print(i)
    































# start = int(input("Enter the starting number: "))
# end = int(input("Enter the ending number: "))

# for i in range(start, end+1):
#     if i % 2 == 0 and i % 3 == 0:
#         print(i, "good student")
#     elif i % 2 == 0:
#         print(i, "good")
#     elif i % 3 == 0:
#         print(i, "student")
