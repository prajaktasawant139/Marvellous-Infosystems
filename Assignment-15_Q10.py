# Q10.Write a lambda function using filter() which accepts a list of numbers and returns the count of even numbers.

Even = lambda No : No % 2 == 0

def main():
    Data = [13, 12, 8, 10, 11, 20]
    print("Input Data is : ", Data)

    FData = list(filter(Even, Data))
    Count = len(FData)

    print("Count of even numbers is : ", Count)

if __name__ == "__main__":
    main()