# Q7. Write a lambda function which accepts one number and returns True if divisible by 5.

check = lambda n: n % 5 == 0

def main():
    n = int(input("Enter a number: "))
    
    if check(n):
        print(True)
    else:
        print(False)

if __name__ == "__main__":
    main()