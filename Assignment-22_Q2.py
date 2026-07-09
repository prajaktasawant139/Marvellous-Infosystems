# Q2. Write a program that calculates factorials of multiple numbers simultaneously using Pool.map().


import multiprocessing
import os

def Factorial(No):
    Fact = 1
    for i in range(1, No + 1):
        Fact = Fact * i

    return (os.getpid(), No, Fact)

def main():
    n = int(input("Enter the number of elements: "))

    Data = []
    print("Enter the numbers:")
    for i in range(n):
        Data.append(int(input()))

    pobj = multiprocessing.Pool()

    Result = pobj.map(Factorial, Data)

    pobj.close()
    pobj.join()

    print("\nProcess ID\tInput Number\tFactorial")
    print("-" * 45)

    for pid, num, fact in Result:
        print(f"{pid}\t\t{num}\t\t{fact}")

if __name__ == "__main__":
    main()