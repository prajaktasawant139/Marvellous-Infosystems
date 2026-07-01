# Q1. Write a python program which accepts one number and prints multiplication table of that number.

def MultiplicationTable(No):

    for i in range(1, 11):
        print(No, "x", i, "=", No * i)


def main():
    Value = int(input("Enter number : "))

    MultiplicationTable(Value)


if __name__ == "__main__":
    main()
