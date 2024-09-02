class ourBank:
    nob=1
    ifsc='OBI000420'
    roi=8
    def __init__(self,Name,Mobno,Aadhar,Bal,Pin):
        self.Name = Name
        self.Mobno = Mobno
        self.Aadhar = Aadhar
        self.Bal = Bal
        self.Pin = Pin
    def checkBalance(self):
        if self.Pin == self.takePin():
            print(f'Available balance is{self.Bal}')
        else:
            print('Invalid Pin')
    def deposite(self):
        if self.Pin == self.takePin():
            amount = int(input('Enter amount to deposite: '))
            self.Bal += amount
            print('Amount credited successfully...')
            print(f'Available balance is{self.Bal}')
        else:
            print('Invalid Pin')
    @classmethod
    def croi(cls):
        newv = float(input('Enter new roi: '))
        cls.roi = newv
    def withdraw(self):
        if self.Pin == self.takePin():
            amount = int(input('Enter amount to withdraw: '))
            if amount <= self.Bal:
                self.Bal-= amount
                print('Amount debited successfully...')
                print(f'Available balance is{self.Bal}')
            else:
                print('Insufficient balance...')
        else:
            print('Invalid Pin')
    @staticmethod
    def takePin():
        password = int(input('Enter the pin: '))
        return password
us1 = ourBank('Ambani',9853141418,11111111111,2000000,1111)
us2 = ourBank('Tata',8908966030,22222222222,5000000,9999)
us1.withdraw()
print('-'*10)
us2.deposite()