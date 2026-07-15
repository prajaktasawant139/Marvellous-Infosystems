class Demo:
   Value = 10

   def __init__(self,No1,No2):
      self.No1 = No1
      self.No2 = No2

   def fun(self):
      print("Inside fun")
      print("No1 =", self.No1)
      print("No2 =", self.No2)

   def gun(self):
      print("Inside gun")
      print("No1 =", self.No1)
      print("No2 =", self.No2)

obj1 = Demo(11,21)
obj2 = Demo(51,101)

obj1.fun()

obj2.fun()
obj1.gun()
obj2.gun()





