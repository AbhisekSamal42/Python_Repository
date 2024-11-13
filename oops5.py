# Built in attributes

class Emp():
    '''This is storing the emp details.'''
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def display(self):
        print(f"My name is {self.name} and my age is {self.age}.")

e1=Emp('Abhisek',22)

# print(e1.age)
# print(e1.name)
# e1.age=21
# print(e1.age)
# e1.display()

print(Emp.__doc__)
print(Emp.__name__)
print(Emp.__dict__)
print(Emp.__module__)