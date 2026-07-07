# Q6. Write a program which accept number from user and check whether that number is positive or negative or zero.

def ChkNum(No):
    if No > 0 :
        print("Number is Positive")

    elif No < 0 :
        print("Number is Negative")

    else:
        print("Number is Zero")

def main():
    Value = int(input("Enter a number : "))

    ChkNum(Value)

if __name__ == "__main__":
    main()