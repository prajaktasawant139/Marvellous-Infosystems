#Q3.Write a program that scans a specified directory every minute.
# The task should display:Directory name,Number of files,Number of subdirectories,Date and time of scanning,Use the os module.
#Example output should:
#Directory Scanned: E:/Data
#Total Files: 15
#Total Subdirectories: 4
#Scan Time: 25-07-2026 04:30:00 PM


import os
import time
import schedule
from datetime import datetime

def ScanDirectory(path):
    file_count = 0
    directory_count = 0

    for item in os.listdir(path):
        full_path = os.path.join(path, item)

        if os.path.isfile(full_path):
            file_count = file_count + 1
        elif os.path.isdir(full_path):
            directory_count = directory_count + 1

    print("\nDirectory Scanned:", path)
    print("Total Files:", file_count)
    print("Total Subdirectories:", directory_count)
    print("Scan Time:", datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))

def main():
    directory = input("Enter Directory path: ")

    if not os.path.isdir(directory):
        print("Invalid directory path.")
        return

    # Schedule the scan every 1 minute
    schedule.every(1).minutes.do(ScanDirectory, directory)

    print("\nScanning directory every 1 minute...")
    


    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()


