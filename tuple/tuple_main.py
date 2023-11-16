# using concat
a2 = ()
for i in range(1, 10):
    a2 += (i,) # two tuples can concat or append like string but 
# change the id every time
print(a2, type(a2)) # (1, 2, 3, 4, 5, 6, 7, 8, 9) <class 'tuple'>
# tuple generator (iterator)
a3 = (i for i in range(1, 10))
print(a3, type(a3)) 
# <generator object <genexpr> at 0x0E324F30> 
# <class 'generator'>
# A generator is a special kind of iterator, which stores the 
# instructions for how to generate each
# of its members, in order, along with its current state of 
# iterations.
# # It generates each member, one at a time, only as it is requested via 
# iteration.
tp = tuple(a3) # gen to tuple type
print(tp, type(tp)) # (1, 2, 3, 4, 5, 6, 7, 8, 9) <class 'tuple'>
# tuple other operation
# membership
t = (2, 4, 6, 89, 1)
item = 1
out = item in t
print(out) # True
item = 100
out = item in t
print(out) # False
# multiplication with number
t = (2,5)
out = t*2
print(out, type(out)) # (2, 5, 2, 5) <class 'tuple'>
out = t*0
print(out, type(out)) # () <class 'tuple'>
# Addition (concat)
t1 = (2, 4)
t2 = (4, 8)
t = t1 + t2
print(t, type(t)) # (2, 4, 4, 8) <class 'tuple'>
# iteration with tuple (traverse)
t = (2, 54, 'hello')
for i in t:
    print(i)
# 2
# 54
# hello


#break string if tupple occurs
lst = [1, 2, 3, (1, 2), 4, 5]
count = 0

for elem in lst:
    if isinstance(elem, tuple):
        break
    count += 1

print(count)  # Output: 3
