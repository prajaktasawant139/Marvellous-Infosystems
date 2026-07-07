# Q9. Write a program which accept number from user and return number of digits in that number.

def CountDigits(No):
    return len(str(No))

def main():
    Value = int(input("Enter a number: "))

    Ans = CountDigits(Value)

    print("Number of digits is:", Ans)

if __name__ == "__main__":
    main()