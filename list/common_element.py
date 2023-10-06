

# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]

# not_common = []

# for element in list1 + list2:
#     if element not in list2:
#         not_common.append(element)



#     print("Elements  not common:")
#     for element in not_common:
#       print(element)
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]

# not_common = []

# for element in list1 + list2:
#     if element not in list1 + list2:
#         not_common.append(element)


# print("Elements that are not common:")
# for element in not_common:
#     print(element)

list1 = [1, 2, 3, 4, 5,8,4]
list2 = [4, 5, 6, 7, 8]

not_common = []

for element in list1:
    if element not in list2:
        not_common.append(element)

for element in list2:
    if element not in list1:
        not_common.append(element)

# print("Elements that are not common:")
for element in not_common:
    print(element ,end=" ")
