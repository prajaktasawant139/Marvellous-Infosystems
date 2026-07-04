# Q3. Write a lambda function which accepts two numbers and returns maximum number.

maximum = lambda a, b : max(a, b)

def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Maximum =", maximum(a, b))

if __name__ == "__main__":
    main()