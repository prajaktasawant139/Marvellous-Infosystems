# Q5. Write a lambda function which accepts one number and returns True if number is even otherwise False.

Even = lambda n : n % 2 == 0

def main():
    num = int(input("Enter a number: "))
    
    if Even(num):
        print(True)
    else:
        print(False)

if __name__ == "__main__":
    main()