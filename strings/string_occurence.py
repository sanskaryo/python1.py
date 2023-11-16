# word = "zindagani"

# char_count = {}

# for char in word:
#     if char in char_count:
#         char_count[char] += 1
#     else:
#         char_count[char] = 1
        
# for char,count in char_count.items():
#     print(char,count)


# wap to count the number of vowels and consonants in a string

given_string = "aeiocuswAEIDOYHGDi"

vowels = "aeiouAEIOU"

num_vowels = 0
num_consonats = 0

for char in given_string:
    if char in vowels:
        num_vowels +=1
num_consonats = len(given_string) - num_vowels

print(f"number of vowels  {num_vowels} , consonants {num_consonats}")