# Q1. Write a lambda function which accepts one number and returns square of that number.

square = lambda no : no * no

def main():
    num = int(input("Enter a number: "))
    print("Square =", square(num))

if __name__ == "__main__":
    main()