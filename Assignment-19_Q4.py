# Q4. Write a program which contains filter(), map() and reduce() in it.
#  Python application which contains one list of numbers. 
# List contains the numbers which are accepted from user. 
# Filter should filter out all such numbers which are even. Map function will calculate its square.
#  Reduce will return addition of all that numbers.

from functools import reduce

FilterX = lambda No: (No % 2 == 0)
MapX = lambda No: No ** 2
ReduceX = lambda A, B: A + B

def main():
    Size = int(input("Enter number of elements : "))

    Data = []

    print("Enter the elements :")
    for i in range(Size):
        Data.append(int(input()))

    FData = list(filter(FilterX, Data))
    print("List after filter :", FData)

    MData = list(map(MapX, FData))
    print("List after map :", MData)

    RData = reduce(ReduceX, MData)
    print("Output of reduce :", RData)

if __name__ == "__main__":
    main()