# Access modifier
  #(i) Public access modifier
class Finance:
    def __init__(self):
        self.revenue=1000000
        self.number_of_sales=114

class Hr:
    def __init__(self):
        self.number_of_emp=30

h1=Hr()
f1=Finance()
print(f1.__dict__)

#(ii) protected access modifier

class Access:
    def __init__(self):
        self._a=420

    def m1(self):
        print(self._a)

obj=Access()
obj.m1()
print(obj._a)

#(iii) Private access modifier

class Finance():
    def __init__(self):
        self.__revenue=1000000
        self.__sale=111

    def display(self):
        print(f"Revenue is {self.__revenue} and number of sales {self.__sale}")

f1=Finance()
f1.display()