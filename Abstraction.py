# Abstraction example:-

from abc import ABC,abstractmethod
class Car(ABC):
    @abstractmethod
    def mileage(self):
        pass
    def color(self):
        print("Gray")

class TATA(Car):
    def mileage(self):
        print("milage is 30kmph")

class Maruti_Suzuki(Car):
    def mileage(self):
        print("mileage is 35lmph")

obj1=TATA()
obj1.mileage()
obj2=Maruti_Suzuki()
obj2.mileage()
