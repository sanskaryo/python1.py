class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_details(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

    def calculate_grade(self, percentage):
        if percentage >= 90:
            return 'A'
        elif percentage >= 80:
            return 'B'
        elif percentage >= 70:
            return 'C'
        elif percentage >= 60:
            return 'D'
        else:
            return 'F'

student1 = Student("Sanskar", 20, "Sophomore")
student2 = Student("Shiv kumar", 19, "Sophomore")


print(student1.display_details())
print(student2.display_details())

print(student1.calculate_grade(85))
print(student2.calculate_grade(92))
