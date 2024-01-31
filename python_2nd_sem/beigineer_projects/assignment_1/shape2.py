class shape:
    def __init__(self,length,breadth):
        self.length = l
        self.breadth = b
        
    def area(self):
        return self.length*self.breadth
    
    def perimeter(self):
        return  2*(self.length+self.breadth)

class Rectangle(shape):
    def __init__(self,length,breadth):
        super().__init__(length,breadth)
        
        
class square(shape):
    def __init__(self,side):
        super().__init__(side,side)
    
    
l = int(input("enter the length : "))
b = int(input("enter the breadth : "))
rec = Rectangle(l,b)
area = rec.area()
peri = rec.perimeter()

print(f'area of rectangle is {area}')
print(f'perimeter of rectangle is {peri}')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#     class Shape: 
# def area(self): 
# pass
# class Rectangle(Shape): 
# def __init__(self, length, width): 
# self.length = length
# self.width = width
# def area(self): 
# return self.length * self.width
# class Circle(Shape): 
# def __init__(self, radius): 
# self.radius = radius
# def area(self): 
# return 3.14 * self.radius ** 2
# # Test the classes 
# rectangle = Rectangle(5, 10) 
# circle = Circle(7) 
# print(f"Rectangle Area: {rectangle.area()}") 
# print(f"Circle Area: {circle.area()}") 
