# Q8. Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5.

CheckDiv = lambda No : No % 3 == 0 and No % 5 == 0

def main():
    Data = [15, 30, 9, 10, 20, 45, 60, 7]
    print("Input Data is : ", Data)

    FData = list(filter(CheckDiv, Data))
    print("Numbers divisible by 3 and 5 are : ", FData)

if __name__ == "__main__":
    main()