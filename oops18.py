# Method Overloading:-

class Area:
    def area(self,l=0,b=0):
        if l>0 and b>0:
            print("Area of rectangle:",l*b)
        elif l>0 and b==0:
            print("Area of square:",l*l)

a=Area()
a.area(10)
a.area(10,20)