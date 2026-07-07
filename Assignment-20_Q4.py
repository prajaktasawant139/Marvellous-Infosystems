# Q4. Design a Python application that creates three threads named Small, Capital, and Digits.
#All threads should accept a string as input.
#The Small thread should count and display the number of lowercase characters.
#The Capital thread should count and display the number of uppercase characters.
#The Digits thread should count and display the number of numeric digits.
#Each thread must also display: Thread ID,Thread Name.


import threading

def Small(string):
    count = 0

    for char in string:
        if char.islower():
            count = count + 1

    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Lowercase Characters:", count)
    print()


def Capital(string):
    count = 0

    for char in string:
        if char.isupper():
            count = count + 1

    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Uppercase Characters:", count)
    print()


def Digits(string):
    count = 0

    for char in string:
        if char.isdigit():
            count = count + 1

    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Numeric Digits:", count)
    print()


def main():
    string = input("Enter string: ")

    t1 = threading.Thread(target=Small, args=(string,), name="Small")
    t2 = threading.Thread(target=Capital, args=(string,), name="Capital")
    t3 = threading.Thread(target=Digits, args=(string,), name="Digits")

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    t3.start()
    t3.join()

    print("Exit from main")


if __name__ == "__main__":
    main()