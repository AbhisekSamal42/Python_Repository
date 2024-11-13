# Instace method / Object method

class Student():

    def __init__(self,name,mark):
        self.name=name
        self.mark=mark

    def display(self):
        print(self.name,self.mark)

std1=Student('Abhisek',80)
std2=Student('Ram',85)
std1.age=22
print(std1.__dict__)
std1.display()
std2.display()