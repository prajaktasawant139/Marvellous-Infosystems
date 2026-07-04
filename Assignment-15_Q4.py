# Q4. Write a lambda function using reduce() which accepts a list of numbers and returns the addition of all elements.

from functools import reduce

Sum = lambda x, y : x + y

def main():
    Data = [13, 12, 8, 10, 11, 20]
    print("Input Data is : ", Data)

    Ret = reduce(Sum, Data)
    print("Addition of all elements is : ", Ret)

if __name__ == "__main__":
    main()