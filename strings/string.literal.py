# # text = "abc"
# # print(text.isalpha())

# # text = "abc123"
# # print(text.isalpha())


# # count = 0
# # counta = 0
# # text = "GLA123456"
# # for char in text:
# #     if char.isalpha():
# #         count += 1   
# #     elif str.isdigit():
# #         counta += 1
# #     print(counta)

# # print(count)
countalpha = 0
countnum = 0
space = 0
special = 0
text = "Anik@  $#12345"
for char in text:
    if char.isalpha():
        countalpha += 1  
    elif char.isdigit():
        countnum += 1
    elif char.isspace():
        space += 1
    else:
        special += 1
        
print(f"The special characters are {special}")
print(f"The digit count is {countnum}")
print(f"The number of alphabets are {countalpha}")
print(f"The number of spaces are {space}")
