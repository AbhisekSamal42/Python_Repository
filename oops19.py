# Nested class:-

class Student:
    def __init__(self, name, rollno, date, month, year):
        self.name = name
        self.rollno = rollno
        self.dob = self.Dob(date, month, year)

    def display(self):
        print(f"Name is {self.name} and rollno is {self.rollno}.")
        self.dob.display()  # Corrected method call

    class Dob:  # Made Dob a nested class
        def __init__(self, date, month, year):
            self.date = date
            self.month = month
            self.year = year

        def display(self):
            print(f"Date of birth is: {self.date}/{self.month}/{self.year}")


# Create an instance of the Student class
s1 = Student("Abhisek Samal", 101, 18, 8, 2002)
s1.display()
