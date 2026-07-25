# Create a function named: DisplayMessage(message)  
# schedule the function using: schedule.every(5).seconds.do(DisplayMessage,message) the message should be accepted from the user.

import time 
import schedule

def DisplayMessage(message):
    print(message)

def main():
    message = input("Enter message: ")

    schedule.every(5).seconds.do(DisplayMessage,message)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()