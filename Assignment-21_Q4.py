# Q5. Design a Python application that creates two threads.
#Thread 1 should compute the sum of elements from a list.
#Thread 2 should compute the product of elements from the same list.
#Return the results to the main thread and display them.


import threading

sum_result = 0
product_result = 1


def Sum(numbers):
    global sum_result
    for i in numbers:
        sum_result = sum_result + i


def Product(numbers):
    global product_result
    for i in numbers:
        product_result = product_result * i


def main():
    n = int(input("Enter number of elements: "))

    numbers = []

    print("Enter the elements:")
    for i in range(n):
        num = int(input())
        numbers.append(num)

    t1 = threading.Thread(target=Sum, args=(numbers,))
    t2 = threading.Thread(target=Product, args=(numbers,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Sum of elements:", sum_result)
    print("Product of elements:", product_result)


if __name__ == "__main__":
    main()