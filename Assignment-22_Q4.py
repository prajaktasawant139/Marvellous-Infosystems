# Q4. Write a program that calculates 1^5 + 2^5 + 3^5 +......+N^5.
# for multiple values of N simultaneously using Pool. Measure total execution time.
    

import multiprocessing
import time
import os

def SumPower5(No):
    Sum = 0

    for i in range(1, No + 1):
        Sum = Sum + (i ** 5)

    return (os.getpid(), No, Sum)


def main():
    n = int(input("Enter the number of elements: "))

    Data = []
    print("Enter the values of N:")
    for i in range(n):
        Data.append(int(input()))

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()

    Result = pobj.map(SumPower5, Data)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    print("\nProcess ID\tInput Number\tSum")
    print("-" * 50)

    for pid, num, total in Result:
        print(f"{pid}\t\t{num}\t\t{total}")

    print(f"\nTotal Execution Time : {end_time - start_time:.4f} seconds")


if __name__ == "__main__":
    main()