# Q3. Write a program which accept N numbers from user and store it into List. Return Minimum number from that List.

def minimum(numbers):
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num


def main():
    n = int(input("Enter number of elements: "))

    data = []

    print("Enter the numbers:")
    for i in range(n):
        value = int(input())
        data.append(value)

    ans = minimum(data)

    print("Minimum number is:", ans)


if __name__ == "__main__":
    main()