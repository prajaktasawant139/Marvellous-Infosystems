# Q1. Write a python program which accepts one character and checks whether it is vowel or consonant.

def CheckCharacter(ch):

    if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or
       ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
        return True
    else:
        return False


def main():
    Value = input("Enter a character : ")

    Ret = CheckCharacter(Value)

    if(Ret == True):
        print("It is a Vowel")
    else:
        print("It is a Consonant")


if __name__ == "__main__":
    main()