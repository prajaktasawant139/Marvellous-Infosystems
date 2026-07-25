#Q2.write a python program that monitors the size of a specified file every 30 seconds.
#write the following details into: FileSizeLog.txt - FilePath,File size in bytes,Date and time .handle the situation where the file does not exist.

import os
import time
import schedule 
from datetime import datetime

def MonitorFile(file_path):
    if not os.path.isfile(file_path):
        print("File does not exist.")

        logfile = open("FileSizeLog.txt", "a")
        logfile.write("File Path : " + file_path + "\n")
        logfile.write("Status : File does not exist\n")
        logfile.write("Date and Time : " + datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") + "\n")
        logfile.write("-" * 40 + "\n")
        logfile.close()
        return

    size = os.path.getsize(file_path)

    logfile = open("FileSizeLog.txt", "a")
    logfile.write("File Path : " + file_path + "\n")
    logfile.write("File Size : " + str(size) + " bytes\n")
    logfile.write("Date and Time : " + datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") + "\n")
    logfile.write("-" * 40 + "\n")
    logfile.close()

    print("File size recorded successfully.")

def main():

    file_path = input("Enter file path: ").strip()

    

    schedule.every(30).seconds.do(MonitorFile, file_path)

    print("Monitoring started... .")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()