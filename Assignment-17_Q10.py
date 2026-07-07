# Q10. Write a program which accept number from user and return addition of digits in that number.

def SumDigits(No):
    Sum = 0

    for digit in str(No):
        Sum = Sum + int(digit)

    return Sum

def main():
    Value = int(input("Enter a number: "))

    Ans = SumDigits(Value)

    print("Addition of digits is:", Ans)

if __name__ == "__main__":
    main()