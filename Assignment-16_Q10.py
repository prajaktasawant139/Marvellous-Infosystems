# Q10. Write a program which accepts name for user and display length of its name.

def NameLength(Name):

    return len(Name)

def main():
    Name = input("Enter Name : ")

    Length = NameLength(Name)
    print("Length of name is : ",Length)

if __name__ == "__main__":
    main()
