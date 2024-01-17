# list1 = [3, 4, 5, 20, 5]
# print(list1.index(5))


veg = ["cabbage", "potato", "brinjal", "tomato", "gourd"]
newlist = []
for x in veg:
 if "o" in x:
   newlist.append(x)
print(newlist)



veg = ["cabbage", "potato", "brinjal", "tomato"]
newlist1 = [x for x in veg if "o" in x]
print(newlist1)
