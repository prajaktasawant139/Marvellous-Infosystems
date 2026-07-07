# Q1. Write a program which accept N numbers from user and store it into List. Return addition of all elements from that List.

def addition(numbers):
    return sum(numbers)

def main():
    n = int(input("Enter number of elements: "))

    data = []

    for i in range(n):
        data.append(int(input("Enter number : ")))

    print("Addition of all elements is:", addition(data))

if __name__ == "__main__":
    main()