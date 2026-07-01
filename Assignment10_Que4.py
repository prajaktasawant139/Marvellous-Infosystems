# Q4. Write a python program which accepts one number and prints all even numbers till that number.

def PrintEven(No):

    for i in range(2, No + 1, 2):
        print(i)


def main():
    Value = int(input("Enter number : "))

    PrintEven(Value)


if __name__ == "__main__":
    main()