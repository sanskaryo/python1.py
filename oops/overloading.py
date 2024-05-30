
#function overloading ... same function different parameter

class Area:
    def findArea(self,X=None,Y=None):
        
        if X!=None and Y!=None:
            print(X*Y) 
        elif X!=None:
            print(X*X)
        else:
            print("nothing")

obj1=Area()
obj1.findArea()
obj1.findArea(5)
obj1.findArea(5,6)

