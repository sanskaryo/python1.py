
no_key = int(input("Enter the number of keys you want to enter  "))
dictionary = {}
for i in range(no_key):
    
        key = input("Enter a key  ")
        value = input("Enter a value  ")
        dictionary[key] = value
print("The dictionary is : ", dictionary)


sum = 0
print(dictionary.values())

for i in dictionary.values():

    sum+= int(i)
print("total cost" ,sum)


    
