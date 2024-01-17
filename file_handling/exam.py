

















# f = open("data.txt", "r")
# lines = 0
# words = 0 
# alphabets = 0
# digits = 0
# for line in f:
#     lines += 1
#     words_in_line = line.split()
#     words += len(words_in_line)
    
#     for word in words_in_line:
#         for char in word:
#             if char.isalpha():
#                 alphabets += 1
#             elif char.isdigit():
#                 digits += 1
                
# print(f"Number of lines: {lines}") 
# print(f"Number of words: {words}")
# print(f"Number of alphabets: {alphabets}")
# print(f"Number of digits: {digits}")





























n = int(input("Enter number of elements: "))
list1 = []
for i in range(1,n+1):
    num = int(input("Enter number: "))
    list1.append(num)
    
fact = 1
for i in list1:    
    for j in range(1,i+1):
        fact = fact * j
    print(fact, end=" ")
    fact = 1
