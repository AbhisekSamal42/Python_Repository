# Getter and Setter method

class Emp():

    def setname(self,name):
        self.name=name

    def getname(self):
        print(self.name)

e1=Emp()
e2=Emp()
e1.setname('Abhbisek')
e2.setname('Ram')
print(e1.__dict__)
print(e2.__dict__)
e2.getname()
e1.getname()