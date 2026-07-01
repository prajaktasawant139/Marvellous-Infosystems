# Q2. Write a python program which accepts one number and prints sum of first N natural numbers.

def SumNatural(No):

    Sum = 0

    for i in range(1, No + 1):
        Sum = Sum + i

    return Sum


def main():
    Value = int(input("Enter number : "))

    Ret = SumNatural(Value)

    print("Sum of first", Value, "natural numbers is :", Ret)


if __name__ == "__main__":
    main()