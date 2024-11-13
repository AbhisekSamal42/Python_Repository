# Accessing class member outside the class.

class Company():
    def __init__(self,sal,age):
        self.sal=sal
        self.age=age

    def display(self):
        print(f"Salary is {self.sal} and age is {self.age}.")

emp1=Company(240000,21)
emp2=Company(300000,22)

# Accessing attribute outside the class.
print(emp1.sal) # output is 240000
emp1.sal=350000 # updating the value 
print(emp1.sal) # output is 350000
print(emp2.age) # output is 22

emp1.display()
emp2.display()