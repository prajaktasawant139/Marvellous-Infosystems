# Q6. Write a lambda function using reduce() which accepts a list of numbers and returns the minimum element.

from functools import reduce

FindMax = lambda x, y : x if x < y else y

def main():
    Data = [13, 12, 8, 10, 11, 20]
    print("Input Data is : ", Data)

    RData = reduce(FindMax, Data)
    print("Minimum element is : ", RData)

if __name__ == "__main__":
    main()