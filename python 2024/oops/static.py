# tatic methods in Python are methods that belong to a class rather than an instance of the class. They are defined using the @staticmethod decorator and do not have access to the instance of the class (i.e. self). They are called on the class itself, not on an instance of the class. Static methods are often used to create utility functions that don't need access to instance data.

# STATIC likh diya to self likhne ki jarurat nhi h 


class Math:
    @staticmethod
    def add(a, b):
        return a + b
result = Math.add(1, 2)
print(result) # Output: 3


