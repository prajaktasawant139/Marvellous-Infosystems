class Arithmetic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter first number : "))
        self.Value2 = int(input("Enter second number : "))
        
    def Addition(self):
        return self.Value1 + self.Value2
    
    def Substraction(self):
        return self.Value1 - self.Value2
    
    def Multiplication(self):
         return self.Value1 * self.Value2
         

    def Division(self):
        if self.Value2 == 0:
            return "Division by zero is not possible"
        return self.Value1 / self.Value2
        



obj1 = Arithmetic()

print("first object")

obj1.Accept()
print("Addition =", obj1.Addition())
print("Substraction =", obj1.Substraction())
print("Multiplication =", obj1.Multiplication())
print("Division =", obj1.Division())


obj2 = Arithmetic()

print("second object")
obj2.Accept()
print("Addition =", obj2.Addition())
print("Substraction =", obj2.Substraction())
print("Multiplication =", obj2.Multiplication())
print("Division =", obj2.Division())