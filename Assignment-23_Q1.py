# Q1. Write a Python program using multiprocessing. Pool to calculate the sum of all even numbers from 1 to N for every number from the given list.

import multiprocessing
import os

def SumEven(No):
    Sum = 0

    for i in range(2, No + 1, 2):
        Sum = Sum + i

    return (os.getpid(), No, Sum)


def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    pobj = multiprocessing.Pool()

    Result = pobj.map(SumEven, Data)

    pobj.close()
    pobj.join()

    print("\nProcess ID\tInput Number\tSum of Even Numbers")
    print("-" * 60)

    for pid, num, total in Result:
        print(f"{pid}\t\t{num}\t\t{total}")


if __name__ == "__main__":
    main()