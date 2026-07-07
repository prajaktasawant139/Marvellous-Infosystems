# Q5. Write a program which contains filter(), map() and reduce() in it.
#  Python application which contains one list of numbers. 
# List contains the numbers which are accepted from user. 
# Filter should filter out all prime numbers. Map function will multiply each number by 2. 
# Reduce will return Maximum number from that numbers. (You can also use normal functions instead of lambda functions).


from functools import reduce

def ChkPrime(No):
    if No <= 1:
        return False

    for i in range(2, No):
        if No % i == 0:
            return False

    return True

MapX = lambda No: No * 2
ReduceX = lambda A, B: max(A, B)

def main():
    Size = int(input("Enter number of elements : "))

    Data = []

    print("Enter the elements :")
    for i in range(Size):
        Data.append(int(input()))

    FData = list(filter(ChkPrime, Data))
    print("List after filter :", FData)

    MData = list(map(MapX, FData))
    print("List after map :", MData)

    RData = reduce(ReduceX, MData)
    print("Output of reduce :", RData)

if __name__ == "__main__":
    main()