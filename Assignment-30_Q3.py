#Q3.write a program that schedules a function to print : Coding Kar..! ,every 30 minutes

import time
import schedule

def Display():
    print("Coding Kar..!")

def main():
        schedule.every(30).minutes.do(Display)

        print("Program started... Press Ctrl+C to stop.")

        while True:
              schedule.run_pending()
              time.sleep(1)

if __name__ == "__main__":
      main()
