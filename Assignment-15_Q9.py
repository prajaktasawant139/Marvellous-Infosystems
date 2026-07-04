# Q9.Write a lambda function using reduce() which accepts a list of numbers and returns the product of all elements.

from functools import reduce

Product = lambda x, y : x * y

def main():
    Data = [1, 2, 3, 4, 5]
    print("Input Data is : ", Data)

    Ret = reduce(Product, Data)
    print("Product of all elements is : ", Ret)

if __name__ == "__main__":
    main()