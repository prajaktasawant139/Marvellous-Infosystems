# Q5. Write a program which accept N numbers from user and store it into List. Return addition of all prime numbers from that List. Main python file accepts N numbers from user and pass each number to ChkPrime() function which is part of our user defined module named as MarvellousNum. Name of the function from main python file should be ListPrime().

import A18Q5MarvellousNum


def ListPrime():
    n = int(input("Enter number of elements: "))

    total = 0
    data = []

    print("Enter the numbers:")
    for i in range(n):
        num = int(input())
        data.append(num)

        if A18Q5MarvellousNum.ChkPrime(num):
            total += num

    print("Addition of prime numbers is:", total)


def main():
    ListPrime()


if __name__ == "__main__":
    main()