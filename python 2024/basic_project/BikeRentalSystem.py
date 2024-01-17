# diplay available bikes , request bike for rent == 1 bike 150 rs , exit

print("****Bike Rental System****")

class bikeShop:
    
    def __init__(self,name,address):
        self.name = name
        self.address = address
        self.bikes = []

    def displayBikes(self):
        print("Available bikes are :")
        for bike in self.bikes:
            print(bike)

    def requestBike(self):
        bike = input("Enter bike name : ")
        self.bikes.append(bike)
        print("Bike rented successfully")

    def exit(self):
        print("Thank you for using our service")

