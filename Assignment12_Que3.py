# Q3. Write a python program which accepts two numbers and prints addition, subtraction, multiplication and division

def Arithmetic(No1, No2):

    Add = No1 + No2
    Sub = No1 - No2
    Mul = No1 * No2
    Div = No1 / No2

    print("Addition is :", Add)
    print("Subtraction is :", Sub)
    print("Multiplication is :", Mul)
    print("Division is :", Div)


def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    Arithmetic(Value1, Value2)


if __name__ == "__main__":
    main()