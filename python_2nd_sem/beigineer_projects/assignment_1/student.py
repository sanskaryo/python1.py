class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
    
    def display_details(self):
        print(f"Name: {self.name}, Roll Number: {self.roll_number}")
# Example usage
student1 = Student("Sanskar", 44)
student1.display_details()
# Brief Description:
# I've implemented a Student class with attributes for name and roll number. The class has a method to display student details.
