# polymorphism with inheritance:-

class Veh:
    def __init__(self,name,color,price):
        self.name=name
        self.color=color
        self.price=price

    def get_details(self):
        print("Name is :",self.name)
        print("Color is :",self.color)
        print("Price is :",self.price)

    def max_speed(self):
        print("Max speed limit is 100")

    def gear(self):
        print("Gear changes is 6")

class Car(Veh):
    def max_speed(self):
        print("Max speed limit is 140")

    def gear(self):
        print("Gear change is 5")

v1=Veh("Truck","Blue",5000000)
c1=Car("Nexon","Matblack",120000)
v1.get_details()
c1.get_details()
v1.max_speed()
c1.max_speed()
v1.gear()
c1.gear()
