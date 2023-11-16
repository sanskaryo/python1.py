students={
    "John": 85,
    "Jane": 90,
    "Bob" : 75,
    "Alice" : 95,
    }

students["Bob"]=80

students["Sam"] = 80

students.pop("Jane")

for student,score in students.items():
    print(f"{student} : {score}")