class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.Radius = float(input("Enter Radius: "))

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print("Radius :", self.Radius)
        print("Area :", self.Area)
        print("Circumference :", self.Circumference)

    @classmethod
    def CreateObject(cls):
        obj = cls()
        obj.Accept()
        obj.CalculateArea()
        obj.CalculateCircumference()
        obj.Display()
        print()
        return obj



obj1 = Circle.CreateObject()
obj2 = Circle.CreateObject()
obj3 = Circle.CreateObject()
obj4 = Circle.CreateObject()
obj5 = Circle.CreateObject()