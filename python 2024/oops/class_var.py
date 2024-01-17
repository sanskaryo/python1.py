# lass Variables
# Class variables are defined at the class level and are shared among all instances of the class. They are defined outside of any method and are usually used to store information that is common to all instances of the class. For example, a class variable can be used to store the number of instances of a class that have been created.


# Explain
class MyClass:
    class_variable = 0
    
    def __init__(self):
        MyClass.class_variable += 1
        
    def print_class_variable(self):
        print(MyClass.class_variable)
        
obj1 = MyClass()
obj2 = MyClass()
obj1.print_class_variable() # Output: 2
obj2.print_class_variable() # Output: 2