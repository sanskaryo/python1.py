my_list = [1,2,3,4,5,5,3,3,5,5]


result = []

for element in my_list:
    if element not in result:
        result.append(element)

print(result)

