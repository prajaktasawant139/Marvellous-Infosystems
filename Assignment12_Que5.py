# Q5. Write a python program which accepts one number and prints that many numbers in reverse order.

def Display(No):

    for i in range(No, 0, -1):
        print(i)


def main():
    Value = int(input("Enter number : "))

    Display(Value)


if __name__ == "__main__":
    main()