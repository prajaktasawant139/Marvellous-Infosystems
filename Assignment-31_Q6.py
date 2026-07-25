#Q6.Write a program that schedules the following messages:
#Monday at 9:00 AM: Start your weekly goals
#Wednesday at 5:00 PM: Review your weekly progress
#Friday at 6:00 PM: Weekly work completed
#Use:schedule.every().monday.at(...) ,schedule.every().wednesday.at(...),schedule.every().friday.at(...)

import schedule 
import time 

def Monday_message():
    print("Start your weekly goals..")

def Wednesday_message():
    print("Review your weekly progress..")

def Friday_message():
    print("Weekly work completed..")

def main():

    schedule.every().monday.at("09:00").do(Monday_message)
    schedule.every().wednesday.at("17:00").do(Wednesday_message)
    schedule.every().friday.at("18:00").do(Friday_message)

    print("Schedular Started...")


    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()