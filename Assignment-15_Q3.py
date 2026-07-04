# Q3. Write a lambda function using filter() which accepts a list of numbers and returns a list of odd numbers.

Odd = lambda No : No % 2 != 0

def main():
    Data = [13, 12, 8, 10, 11, 20]
    print("Input Data is : ", Data)

    FData = list(filter(Odd, Data))
    print("Odd numbers are : ", FData)

if __name__ == "__main__":
    main()