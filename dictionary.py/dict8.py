# wap in python that allows a user to input key-value pair to construct a dictionary.






no_key = int(input("Enter the number of keys you want to enter  "))
dictionary = {}
for i in range(no_key):

        key = input("Enter a key  ")
        value = input("Enter a value  ")
        dictionary[key] = value
print("The dictionary is  ")
print(dictionary)































# dictionary = {}

# while True:
#     key = input("Enter a key (or 'q' to quit): ")
#     if key == 'q':
#         break

#     value = input("Enter a value: ")
#     dictionary[key] = value

# print("Constructed dictionary:", dictionary)
# def construct_dictionary():
#     dictionary = {}

#     while True:
#         key = input("Enter a key (or 'q' to quit): ")
#         if key == 'q':
#             break

#         value = input("Enter a value: ")
#         dictionary[key] = value

#     return dictionary

# user_dictionary = construct_dictionary()
# print("Constructed dictionary:", user_dictionary)
