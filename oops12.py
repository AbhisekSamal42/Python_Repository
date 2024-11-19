# Inheritance

  #(i) Single inheritance(Inheriting properties from one Parent class to one child class.)

class Computer():
    def __init__(self):
        self.ram='8gb'
        self.rom='128gb'

class Mobile(Computer):
    def __init__(self):
        super().__init__()
        self.phone='mi note7 pro'

mob=Mobile()
print(mob.__dict__)


  # (ii) Multi_level inheritance(Inheriting properties from one child class to another child class)

class Company():
    def __init__(self):
        self.comp_name="AS Tech"
        print("Accessing company class.")

class Emp(Company):
    def __init__(self):
        super().__init__()
        self.sal=500000
        print("Accessing emp class.")

class Mgr(Emp):
    def __init__(self):
        super().__init__()
        self.bonus=10000
        print("Accessing in mgr class.")

obj=Mgr()
print(obj.__dict__)

    # Object/instance in multi_level inheritance

class A():
    var1=200
class B(A):
    var2=400
class C(B):
    var3=600
obj=C()
print(obj.var1,obj.var2,obj.var3)

   # (iii) Multiple inheritance

class Country():
    def __init__(self):
        print("Country class constructor")
        self.office='Delhi'

class State():
    def __init__(self):
        super().__init__()
        print("State class constructor")
        self.office='Odisha'

class Dist(State,Country):
    def __init__(self):
        super().__init__()
        print("Dist class constructor")
        self.office='Jajpur'

obj=Dist()
print(obj.__dict__)


    # (iv) Hierarchical inheritance

class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display1(self):
        print("Displaying person class method")

class Emp(Person):
    def __init__(self,name,age,sal):
        super().__init__(name,age)
        self.sal=sal

    def display2(self):
        print("Displaying emp class method")

class Student(Person):
    def __init__(self,name,age,mark):
        super().__init__(name,age)
        self.mark=mark
    
    def dispaly3(self):
        print("Displaying student class method")


s1=Student("Abhisek",21,87)
e1=Emp('RAM',25,400000)
p1=Person("raj",30)

s1.dispaly3()
s1.display1()
#s1.dispaly2() # error(because one child class can not access another child class propeties)

print(s1.__dict__)
print(e1.__dict__)


    #(v) Hybrid inheritance

class A():
    var=10
class B():
    var1=20
class C():
    var2=30
class D(B,C):
    pass
obj=D()
print(obj.var1)