# Static method

class Bank():
    bank_name="SBI"
    rate_of_intrest=12.5
    @staticmethod
    def simple_intrest(principle,num_ofyear):
        si=(principle*num_ofyear*Bank.rate_of_intrest)/100
        print(f"simple interest: {si}")

principle=float(input("Enter principle amount: "))
num_ofyear=int(input("Enter number of year: "))
Bank.simple_intrest(principle,num_ofyear)