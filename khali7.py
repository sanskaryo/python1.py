a = " python is grt"
b = a[::2]
print(b)




























# Database = []

# while True:
#     print("====Employee Database====")
#     print("1. Add Employee")
#     print("2. Retrieve Employee")
#     print("3. Update Salary")
#     print("4. Display All Employees")
#     print("5. Exit")
    
#     choice = int(input("Enter your Choice"))
    
#     if choice == 1:
#         Id = int(input("Enter Employee Id: "))
#         Name = input("Enter name of Employee")
#         Age = int(input("Enter the age of employee"))
#         Gender = input("Enter the Gender")
#         Position = input("Enter the Position")
#         Salary = int(input("Enter the salary in rupees"))
#         Database.append([Id, Name, Age, Gender, Position, Salary])
#         print(f"Employee {Name} added successfully")
        
#     elif choice == 2:
#         print("===Employee===")
#         Retrieve = input("Enter the name of employee to retrieve")
#         if Retrieve in [employee[1] for employee in Database]:
#             details = next(employee for employee in Database if employee[1] == Retrieve)
#             print(f"Employee {Retrieve} found")
#             print(f"Id: {details[0]}")
#             print(f"Name: {details[1]}") 
#         else:
#             print(f"Employee {Retrieve} not found")
        
#     elif choice == 3:
#         print("==Employee Details Update==")
#         Update = input("Enter the name of employee to update")
#         if Update in [employee[1] for employee in Database]:
#             updated_salary = int(input("Enter the updated salary "))
#             details = next(employee for employee in Database if employee[1] == Update)
#             details[5] = updated_salary
#             print(f"Employee {Update} found and salary updated")
#         else:
#             print(f"Employee {Update} not found")
            
#     elif choice == 4:
#         print("===Employee Details===")
#         print("Id\tName\tAge\tGender\tPosition\tSalary")
#         for i in range(len(Database)):
#             print(f"{Database[i][0]}\t{Database[i][1]}\t{Database[i][2]}\t{Database[i][3]}\t{Database[i][4]}\t{Database[i][5]}")
            
#     elif choice == 5:
#         print("Exiting...")
#         break
