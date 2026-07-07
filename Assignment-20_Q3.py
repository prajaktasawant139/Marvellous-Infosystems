# Q3. Design a Python application that creates two threads named EvenList and OddList.
# Both threads should accept a list of integers as input.The EvenList thread should:
# Extract all even elements from the list.
# Calculate and display their sum.
# The OddList thread should:
# Extract all odd elements from the list.
# Calculate and display their sum. Threads should run concurrently.


import threading

def EvenList(numbers):
    even = []
    sum_even = 0

    for i in numbers:
        if i % 2 == 0:
            even.append(i)
            sum_even = sum_even + i

    print("Even Elements:", even)
    print("Sum of Even Elements:", sum_even)


def OddList(numbers):
    odd = []
    sum_odd = 0

    for i in numbers:
        if i % 2 != 0:
            odd.append(i)
            sum_odd = sum_odd + i

    print("Odd Elements:", odd)
    print("Sum of Odd Elements:", sum_odd)


def main():
    numbers = []

    n = int(input("Enter number of elements: "))

    print("Enter list elements:")
    for i in range(n):
        num = int(input())
        numbers.append(num)

    t1 = threading.Thread(target=EvenList, args=(numbers,))
    t2 = threading.Thread(target=OddList, args=(numbers,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()