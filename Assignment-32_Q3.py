#Q3.write a program that reads and display the contents of a specified text file every minute.
#handle the following conditions:File does not exist,File is empty,Permission is denied,File cannot be opened.

import os
import time
import schedule


def ReadFile(file_path):

    try:
        if not os.path.exists(file_path):
            print("File does not exist.")
            return

        if os.path.getsize(file_path) == 0:
            print("File is empty.")
            return

        file = open(file_path, "r")

        print("\nFile Contents:")
        print(file.read())

        file.close()

    except PermissionError:
        print("Permission is denied.")

    except IOError:
        print("File cannot be opened.")

def main():

    file_path = input("Enter file path: ").strip()


    schedule.every(1).minutes.do(ReadFile, file_path)

    print("Monitoring started... Press Ctrl+C to stop.")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()