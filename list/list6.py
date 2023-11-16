list1 = "a","b", "c"
finallist = list(list1)
print(finallist)
# list2 = [1,2,3]
# finalList = list1.copy()
# print(finalList)

# list3 = list1 + list2
# print(list3)

list1 = ["a", "b", "c"]
list2 = [1,2,3]

for x in list2:
    list1.append(x)
    
print(list1)
