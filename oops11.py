# Constructor in inheritance

    # (i) super() method/super() function

class Computer():
    def __init__(self,ram,rom):
        self.ram=ram
        self.rom=rom
        print("Accessing the computer class.")

class Mobile(Computer):
    def __init__(self,ram,rom,phone):
        super().__init__(ram,rom)   # Using super method
        self.phone=phone
        print("Accessing mobile class.")

google=Mobile('12gb','256gb','Google pixel9')
print(google.__dict__)


    # (ii) class method

class Computer():
    def __init__(self,ram,rom):
        self.ram=ram
        self.rom=rom
        print("Accessing computer class.")

class Mobile(Computer):
    def __init__(self,ram,rom,phone):
        Computer.__init__(self,ram,rom)  # Using class method
        self.phone=phone
        print("Accessing mobile class.")

google=Mobile('12gb','256gb','Google pixel9')
print(google.__dict__)