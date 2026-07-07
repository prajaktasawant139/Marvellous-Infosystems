# Q7. Write a program which accept one number and display below pattern

def Display(No):
    for i in range(No):
        print(*range(1, No + 1))

def main():
    Value = int(input("Enter a number: "))
    Display(Value)

if __name__ == "__main__":
    main()