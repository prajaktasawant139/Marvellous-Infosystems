# Q3. Write a program that counts how many even numbers exist between 1 and N using Pool.map().


import multiprocessing
import os

def CountEven(No):
    Count = 0

    for i in range(2, No + 1, 2):
        Count += 1

    return (os.getpid(), No, Count)


def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    pobj = multiprocessing.Pool()

    Result = pobj.map(CountEven, Data)

    pobj.close()
    pobj.join()

    print("\nProcess ID\tInput Number\tEven Number Count")
    print("-" * 60)

    for pid, num, count in Result:
        print(f"{pid}\t\t{num}\t\t{count}")


if __name__ == "__main__":
    main()