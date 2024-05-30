class Employee:
    company = "Google"
    def show(self):
        print(f"the name is {self.name} and company name is {self.company}")
        
        
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company
        
    
e1 = Employee()
e1.name = "John"
e1.change_company("Goldman Sachs")
e1.show() # Output: the name is John and company name is Goldman Sachs  
print(Employee.company) # Output: Goldman Sachs