# Class method

class Emp():
    comp_name="AS Tech"
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal

    @classmethod
    def get_company_name(cls):
        print(cls.comp_name)

e1=Emp('Jay',3000000)
e2=Emp('Abhisek',45000000)

Emp.get_company_name()
print(e2.comp_name)