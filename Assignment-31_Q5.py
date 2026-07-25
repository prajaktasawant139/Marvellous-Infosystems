#Q5. Write a program that accepts a directory name from the user and counts the number of files inside it every five minutes.
#Write the result into: DirectoryCountLog.txt
#Each entry should contain: Directory path,Number of files,Date and time.

import os
import time
import schedule
from datetime import datetime


def CountFiles(directory):
    directory = directory.strip()

    if not os.path.isdir(directory):
        print("Invalid directory.")
        return

    count = 0

    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)):
            count = count + 1

    logfile = open("DirectoryCountLog.txt", "a")
    
    logfile.write("Directory Path : " + directory + "\n")
    logfile.write("Number of Files : " + str(count) + "\n")
    logfile.write("Date and Time : " + datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") + "\n")
    logfile.write("-" * 40 + "\n")

    logfile.close()

    print("Directory information saved to DirectoryCountLog.txt.")
def main():

    directory = input("Enter directory path:").strip()


    schedule.every(5).minutes.do(CountFiles, directory)


    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()