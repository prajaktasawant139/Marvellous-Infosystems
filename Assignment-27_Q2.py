class BankAccount:
    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("Account Holder Name :", self.Name)
        print("Current Balance :", self.Amount)

    def Deposit(self):
        Amt = float(input("Enter amount to deposit : "))
        self.Amount = self.Amount + Amt
        print("Amount deposited successfully.")

    def Withdraw(self):
        Amt = float(input("Enter amount to withdraw : "))
        if Amt <= self.Amount:
            self.Amount = self.Amount - Amt
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest


obj1 = BankAccount("Prajakta Sawant", 15000)
obj2 = BankAccount("Supriya Roy", 10000)


obj1.Display()
obj1.Deposit()
obj1.Withdraw()
obj1.Display()
print("Interest :", obj1.CalculateInterest())


obj2.Display()
obj2.Deposit()
obj2.Withdraw()
obj2.Display()
print("Interest :", obj2.CalculateInterest())

