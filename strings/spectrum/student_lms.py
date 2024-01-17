students = []

while True:
    print("\n=====Student Management System")
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Remove Student")
    print("5. Exit")
    
    choice = input("Enter your choice(1/2/3/4/5): ")
    
    if choice == "1":
        name = input("Enter Student name:")
        age = int(input("Enter Student age:"))
        grades = [int(x) for x in input("Enter grades(comma-seprated):").split(',')]
        students.append([name,age,grades])
        print(f"\n Student '{name}' has been added to the system.")
        
    elif choice == "2":
        
        print("\n====Student====")
        
        if not students:
            print("No students found.")
        else:
            for student in students:
                print(f"Name: {student[0]}")
                print(f"Age: {student[1]}")
                print(f"Grades: {student[2]}")
                
                print("=========")
                
    elif choice == "3":
        search_name = input("Enter student name to search:")
        
        for student in students:
            if student[0] == search_name:
                print(f"\nName: {student[0]}")
                print(f"\nAge: {student[1]}")
                print(f"\nGrades: {student[2]}")
                break
        else:
            print(f"\nStudent '{search_name}' not found.")
        
    elif choice == "4":
        remove_name = input("Enter student name to remove:")
        
        removed = False 
        for student in students:
            if student[0] == remove_name:
                students.remove(student)
                removed = True
                break
            if not removed:
                print(f"\nStudent '{remove_name}' not found.")
                
    elif choice == "5":
        break
    else:
        print("\n invalid choice. Try again")    