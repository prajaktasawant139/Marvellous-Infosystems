# Q6. Write a lambda function which accepts one number and returns True if number is odd otherwise False.

Odd = lambda n : n % 2 != 0

def main():
    n = int(input("Enter a number: "))

    if Odd(n):
        print(True)
    else:
        print(False)

if __name__ == "__main__":
    main()