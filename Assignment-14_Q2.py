# Q2. Write a lambda function which accepts one number and returns cube of that number.

cube = lambda x : x * x * x

def main():
    number = int(input("Enter a number: "))
    Ret = cube(number)
    print("Cube =", Ret)

if __name__ == "__main__":
    main()