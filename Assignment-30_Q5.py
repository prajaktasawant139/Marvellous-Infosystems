#Q5. Schedule a task that executes every five minutes
#the task should write the current date and time into a file named: Marvellous.txt new entities should be appended without removing previous entities.

import time
import datetime
import schedule

def WriteToFile():
    now = datetime.datetime.now()

    file = open("Marvellous.txt","a")
    file.write("Task executed at : " + now.strftime("%d/%m/%Y %I:%M:%S %p") + "\n")
    file.close()

    print("Data written successfully..")

def main():
    schedule.every(5).minutes.do(WriteToFile)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()