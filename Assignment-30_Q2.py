#Q2.write a python program that display the current date and time after every one minute use the datetime module

import time
import datetime
import schedule

def DisplayDatetime():
    now = datetime.datetime.now()
    print("Current Date and Time is:", now.strftime("%d-%m-%Y %I:%M:%S %p"))

def main():
    schedule.every(1).minute.do(DisplayDatetime)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()