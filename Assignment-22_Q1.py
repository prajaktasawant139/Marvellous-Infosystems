# Q1. Write a program that accepts a list of integers and uses Pool.map() 
# to calculate the sum of squares from 1 to N for every element in the list.


import time
import multiprocessing
import os

def SumSquare(No):
    print("Process is running with PID :", os.getpid())

    Sum = 0

    for i in range(1, No + 1):
        Sum = Sum + (i ** 2)

    return Sum


def main():
    Data = [1000000, 2000000, 3000000, 4000000]
    Result = []

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()

    Result = pobj.map(SumSquare, Data)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    print("Result is :")
    print(Result)
    print(f"Time Required is : {end_time - start_time:.4f} seconds")


if __name__ == "__main__":
    main()