# Q3. Write a python program which accepts one number and prints factorial of that number.

def Factorial(No):

    Fact = 1

    for i in range(1, No + 1):
        Fact = Fact * i

    return Fact


def main():
    Value = int(input("Enter number : "))

    Ret = Factorial(Value)

    print("Factorial is :", Ret)


if __name__ == "__main__":
    main()