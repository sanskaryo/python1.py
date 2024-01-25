class Car:
    def __init__(self, model, color, rental_price_per_day):
        self.model = model
        self.color = color
        self.rental_price_per_day = rental_price_per_day
        self.available = True

    def calculate_rental_charges(self, num_days):
        return num_days * self.rental_price_per_day

    def rent_car(self):
        self.available = False

    def return_car(self):
        self.available = True

# Example Usage:
car1 = Car("Honda Accord", "Blue", 50)
charges = car1.calculate_rental_charges(3)
print("Rental charges:", charges)


# Approach:
# The Car Rental System involves a Car class. This class has an __init__ method to initialize attributes for model and color. Additionally, there's a calculate_rental_charges method that takes the number of days as input and calculates the rental charges based on a simple assumption.

# Approach:
# For the ToDo List, I created a ToDo class that manages tasks. The class has an __init__ method to initialize an empty list for tasks. The methods include add_task to add tasks to the list, mark_completed to remove completed tasks, and display_tasks to print the list of tasks.