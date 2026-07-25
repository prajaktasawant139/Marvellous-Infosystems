#Q4.write a program that copies all .txt files from one directory to another directory every ten minutes.
#the program should:Accept source & destination directories,Validate both directories,copy only .txt files,Maintain a log of copied files,Avoid terminating if one file cannot be copied.

import os 
import time
import schedule
import shutil
from datetime import datetime

def CopyFiles(source, destination):

    if not os.path.isdir(source):
        print("Invalid source directory.")
        return

    if not os.path.isdir(destination):
        print("Invalid destination directory.")
        return

    for file in os.listdir(source):

        if file.endswith(".txt"):

            source_path = os.path.join(source, file)
            destination_path = os.path.join(destination, file)

            try:
                shutil.copy(source_path, destination_path)

                logfile = open("CopyLog.txt", "a")
                logfile.write("Copied : " + file + "\n")
                logfile.write("Date and Time : " + datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") + "\n")
                logfile.write("-" * 40 + "\n")
                logfile.close()

                print(file, "copied successfully.")

            except Exception:
                print("Could not copy:", file)

def main():

    source = input("Enter source directory: ").strip()
    destination = input("Enter destination directory: ").strip()

    

    schedule.every(10).minutes.do(CopyFiles, source, destination)

    print("Scheduler started... Press Ctrl+C to stop.")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()