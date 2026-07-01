#Q3.Write a program python which accepts one number and prints square of that number

def Square(No):

    return No * No


def main():
    Value = int(input("Enter number : "))

    Ret = Square(Value)

    print("Square is :", Ret)


if __name__ == "__main__":
    main()