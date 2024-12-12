# Operator overloading in Polymorphism:-

class Book:
    def __init__(self,title,pages):
        self.title=title
        self.pages=pages

    def __add__(self,others):
        total=self.pages+others.pages
        return Book("allbooks",total)
    
    def __str__(self):
        return str(self.pages)
    
b1=Book("Iron leady of india",500)
b2=Book("Mk gandhi",600)
b3=Book("Freedom at midnight",700)
print("total number of pages:",b1+b2+b3)