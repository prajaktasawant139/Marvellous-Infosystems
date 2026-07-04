# Q4. Write a lambda function which accepts two numbers and returns minimum number.

minimum = lambda a, b : min(a, b)

def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Minimum =", minimum(a, b))

if __name__ == "__main__":
    main()