# Student Admission Process Management System
# Problem Statement:
# You are tasked with creating a Student Admission Process Management System in a University using 
# lists and dictionaries. The system will allow users to perform various operations related to managing 
# student admissions. Implement the following menu-based operations:
# 1. Admit Student:
# • Collect student details (Student ID, Name, Age, and Course).
# • Admit the student to the university.
# 2. Display Student List:
# • Display details of all admitted students.
# 3. Update Student Information:
# • Update information (Name, Age, or Course) of a specific student.
# 4. Search Student by ID:
# • Search for a student based on their ID.
# 5. Calculate Average Age:
# • Calculate and display the average age of all admitted students.
# 6. Remove Student by ID:
# • Remove a student from the list based on their ID.
# 7. Exit:
# • Exit the program.




student_database = []


print("===Student Database===")

print("1. Admit Student")

print("2. Display Student List")

print("3. Update Student Information")

print("4. Search Student by ID")

print("5. Average Age")

print("6. Remove Student by ID")

print("7. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    Id = input("Enter ID: ")
    name = input("Enter name: ")
    Age = input("Enter the age")
    Course = input("Enter the course")
    student_database.append({'Student_id': Id ,'name': name,'Age': Age,'Course': Course})
    
    print("Student Admitted Successfully")
    

elif choice == 2:
    print("Student List")
    for student in student_database:
        print(student)
        
elif choice == 3:
    
    ask = input("Enter the detail to be updated: ")
    
    









































    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    student = {}
while True:
    cho = int(input("\n1. Add new student\n2. Display student details\n3. Display average marks\n4. Display percentage of all students\n5. Display grade of a specific student\n6. Exit\nEnter your choice: "))
    if cho == 1:
        name = input("\nEnter student name: ")
        roll = int(input("Enter roll number: "))
        marks_1 = int(input("Enter marks in Subject 1: "))
        marks_2 = int(input("Enter marks in Subject 2: "))
        marks_3 = int(input("Enter marks in Subject 3: "))
        student[roll] = [name, marks_1, marks_2, marks_3]
    elif cho == 2:
        ask = int(input("Enter roll number of the student: "))
        if ask in student:
            details = student[ask]
            print(f"Name: {details[0]}\nRoll Number: {ask}\nMarks in Subject1: {details[1]}\nMarks in Subject2: {details[2]}\nMarks in Subject3: {details[3]}\n")
        else:
            print("Student not found")
    elif cho == 3:
        print("Average Marks:")
        data = student.values()
        m1 = []
        m2 = []
        m3 = []
        for i in data:
            m1.append(i[1])
            m2.append(i[2])
            m3.append(i[3])
        print(f"Subject 1: {sum(m1)/len(m1)}")
        print(f"Subject 2: {sum(m2)/len(m2)}")
        print(f"Subject 3: {sum(m3)/len(m3)}")
    elif cho == 4:
        print("Percentage of Students:")
        for i in student:
            data = student[i]
            print(f"{data[0]}(Roll Number {i}): {(data[1]+data[2]+data[3])/3}%")
    elif cho == 5:
        ask = int(input("\nEnter roll number of the student: "))
        if ask in student:
            details = student[ask]
            percentage = ((details[1]+details[2]+details[3])/3)
            if percentage >= 86:
                grade = 'A'
            else:
                grade = 'B'
            print(f"Grade of Student:\nName: {details[0]}\nRoll Number: {ask}\nPercentage: {percentage}%\nGrade: {grade}")
        else:
            print("Student not found")
    elif cho == 6:
        print("Thanks for using")
        break
    else:
        print("Invalid choice")
