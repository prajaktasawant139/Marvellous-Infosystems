# Q4. Write a program which accept N numbers from user and store it into List. Accept one another number from user and return frequency of that number from List.

def frequency(numbers, value):
    return len(list(filter(lambda x: x == value, numbers)))


def main():
    n = int(input("Enter number of elements: "))

    data = []

    for i in range(n):
        data.append(int(input("Enter number: ")))

    search = int(input("Enter number to search: "))

    print("Frequency is:", frequency(data, search))


if __name__ == "__main__":
    main()