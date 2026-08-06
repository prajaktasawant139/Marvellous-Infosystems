##########################################################
#
# Import Required Libraries
#
##########################################################

import sys
import os
import time
import hashlib
import schedule
import smtplib
from email.message import EmailMessage

##########################################################
#
# Function Name : CalculateChecksum
# Input         : File Name
# Output        : MD5 Checksum
# Description   : Returns checksum of file
#
##########################################################

def CalculateChecksum(Path):

    hobj = hashlib.md5()

    try:
        fobj = open(Path,"rb")

        while True:

            Buffer = fobj.read(1024)

            if(len(Buffer) == 0):
                break

            hobj.update(Buffer)

        fobj.close()

        return hobj.hexdigest()

    except Exception:
        return None

##########################################################
#
# Function Name : SendMail
# Input         : Receiver Mail, Log File
# Description   : Sends log file through Email
#
##########################################################

def SendMail(Receiver,LogFile):

    try:

        Sender = "pts13@gmail.com"
        Password = "Pass@123"

        Msg = EmailMessage()

        Msg["Subject"] = "Duplicate File Removal Log"
        Msg["From"] = Sender
        Msg["To"] = Receiver

        Msg.set_content("Please find attached log file.")

        with open(LogFile,"rb") as fobj:

            Data = fobj.read()

        Msg.add_attachment(Data,
                           maintype="application",
                           subtype="octet-stream",
                           filename=os.path.basename(LogFile))

        Server = smtplib.SMTP("smtp.gmail.com",587)

        Server.starttls()

        Server.login(Sender,Password)

        Server.send_message(Msg)

        Server.quit()

        print("Mail sent successfully")

    except Exception as E:

        print("Unable to send mail")
        print(E)

##########################################################
#
# Function Name : DuplicateFileRemoval
# Input         : Directory
# Description   : Scan directory for duplicate files
#
##########################################################

def DuplicateFileRemoval(DirectoryPath,Receiver):

    Border = "-"*50

    timestamp = time.ctime()

    LogFileName = "Marvellous_%s.log"%(timestamp)

    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")

    if(not os.path.exists("Marvellous")):
        os.mkdir("Marvellous")

    LogFileName = os.path.join("Marvellous",LogFileName)

    if(not os.path.exists(DirectoryPath)):
        print("Directory not found")
        return

    if(not os.path.isdir(DirectoryPath)):
        print("Invalid Directory")
        return

    print("Log File :",LogFileName)

    fobj = open(LogFileName,"w")

    fobj.write(Border+"\n")
    fobj.write("Duplicate File Removal Automation\n")
    fobj.write(Border+"\n\n")

    Duplicate = {}

    TotalFiles = 0
    DuplicateFiles = 0

##########################################################
# Scan Directory
##########################################################

    for FolderName, SubFolderNames, FileNames in os.walk(DirectoryPath):

        for File in FileNames:

            TotalFiles = TotalFiles + 1

            FilePath = os.path.join(FolderName, File)

            Checksum = CalculateChecksum(FilePath)

            if(Checksum == None):
                continue

            if(Checksum in Duplicate):
                Duplicate[Checksum].append(FilePath)
            else:
                Duplicate[Checksum] = [FilePath]

##########################################################
# Delete Duplicate Files
##########################################################

    DeletedFiles = 0

    fobj.write("Duplicate Files Deleted\n")
    fobj.write(Border + "\n")

    for Key in Duplicate:

        if(len(Duplicate[Key]) > 1):

            DuplicateFiles = DuplicateFiles + (len(Duplicate[Key]) - 1)

            fobj.write("\nChecksum : " + Key + "\n")

# Keep first file and delete remaining files
            for File in Duplicate[Key][1:]:

                try:

                    os.remove(File)

                    DeletedFiles = DeletedFiles + 1

                    print("Deleted :", File)

                    fobj.write("Deleted : " + File + "\n")

                except Exception as E:

                    fobj.write("Unable to Delete : " + File + "\n")
                    fobj.write(str(E) + "\n")

##########################################################
# Write Statistics
##########################################################

    fobj.write("\n")
    fobj.write(Border + "\n")

    fobj.write("Scan Time : " + timestamp + "\n")
    fobj.write("Directory : " + DirectoryPath + "\n")
    fobj.write("Total Files Scanned : " + str(TotalFiles) + "\n")
    fobj.write("Duplicate Files Found : " + str(DuplicateFiles) + "\n")
    fobj.write("Duplicate Files Deleted : " + str(DeletedFiles) + "\n")

    fobj.write(Border + "\n")

    fobj.close()

    print(Border)
    print("Total Files :", TotalFiles)
    print("Duplicate Files :", DuplicateFiles)
    print("Deleted Files :", DeletedFiles)
    print(Border)

##########################################################
# Send Log File through Email
##########################################################

    SendMail(Receiver, LogFileName)

##########################################################
#
# Function Name : Help
# Description   : Display Help
#
##########################################################

def Help():

    print("----------------------------------------------------")
    print("Duplicate File Removal Automation")
    print("----------------------------------------------------")
    print("Usage :")
    print("python DuplicateFileRemoval.py DirectoryPath TimeInterval Email")
    print("")
    print("Example :")
    print("python DuplicateFileRemoval.py D:\\Demo 5 abc@gmail.com")
    print("----------------------------------------------------")


##########################################################
#
# Function Name : Usage
# Description   : Display Usage
#
##########################################################

def Usage():

    print("Usage :")
    print("python DuplicateFileRemoval.py")
    print("<DirectoryPath> <TimeInterval in Minutes> <Receiver Email>")


##########################################################
#
# Function Name : main
# Description   : Entry point of application
#
##########################################################

def main():

    Border = "-" * 50

    print(Border)
    print("Duplicate File Removal Automation")
    print(Border)

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            Help()
            return

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            Usage()
            return

        else:
            print("Invalid Argument")
            return

    elif(len(sys.argv) != 4):

        print("Invalid Number of Arguments")
        print("Use --h for Help")
        print("Use --u for Usage")
        return

    DirectoryName = sys.argv[1]

    try:
        TimeInterval = int(sys.argv[2])
    except:
        print("Invalid Time Interval")
        return

    Receiver = sys.argv[3]

    print("Directory :", DirectoryName)
    print("Time Interval :", TimeInterval, "Minute(s)")
    print("Receiver :", Receiver)

    # First execution
    DuplicateFileRemoval(DirectoryName, Receiver)

    # Schedule execution
    schedule.every(TimeInterval).minutes.do(
        DuplicateFileRemoval,
        DirectoryName,
        Receiver
    )

    print("\nAutomation Started...\n")

    while True:

        schedule.run_pending()
        time.sleep(1)


##########################################################
#
# Starter
#
##########################################################

if __name__ == "__main__":
    main()


 