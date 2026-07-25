#Q4. create a task that executes every day at  9:00 AM and prints : Namaskar..!  use schedule.every().day.at("9:00").do(...)

import schedule
import time

def Display():
    print("Namaskar..!")

def main():

    schedule.every().day.at("09:00").do(Display)

    print("Program started... Waiting for 09:00 AM.")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__== "__main__":
    main()


