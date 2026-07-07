# Q2. Write a program which accept one number and display below pattern.

def Dispaly(No):
    for i in range(No):
        print("  *  " * No)

def main():
    Value = int(input("Enter number : "))
    Dispaly(Value)

if __name__ == "__main__":
    main()