#there is a file name data.txt which store which store some data , write a program in python without  def , without comments that read the content of  that file   , and count how many line , words , alphabets and digits are thee in the file

# f = open("data.txt" , "w")

# def facT():
#     for i in range(1,n+1):
#         fact = fact * i
#     return fact
        
        
        
    
# f = open("data.txt" , "r")



































f = open("data.txt", "r")
lines = 0
words = 0 
alphabets = 0
digits = 0

for line in f:
    lines += 1
    words_in_line = line.split()
    words += len(words_in_line)
    
    for word in words_in_line:
        for char in word:
            if char.isalpha():
                alphabets += 1
            elif char.isdigit():
                digits += 1
                
print(f"Number of lines: {lines}") 
print(f"Number of words: {words}")
print(f"Number of alphabets: {alphabets}")
print(f"Number of digits: {digits}")
