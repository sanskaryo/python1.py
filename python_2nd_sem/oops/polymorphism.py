# overloading ... oversetting


class SK:
    def displayinfo(self):
        print("hello duniya by sk")

class IIP(SK):
    def displayinfo(self):
        super().displayinfo()  # we are able to caall the parent by using super function ,, ... over riding
        print("hello duniya by iip")
        
obj=IIP()
obj.displayinfo()  