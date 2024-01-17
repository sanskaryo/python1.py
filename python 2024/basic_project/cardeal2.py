class car:
    def _init_(self, brand, name, model, year, price):
        self.brand = brand
        self.name = name
        self.model = model
        self.year = year
        self.price = price
        self.available = True
        
    def display_car(self):
        return f'''Brand : {self.brand}
Car Name : {self.name}
Model : {self.model}
Year : {self.year}
Price : {self.price}\n'''


class dealership:
    def _init_(self, dealer_name):
        self.dealer_name = dealer_name
        self.inventory = []
    def add_car_to_inventory(self,car):
        self.inventory.append(car)
    def display_available_car(self):
        count = 1
        for car in self.inventory:
            if car.available:
                print(f'\nCar : {count}')
                print(car.display_car())
                print('-'*139)
                count += 1
    def sell_car(self, customer1, index):
        if 0 < index < len(self.inventory) and self.inventory[index-1].available:
            customer1.purchase(self.inventory[index-1])
            return self.inventory[index-1]
        
class customer:
    def _init_(self, cus_name):
        self.cus_name = cus_name
        self.purchased_car = []
    
    def purchase(self, car):
        self.purchased_car.append(car)
        car.available = False
        
#main-code
car1 = car('Porshe', 'Porshe 911', 'V8', '2024', '95000000')
car2 = car('Toyota', 'Fortuner', 'Legender', '2024', '6000000')
car3 = car('Land Rover', 'Defender', 'O', '2023', '15000000')
car4 = car('Mahindra', 'Scorpio', 'Classic', '2024', '2000000')


d1 = dealership('Fusion Cars')
d1.add_car_to_inventory(car1)
d1.add_car_to_inventory(car2)
d1.add_car_to_inventory(car3)
d1.add_car_to_inventory(car4)

d1.display_available_car()

c1 = customer('Sunny')
ret = d1.sell_car(c1, 2)
if ret:
    print(f'\n{c1.cus_name} Purchased \n{ret.display_car()}\n')
print('\n After Selling, Display Available Cars : \n')
d1.display_available_car()