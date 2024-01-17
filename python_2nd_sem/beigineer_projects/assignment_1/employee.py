class Employee:
    def __init__(self, name, employee_id, hourly_rate):
        self.name = name
        self.employee_id = employee_id
        self.hourly_rate = hourly_rate
        self.hours_worked = 0

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

# Example usage
employee1 = Employee("Ravi", 456, 500)
employee1.hours_worked = 70
salary = employee1.calculate_salary()
print(salary)  # Output: 800
