


thisdict = {
 "brand": "Ford",
 "model": "Mustang",
 "year": 1964
}
for x in thisdict:
 print(x)
print()
for x in thisdict:
 print(thisdict[x])
print()
for x in thisdict.values():
  
 print(x)
print()
for x in thisdict.keys():
 print(x)
print()
for x, y in thisdict.items():
 print(x, y)
print()































# # List of patients
# patients = [
# {'name': 'John', 'amount_to_pay': 500, 'disease': 'Flu'},
# {'name': 'Jane', 'amount_to_pay': 1000, 'disease': 'Fever'},
# {'name': 'Tom', 'amount_to_pay': 800, 'disease': 'Flu'},
# {'name': 'Emily', 'amount_to_pay': 1200, 'disease': 'Covid'},
# {'name': 'Sam', 'amount_to_pay': 1500, 'disease': 'Covid'},
# {'name': 'Alex', 'amount_to_pay': 700, 'disease': 'Fever'},
# {'name': 'Sarah', 'amount_to_pay': 900, 'disease': 'Flu'},
# {'name': 'Michael', 'amount_to_pay': 1100, 'disease': 'Covid'},
# {'name': 'Jessica', 'amount_to_pay': 600, 'disease': 'Fever'}
# ]
# # Task 1: Calculate the total amount to be paid by all patients
# total_amount_to_pay = 0
# for patient in patients:
#    total_amount_to_pay += patient['amount_to_pay']


# # Task 2: Find the patient with the highest amount to be paid
# highest_amount_patient = 0
# highest_amount = -1
# for patient in patients:
#    if patient['amount_to_pay'] > highest_amount:
#       highest_amount = patient['amount_to_pay']
#       highest_amount_patient = patient


# # Task 3: Identify the patients suffering from a specific disease
# specific_disease = 'Covid'
# patients_with_specific_disease = []
# for patient in patients:
#    if patient['disease'] == specific_disease:
#       patients_with_specific_disease.append(patient)


# # Printing results
# print("Total amount to be paid by all patients:", total_amount_to_pay)
# print(f"\nPatient with the highest amount to be paid: {highest_amount_patient['name']} (Amount: {highest_amount_patient['amount_to_pay']})")
# print(f"\nPatients suffering from {specific_disease}:")
# for patient in patients_with_specific_disease:
#       print(f"Name: {patient['name']}, Amount to be paid: {patient['amount_to_pay']}")

