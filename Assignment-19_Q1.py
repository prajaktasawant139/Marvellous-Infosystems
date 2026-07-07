# Q1. Write a program which contains one lambda function which accepts one parameter and return power of two.

Power = lambda No : No ** 2

def main():
    Value = int(input("Enter number : "))

    Ret = Power(Value)

    print("Power of two is :", Ret)

if __name__ == "__main__":
    main()