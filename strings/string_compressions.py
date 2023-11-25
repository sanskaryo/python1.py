# sample = "aabbbccdddd"
# compression = ""
# count = 1

# for i in range(len(sample)-1):
#     if sample[i] == sample[i+1]:
#         count += 1
#     else:
#         compression += sample[i] + str(count)
#         count = 1

# compression += sample[-1] + str(count)  # Move this line inside the loop
# print(compression)\
first = input("Enter the string: ")
second = input("Enter the string : ")

if len(first) != len(second):
    is_rotation = True
else:
    concatenated = first + second
    if second is concatenated:
        is_rotation = True
    else:
        is_rotation = False
        
print(f" the second string is a rotation of the first string is {is_rotation} ")
    
  