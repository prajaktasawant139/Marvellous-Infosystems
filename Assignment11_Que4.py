# Q4. Write a python program which accepts one number and prints reverse of that number.

def Reverse(No):

    Rev = ""

    for Digit in str(No):
        Rev = Digit + Rev

    return Rev


def main():
    Value = int(input("Enter number : "))

    Ret = Reverse(Value)

    print("Reverse number is :", Ret)


if __name__ == "__main__":
    main()