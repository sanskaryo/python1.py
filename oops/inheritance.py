class A:
    def displayA(self):
        print("hello duniya A")

class B(A):
    def displayB(self):
        print("hello duniya B")
        
obj=B()
obj.displayA()
obj.displayB()