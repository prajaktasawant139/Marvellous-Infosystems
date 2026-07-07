# Q1. Design a Python application that creates two threads named Prime and NonPrime.
#Both threads should accept a list of integers.
#The Prime thread should display all prime numbers from the list.
#The Non Prime thread should display all non-prime numbers from the list.


import threading

def isPrime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def Prime(numbers):
    prime_list = []

    for i in numbers:
        if isPrime(i):
            prime_list.append(i)

    print("Prime Numbers:", prime_list)


def NonPrime(numbers):
    nonprime_list = []

    for i in numbers:
        if not isPrime(i):
            nonprime_list.append(i)

    print("Non-Prime Numbers:", nonprime_list)


def main():

    numbers = []

    n = int(input("Enter number of elements: "))

    print("Enter list elements:")

    for i in range(n):
        num = int(input())
        numbers.append(num)

    t1 = threading.Thread(target=Prime, args=(numbers,))
    t2 = threading.Thread(target=NonPrime, args=(numbers,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()