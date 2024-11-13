# Constructor
   #(i)Parameterized constructor:-

class Company():
    def __init__(self,ename,esal,eage):
        self.ename=ename
        self.esal=esal
        self.eage=eage

emp1=Company('Abhisek',2500000,23)
emp2=Company('Ram',3000000,24)
print(emp1.ename,emp1.esal,emp1.eage)
print(emp2.ename,emp2.esal,emp2.eage)


   #(ii)Non-parameterized constructor:-

class Company():
    def __init__(self):
        print('All emp are executed')
    
emp1=Company()
emp2=Company()