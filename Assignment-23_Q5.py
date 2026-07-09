# Q5. Write  a program that calculates factorials of multiple numbers simultaneously using multiprocessing.pool

import multiprocessing
import os

def Factorial(No):
    Fact = 1

    for i in range(1, No + 1):
        Fact = Fact * i

    return (os.getpid(), No, Fact)


def main():
    Data = [10, 15, 20, 25]

    pobj = multiprocessing.Pool()

    Result = pobj.map(Factorial, Data)

    pobj.close()
    pobj.join()

    print("\nProcess ID\tInput Number\tFactorial")
    print("-" * 70)

    for pid, num, fact in Result:
        print(f"{pid}\t\t{num}\t\t{fact}")


if __name__ == "__main__":
    main()

    