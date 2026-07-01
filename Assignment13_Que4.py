# Q4. Write a python program which accepts one number and prints binary equivalent.

def Binary(No):

    print("Binary equivalent is :", bin(No)[2:])


def main():
    Value = int(input("Enter number : "))

    Binary(Value)


if __name__ == "__main__":
    main()