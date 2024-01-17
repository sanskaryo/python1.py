# escape_string = "Hello""world" 
# print(escape_string)
















































patient = {}
while True:
    cho = int(input("Patient Database Menu:\n1. Add new patient\n2. Retrieve patient information\n3. Update patient medical history\n4. Display all patients\n5. Exit\nEnter your choice (1-5): "))
    if cho == 1:
        name = input("\nEnter Patient Name: ")
        id = int(input("Enter Patient ID: "))
        age = int(input("Enter Age of the Patient: "))
        gender = input("Enter patient's gender: ")
        number = int(input("Enter contact number of the patient: "))
        history = input("Enter Medical History of the patient: ")
        patient[id] = [name, age, gender, number, history]
        print("Patient added successfully\n")
    elif cho == 2:
        ask = int(input("Enter patient id: "))
        if ask in patient:
            details = patient[ask]
            print(f"Name: {details[0]}\nPatient ID: {ask}\nAge: {details[1]}\nGender: {details[2]}\nNumber: {details[3]}\nHistory: {details[4]}\n")
        else:
            print("Patient not found")
    elif cho == 3:
        print("Update Details Menu:")
        ask = int(input("Enter patient id to update details: "))
        if ask in patient:
            history = input("Enter Updated Medical History of the patient: ")
            details = patient[ask]
            details[4] = history
            print(f"Medical history updated for patient ID [{ask}].")
        else:
            print("Patient not found")
    elif cho == 4:
        print("All Patients Details:\n")
        for i in patient:
            details = patient[i]
            print(f"Name: {details[0]}\nPatient ID: {i}\nAge: {details[1]}\nGender: {details[2]}\nNumber: {details[3]}\nHistory: {details[4]}\n")
    elif cho == 5:
        print("Exiting the Program")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
