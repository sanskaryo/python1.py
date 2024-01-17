print("****Car Dealership****")


class cars:
    
    def __init__(self,name,model,year,company,price,available):
        self.name = name
        self.model = model
        self.year = year
        self.company = company
        self.price = price
        self.available = True
    def display_car(self):
        return f'''company: {self.company}
Car Name: {self.name}
Model: {self.model}
Year: {self.year}
Price: {self.price}'''

class dealership:
    def __init__(self,name) -> None:
        self.name = name  
        self.inventory = []
        
        
    def add_car_to_inventory(self,car):
        self.inventory.append(car)
        
        
    def display_available_car(self):
        count = 1
        for car in self.inventory:
            if car.available:
                print(f'\nCar : {count}')
                print(car.display_car())
                count += 1
                
    def sell_car(self, customer, index):
        if 0 < index <= len(self.inventory) and self.inventory[index-1].available:
            customer.purchase(self.inventory[index-1])
            return self.inventory[index-1]  # Return the sold car
        return None
                
                
                
    
    class customer :
        def __init__(self,name) -> None:
            self.name = name
            self.purchased_car = []
        def purchase(self,car):
            self.purchased_car.append(car)
            car.available = False
        
 # main code   
        
car1 = cars("BMW", "X5", 2019, "BMW", 15000000)
car2 = cars("Tesla", "Model 3", 2019, "Tesla", 900000)
car3 = cars("hector", "Model S", 2019, "MG", 100000)


d1 = dealership('Hero Dealers')
d1.add_car_to_inventory(car1)
d1.add_car_to_inventory(car2)
d1.add_car_to_inventory(car3)

d1.display_available_car()

cname = input("Enter your name: ")
Carnum = int(input(f"Enter the number of car you want to buy: [1-{len(d1.inventory)}] "))
c1 = c(cname)  # Create a customer instance
ret = d1.sell_car(c1, Carnum)

if ret:
    print(f"{c1.name} has purchased {ret.display_car()}")
else:
    print("Car is not available")

print("\nAfter selling available car")
d1.display_available_car() 
    

