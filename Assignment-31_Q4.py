#Q4.Write a program that creates a new log file after every 10 minutes.
#The filename should contain the current date and time.
#Example: MarvellousLog_25_07_2026_16_30_00.txt
#The file should contain: Log file created successfully,Creation Time: 25-07-2026 04:30:00 PM

import schedule
import time
from datetime import datetime

def CreateLogFile():
    file_name = "MarvellousLog_" + datetime.now().strftime("%d_%m_%Y_%H_%M_%S") + ".txt"

    file = open(file_name, "w")

    file.write("Log File Created Successfully..\n")
    file.write("Creation Time: ")
    file.write(datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))

    file.close()

    print(file_name," Created Successfully..")


def main():
    schedule.every(10).minutes.do(CreateLogFile)

    print("Log File will be created every 10 minutes...")

 
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ =="__main__":
    main()