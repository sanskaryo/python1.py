# car dealership

class Car:
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.is_sold = False

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}, Price: ${self.price}, Status: {'Sold' if self.is_sold else 'Available'}")


class Dealership:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def add_car(self, car):
        self.inventory.append(car)

    def display_inventory(self):
        print(f"Inventory of {self.name} Dealership:")
        for car in self.inventory:
            car.display_info()

    def sell_car(self, make, model, year):
        for car in self.inventory:
            if car.make == make and car.model == model and car.year == year and not car.is_sold:
                car.is_sold = True
                print(f"Sold: {year} {make} {model} from {self.name} Dealership")
                return
        print(f"Car not found or already sold: {year} {make} {model}")


# Example usage:
car1 = Car("Toyota", "Camry", 2022, 25000)
car2 = Car("Honda", "Accord", 2021, 28000)

dealership = Dealership("Best Cars")

dealership.add_car(car1)
dealership.add_car(car2)

dealership.display_inventory()

dealership.sell_car("Toyota", "Camry", 2022)

dealership.display_inventory()
