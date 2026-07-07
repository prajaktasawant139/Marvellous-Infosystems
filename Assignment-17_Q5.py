# Q5. Write a program which accept one number for user and check whether number is prime or not.

def CheckPrime(No):
    if No <= 1:
        return False

    for i in range(2, No):
        if No % i == 0:
            return False

    return True

def main():
    Value = int(input("Enter a number: "))

    if CheckPrime(Value):
        print("Number is Prime")
    else:
        print("Number is Not Prime")

if __name__ == "__main__":
    main()