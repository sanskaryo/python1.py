#you are given two list , one containing the names of students and the other containhg
# their corresponing scores in test , Create a dict where the keys are the student names and values are their score , then find
# and print the avergae score 
# You are allowed to use len() only


no_stud = int(input("Enter the number of students you want to enter  "))
dictionary = {}
for i in range(no_stud):
    
        key = input("Enter student name  ")
        value = int(input("Enter score "))
        dictionary[key] = value
print("The dictionary is : ", dictionary)

total_score = 0
num_score = 0

for key, value in dictionary.items():
    total_score += value
    num_score += 1
    
average_score = total_score / num_score

print("the average score is ", average_score)






























# average = 0
# # for i in dictionary.values:
# #     for key in len(value):
        
        
# #         # Create a list of numbers
# # numbers = [1, 2, 3, 4, 5]

# # Get the length of the list
# length = len(value)

# # Calculate the average of the list
# average = sum(value) / length

# # Print the average
# print(average)





# student_grades = {'Rahim': 92, 'Ram': 85, 'Dhananjay': 95, 'Ron': 95, 'Ravinder': 78}



