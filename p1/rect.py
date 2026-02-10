class rectangle:
    def area(self,a,b):
        return a*b
    def peri(self,a,b):
        return 2*(a+b)
r=rectangle()
print("area:",r.area(2,4))
print("peri:",r.peri(2,4))