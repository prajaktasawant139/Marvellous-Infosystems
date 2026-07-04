# Q10. Write a lambda function which accepts three numbers and returns largest number.

largest = lambda a, b, c : max(a, b, c)

def main():
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    n3 = int(input("Enter third number: "))
    
    print("Largest number =", largest(n1, n2, n3))

if __name__ == "__main__":
    main()