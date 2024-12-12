# polymorphism in function and objects:-

class Bmw:
    def fuel_type(self):
        print("Diesel")
    def max_speed(self):
        print("max speed is 180")

class Ferrari:
    def fuel_type(self):
        print("Petrol")
    def max_speed(self):
        print("Max speed is 200")

def car_details(car):
    car.fuel_type()
    car.max_speed()

B1=Bmw()
F1=Ferrari()
car_details(B1)
print("___________________")
car_details(F1)
