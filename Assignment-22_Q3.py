# Q3. For every number in the given list, count how many prime numbers exist between 1 and N using multiprocessing Pool.
#Display total prime count for each number.

import multiprocessing
import os

def ChkPrime(No):
    if No < 2:
        return False

    for i in range(2, int(No ** 0.5) + 1):
        if No % i == 0:
            return False

    return True


def PrimeCount(No):
    Count = 0

    for i in range(1, No + 1):
        if ChkPrime(i):
            Count += 1

    return (os.getpid(), No, Count)


def main():
    n = int(input("Enter the number of elements: "))

    Data = []
    print("Enter the numbers:")
    for i in range(n):
        Data.append(int(input()))

    pobj = multiprocessing.Pool()

    Result = pobj.map(PrimeCount, Data)

    pobj.close()
    pobj.join()

    print("\nProcess ID\tInput Number\tPrime Count")
    print("-" * 45)

    for pid, num, count in Result:
        print(f"{pid}\t\t{num}\t\t{count}")


if __name__ == "__main__":
    main()