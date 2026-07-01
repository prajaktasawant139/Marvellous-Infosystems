# Q1. Write a python program which accepts one number and checks whether it is prime or not.

def CheckPrime(No):

    if(No <= 1):
        return False

    for i in range(2, No):
        if(No % i == 0):
            return False

    return True


def main():
    Value = int(input("Enter number : "))

    Ret = CheckPrime(Value)

    if(Ret == True):
        print("Number is Prime")
    else:
        print("Number is not Prime")


if __name__ == "__main__":
    main()