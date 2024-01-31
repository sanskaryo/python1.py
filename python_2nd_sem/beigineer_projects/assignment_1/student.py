class Student:
    def __init__(self):
        self.name = 'NA'
        self.age = 'NA'
        self.percentage = 'NA'

    def setdetail(self, name, age, percentage):
        self.name = name
        self.age = age
        self.percentage = percentage

    def calculate_grade(self):
        if self.percentage >= 90:
            return 'O'
        elif self.percentage >= 80:
            return 'A'
        elif self.percentage >= 70:
            return 'B'
        elif self.percentage >= 60:
            return 'C'
        else:
            return 'D'

    def getdetail(self):
        return f"Name: {self.name}, Age: {self.age}, Percentage: {self.percentage}"

    def display_details(self):
        grade = self.calculate_grade()
        print(f"Name: {self.name}, Age: {self.age}, Grade: {grade}")

# main
student1 = Student()
student1.setdetail("Sanskar", 20, 95)
student1.display_details()
