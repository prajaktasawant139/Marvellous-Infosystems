# Q3. Write a python program which accepts one number and checks whether it is perfect number or not.

def CheckPerfect(No):

    Sum = 0

    for i in range(1, No):
        if(No % i == 0):
            Sum = Sum + i

    if(Sum == No):
        return True
    else:
        return False


def main():
    Value = int(input("Enter number : "))

    Ret = CheckPerfect(Value)

    if(Ret == True):
        print("Number is Perfect")
    else:
        print("Number is not Perfect")


if __name__ == "__main__":
    main()