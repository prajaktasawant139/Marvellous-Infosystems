# Q4. Write a program that counts how many odd numbers exist between 1 and N.

import multiprocessing
import os

def CountOdd(No):
    Count = 0

    for i in range(1, No + 1, 2):
        Count = Count + 1

    return (os.getpid(), No, Count)


def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    pobj = multiprocessing.Pool()

    Result = pobj.map(CountOdd, Data)

    pobj.close()
    pobj.join()

    print("\nProcess ID\tInput Number\tOdd Number Count")
    print("-" * 60)

    for pid, num, count in Result:
        print(f"{pid}\t\t{num}\t\t{count}")


if __name__ == "__main__":
    main()