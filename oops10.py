# Inheritance

class Emp():
    bonus=20000
    def display(self):
        print("This is emp. class method")

class Mgr(Emp):
    bonus1=30000
    def show(self):
        print("This is mgr. class method")

e1=Emp()
m1=Mgr()


print(m1.bonus)
print(m1.display)
print(m1.__dict__)