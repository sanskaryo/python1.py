##class Shape:
##    pass
##class Circle(Shape):
##    def __init__(self):
##        self.radius=int(input("Enter the Radius of Circle "))
##    def Area(self):
##        return print(3.14*self.radius**2)
##    def Perimeter(self):
##        return print(2*3.14*self.radius)
##
##class Rectangle(Shape):
##    def __init__(self):
##        self.length=int(input("Enter the length "))
##        self.breadth=int(input("Enter the Breadth "))
##    def Area(self):
##        return print(self.length*self.breadth)
##    def Perimeter(self):
##        return print(2*(self.length+self.breadth))
##
##class Square(Shape):
##    def __init__(self):
##        self.side=int(input("Enter the Side of Square "))
##    def Area(self):
##        return print(self.side*self.side)
##    def Perimeter(self):
##        return print(4*self.side)
##
##obj1=Circle()
##obj2=Square()
##obj3=Rectangle()
##ch=input("1.Area 2.Perimeter")
##if ch==1:
##    obj1.Area()
##    obj2.Area()
##    obj3.Area()
##else:
##    obj1.Perimeter()
##    obj2.Perimeter()
##    obj3.Perimeter()