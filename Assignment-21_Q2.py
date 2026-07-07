# Q2. Design a Python application that creates two threads.
#Thread 1 should calculate and display the maximum element from an list.
#Thread 2 should calculate and display the minimum element from the same list.
#The list should be accepted from the user.


import threading

def Maximum(numbers):
    print("Maximum Element:", max(numbers))


def Minimum(numbers):
    print("Minimum Element:", min(numbers))


def main():
    numbers = []

    n = int(input("Enter number of elements: "))

    print("Enter list elements:")

    for i in range(n):
        num = int(input())
        numbers.append(num)
    t1 = threading.Thread(target=Maximum, args=(numbers,))
    t2 = threading.Thread(target=Minimum, args=(numbers,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()