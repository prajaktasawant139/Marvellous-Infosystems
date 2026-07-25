import os
import time
import schedule
import shutil
import datetime

def Backup():
    source = input("Enter source file path: ")
    destination = input("Enter destination directory path: ")

    filename = os.path.basename(source)
    name,extension = os.path.splitext(filename)

    current = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

    backupfile = name + "_" + current + extension

    shutil.copy(source, os.path.join(destination, backupfile))

    logfile = open("backup_log.txt","a")
    logfile.write("Backup completed successfully at : ")
    logfile.write(datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))
    logfile.write("\n")
    logfile.close()

    print("Backup completed successfully..")

def main():
    schedule.every(1).hours.do(Backup)

    print("Backup schedular started...Press Ctrl+C to stop.")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()