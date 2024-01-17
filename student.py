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


while True :

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
        print("Update Student Information")
        ask = input("Enter ID to update: ")
        if ask in student_database:
            detail = input("Enter updated details: ")
            newd = student[ask]
            student_database[2] = detail

            print(f" the student id detail {name} has been updated")
        else: 
            print("The thing which you asked for is not present")
            
            
    elif choice == 4:
        print("Search Menu")
        search = input("Enter the name which you want to search ")
        
        if search in student_database:
            print(f"the detail {search} is found")
        else :
            print("not found")
            
    elif choice == 5:
        print("average age calculator")
        
    elif choice == 6:
        print("remove student by id")
            
            
             
            
            
    elif choice == 7:
        print("exiting from the program")
        break
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            
    
            
            
            
            
            
            
      















































