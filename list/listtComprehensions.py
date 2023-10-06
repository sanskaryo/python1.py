squares = [x ** 2 for x in range(5)]
print(squares)

print()

even_number = [x for x in range(10) if x % 2 ==  0]
print(even_number)


print()

odd_number = [x for x in range(10) if x % 2 !=  0]
print(odd_number)

print()

results = ['pass' if score >= 60 else 'fail' for score in[75,30,85,12]]
print(results)



print()

names = ["john", "jane", "janeman", "Shehnshah"]
name_length = [len(name) for name in names]
print(name_length)

print()

num = [ x +2  for x in range(100) if x %5 == 0  ]
print(f"numbers divisible by 5 and adding 2 " ,num)