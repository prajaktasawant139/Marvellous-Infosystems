# Q6. Write a program which accept one number and display below pattern.

def Display(No):
    for i in range(No, 0, -1):
        for j in range(i):
            print("  *  ", end =" ")
        print()

def main():
    Value = int(input("Enter a number: "))
    Display(Value)

if __name__ == "__main__":
    main()