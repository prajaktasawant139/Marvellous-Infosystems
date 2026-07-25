#Q6. write a script that schedules the following tasks: 
# 1.print Lunch Time! every day at 1:00 PM 
# 2.print Wrap up work every day at 6:00 PM. 
# both tasks should be handled by seperate function

import time 
import schedule

def LunchTime():
    print("Lunch Time..!!")

def WrapUp():
    print("Wrap Up Work..!!")

def main():
    schedule.every().day.at("13:00").do(LunchTime)
    schedule.every().day.at("18:00").do(WrapUp)
  
    print("Scheduler started... Press Ctrl+C to stop.")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

