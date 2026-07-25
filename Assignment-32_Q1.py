#Q1.Write a program that creates a new text file every minute.
#The filename should conatin the current timestamp.
#Example: File_25_07_2026_16_30_00.txt.
#write the following information inoto the file:Filename,Creation date,Creation time.

import time  
import schedule
from datetime import datetime


def CreateFile():

    current = datetime.now()

    filename = "File_" + current.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"

    file = open(filename, "w")
    file.write("Filename : " + filename + "\n")
    file.write("Creation Date : " + current.strftime("%d-%m-%Y") + "\n")
    file.write("Creation Time : " + current.strftime("%I:%M:%S %p") + "\n")
    file.close()

    print(filename, "created successfully.")

def main():

    schedule.every(1).minutes.do(CreateFile)

    print("Scheduler started... Press Ctrl+C to stop.")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()