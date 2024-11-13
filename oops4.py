# Built in class functions

class Emp():
    def __init__(self,name,age):
        self.name=name
        self.age=age
e1=Emp('Abhi',22)
e2=Emp('Priya',21)

print(getattr(e1,'name'))
setattr(e2,'name','jeevan')
print(e2.__dict__)
delattr(e2,'age')
print(e2.__dict__)
print(hasattr(e1,'age'))
