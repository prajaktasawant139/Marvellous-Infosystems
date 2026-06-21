#Assignment3-Q6. Write a program to display:Data type,Memory address,Size in bytes of a variable entered by the user.

x = input("Enter a value: ")

print("Data Type is :", type(x))
print("Memory Address is :", id(x))
print("Size in Bytes is :", x.__sizeof__())


