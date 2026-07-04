# Q9. Write a lambda function which accepts two numbers and returns multiplication.

multiplication = lambda a, b : a * b

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("Multiplication =", multiplication(num1, num2))

if __name__ == "__main__":
    main()