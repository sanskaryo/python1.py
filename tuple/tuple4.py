# t1 = ("e1","e2","e3")
# y = list(t1)
# y[1] = "e4"
# # b = tuple(y)
# print(y)
# y.append("e5")
# s = tuple(y)
# print(s)

#PACKING & UNPACKING
students = ("s1","s2","s3")
(one,two, three)=students 
print(one)
print(two)
print(three)

(one,*two)=students
print(two)