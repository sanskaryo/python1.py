class Person :
    Name = "Sanskar"
    occup = "ML Dev"
    
    def info(self):
        print(f"{self.Name} is a {self.occup}")
        
a = Person()
# print(a.Name)
a.Name = "ojasvi"
a.occup = "H.R."
a.info()