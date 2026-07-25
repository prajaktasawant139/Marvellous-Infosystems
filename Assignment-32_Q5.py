#Q5.write a program that deletes all empty files from a specified directory every hour.
#the program should:Scan the directory recursively,Detect files whose size is zero bytes,delete the empty files,store deleted file paths in a log file,handle  permission errors.

import os
import schedule
import time
from datetime import datetime

def DeleteEmptyFiles(directory):
    logfile = "DeletedFilesLog.txt"

    with open(logfile, "a") as log:
        log.write("\n----------------------------------------\n")
        log.write("Date & Time : " + str(datetime.now()) + "\n")

        for FolderName, SubFolders, FileNames in os.walk(directory):
            for File in FileNames:
                FilePath = os.path.join(FolderName, File)

                try:
                    if os.path.getsize(FilePath) == 0:
                        os.remove(FilePath)
                        print("Deleted :", FilePath)

                        log.write("Deleted : " + FilePath + "\n")

                except PermissionError:
                    print("Permission denied :", FilePath)
                    log.write("Permission denied : " + FilePath + "\n")

                except Exception as e:
                    print("Error :", e)
                    log.write("Error : " + str(e) + "\n")


def main():

    Directory = input("Enter directory name : ")

    if os.path.isdir(Directory):

        schedule.every().hour.do(DeleteEmptyFiles, Directory)

        print("Empty file deletion service started...")


        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid directory.")


if __name__ == "__main__":
    main()