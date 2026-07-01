# Q2. Write a program which accepts one number and prints count of digits in that number.

def CountDigits(No):

    Count = 0

    for i in str(No):
        Count = Count + 1

    return Count


def main():
    Value = int(input("Enter number : "))

    Ret = CountDigits(Value)

    print("Number of digits is :", Ret)


if __name__ == "__main__":
    main()