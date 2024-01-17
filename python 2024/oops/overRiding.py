# child ka parent ko inherit , good for memory reduction , having same name , same argument


class A:
    def Showdata(self):
        print("hello duniya A")
        
class B(A):
    def Showdata(self):
        print("hello duniya B")
        
        
obj = B()
obj.Showdata()   # jab inherit kiya to vo over ride hogaya
    