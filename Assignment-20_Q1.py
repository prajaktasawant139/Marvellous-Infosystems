# Q1. Design a Python application that creates two separate threads named Even and Odd.
# The Even thread should display the first 10 even numbers.
# The Odd thread should display the first 10 odd numbers.
# Both threads should execute independently using the threading module.
# Ensure proper thread creation and execution.


import time
import threading

def Even():
    print("First 10 Even Numbers:")
    for i in range(2, 21, 2):
        print(i)

def Odd():
    print("First 10 Odd Numbers:")
    for i in range(1, 20, 2):
        print(i)

def main():
    start_time = time.perf_counter()

    t1 = threading.Thread(target=Even,)
    t2 = threading.Thread(target=Odd,)

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    end_time = time.perf_counter()

     
    print("Both threads completed.")
    print(f"Time Required is : {end_time-start_time:.4f} seconds")


if __name__ == "__main__":
    main()