# Q2. Write a program which accept N numbers from user and store it into List. Return Maximum number from that List.


def maximum(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num


def main():
    n = int(input("Enter number of elements: "))

    data = []

    print("Enter the numbers:")
    for i in range(n):
        value = int(input())
        data.append(value)

    ans = maximum(data)

    print("Maximum number is:", ans)


if __name__ == "__main__":
    main()