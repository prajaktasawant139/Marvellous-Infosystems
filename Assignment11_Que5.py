# Q5. Write a python program which accepts one number and checks whether it is palindrome or not.

def CheckPalindrome(No):

    Rev = ""

    for Digit in str(No):
        Rev = Digit + Rev

    if(str(No) == Rev):
        return True
    else:
        return False


def main():
    Value = int(input("Enter number : "))

    Ret = CheckPalindrome(Value)

    if(Ret == True):
        print("Number is Palindrome")
    else:
        print("Number is not Palindrome")


if __name__ == "__main__":
    main()