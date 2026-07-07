# Q4. Write a program which accept one number form user and return addition of its factors.

def AddFactors(No):
    Sum = 0

    for i in range(1, No):
        if No % i == 0:
            Sum = Sum + i

    return Sum

def main():
    Value = int(input("Enter a number: "))

    Ans = AddFactors(Value)

    print("Addition of factors is:", Ans)

if __name__ == "__main__":
    main()