#bike stor system by oops class obj
print(" **** Bike REntal System ****")
class BikeStore:
    def __init__(self,stock):
        self.stock=stock
    def displayBike(self):
        print("total Bikes",self.stock)
    def rentForBike(self,q):
        
        if q<=0:
            print("invalid quantity")
        elif q>self.stock:
            print("enter value less than the available stock")
        
        else:
            self.stock=self.stock-q
            print("total cost",q*150)
            print("total bikes", self.stock) 
        
    
while True:
    obj=BikeStore(150)
    distock = int(input('''
                        
                        1. display stock
                        
                        2. rent a bike
                        
                        3. Exit
                        
                        
                        '''))
    
    if distock==1:
        obj.displayBike()
    elif distock ==2:
        n = int(input("enter the quantity == "))
        
        obj.rentForBike(n)
    else:
        break
