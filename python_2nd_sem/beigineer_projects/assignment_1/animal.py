class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Species: {self.species}, Age: {self.age}"
    
    
animal1 = Animal("lion","panther",5)
print(animal1.display_info())














# class Lion(Animal):
#     def roar(self):
#         return "Roar!"

# class Elephant(Animal):
#     def trumpet(self):
#         return "Trumpet!"
    
# class Horse(Animal):
#     def neigh(self):
#         return "Neigh !"

# class Giraffe(Animal):
#     def munch(self):
#         return "Munch, munch!"
