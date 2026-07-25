#Q1.write a program that accepts : 
# 1.a message from the user
# 2.a time interval in seconds
#Schedule the program to display the message repeatedly after the specified interval.
# example output: Enter message: Jay Ganesh , Enter interval in seconds :5 validate that the interval is grater than zero. 

import time
import schedule

def Display(msg):
    print(msg)

def main():
    message = input("Enter message: ")
    interval = int(input("Enter interval in seconds: "))

    if interval <= 0:
        print("Error: Interval must be greater than zero..")

    else:
        schedule.every(interval).seconds.do(Display,message)

        print("\nMessage will be displayed every", interval, "seconds.")

        while True:
            schedule.run_pending()
            time.sleep(1)

if __name__ == "__main__":
    main()