# Q2. Design a Python application that creates two threads named EvenFactor and OddFactor.
# Both threads should accept one integer number as a parameter.
# The EvenFactor thread should:
# Identify all even factors of the given number
# Calculate and display the sum of even factors.
# The OddFactor thread should:
# Identify all odd factors of the given number.
# Calculate and display the sum of odd factors.
# After both threads complete execution, the main thread should display the message: "Exit from main".


import time
import threading

def Factors(num):
    factors = []

    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)

    print("Factors of", num, "are:", factors)


def EvenFactor(num):
    even_factors = []
    sum_even = 0

    for i in range(1, num + 1):
        if num % i == 0 and i % 2 == 0:
            even_factors.append(i)
            sum_even += i

    print("Even Factors:", even_factors)
    print("Sum of Even Factors:", sum_even)


def OddFactor(num):
    odd_factors = []
    sum_odd = 0

    for i in range(1, num + 1):
        if num % i == 0 and i % 2 != 0:
            odd_factors.append(i)
            sum_odd += i

    print("Odd Factors:", odd_factors)
    print("Sum of Odd Factors:", sum_odd)


def main():
    number = int(input("Enter number: "))

    Factors(number)

    start_time = time.perf_counter()

    t1 = threading.Thread(target=EvenFactor, args=(number,))
    t2 = threading.Thread(target=OddFactor, args=(number,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    end_time = time.perf_counter()

    print("Exit from main")
    print(f"Time Required is : {end_time-start_time:.5f} seconds")


if __name__ == "__main__":
    main()