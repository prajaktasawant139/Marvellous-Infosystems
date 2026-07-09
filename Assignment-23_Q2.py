# Q2. Write a Python program using multiprocessing. Pool to calculate the sum of all odd numbers from 1 to N.


import multiprocessing
import os

def SumOdd(No):
    Sum = 0

    for i in range(1, No + 1, 2):
        Sum = Sum + i

    return (os.getpid(), No, Sum)


def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    pobj = multiprocessing.Pool()

    Result = pobj.map(SumOdd, Data)

    pobj.close()
    pobj.join()

    print("\nProcess ID\tInput Number\tSum of Odd Numbers")
    print("-" * 60)

    for pid, num, total in Result:
        print(f"{pid}\t\t{num}\t\t{total}")


if __name__ == "__main__":
    main()
