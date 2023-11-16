
student_grades = {'Rahim': 92, 'Ram': 85, 'Dhananjay': 95, 'Ron': 95, 'Ravinder': 78}

print(student_grades)

highest_grade = -1

for grade in student_grades.values():
    if grade > highest_grade:
        highest_grade = grade

topper_student = [student for student, grade in student_grades.items() if grade == highest_grade]

print(f"The highest students are {topper_student}")
