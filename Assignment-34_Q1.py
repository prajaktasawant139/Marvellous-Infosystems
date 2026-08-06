# System Surveillance System Project
# py ProcessSurvillence.py time_interval FolderName Receiver_Email
#        0                   1              2            3
# len(sys.argv) --> 4
# py ProcessSurvillence.py  --h
# py ProcessSurvillence.py  --u
#            0                 1
# len(sys.argv) --> 2

import psutil
import sys  
import os
import time
import schedule
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def ProcessScan():
    """Scans running system processes and maps resource metrics safely."""
    listprocess = []
    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=["pid", "name", "username", "status"])
            info["cpu_percent"] = proc.cpu_percent(None)
            info["memory_percent"] = proc.memory_percent()
            listprocess.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return listprocess


def SendLogMail(AttachmentPath, ReceiverEmail):
    """Sends the generated system surveillance log file to the target email address."""
    # Configuration - Change these defaults as required for your SMTP server
    SenderEmail = "pts123@gmail.com"
    SenderPassword = "Pass123"     # Use an App Password instead of plain passwords
    SmtpServer = "smtp.gmail.com"
    SmtpPort = 587

    try:
        # Create message container
        msg = MIMEMultipart()
        msg['From'] = SenderEmail
        msg['To'] = ReceiverEmail
        msg['Subject'] = f"Marvellous Platform Surveillance System Report: {time.strftime('%Y-%m-%d')}"

        body = "Hello,\n\nPlease find the attached system surveillance log file containing the active system report and process scan details.\n\nThanks,\nAutomation System"
        msg.attach(MIMEText(body, 'plain'))

        # Read and pack the log attachment
        if os.path.exists(AttachmentPath):
            with open(AttachmentPath, "rb") as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(AttachmentPath)}")
                msg.attach(part)
        else:
            print(f"Error: Attachment log file not found at {AttachmentPath}")
            return False

        # Open connection and send email
        server = smtplib.SMTP(SmtpServer, SmtpPort)
        server.starttls()                 # Upgrade connection to secure TLS encryption
        server.login(SenderEmail, SenderPassword)
        server.sendmail(SenderEmail, ReceiverEmail, msg.as_string())
        server.quit()
        
        print(f"Log file successfully emailed to: {ReceiverEmail}")
        return True

    except Exception as e:
        print(f"Failed to transmit email notification to {ReceiverEmail}: {e}")
        return False


def PlatformSurvillence(FolderName, ReceiverEmail=None):
    """Creates directory path structures, generates logs, and initiates mail transfers."""
    Border = "-" * 50
    Ret = os.path.exists(FolderName)

    if Ret == True:
        if os.path.isdir(FolderName) == False:
            print("Unable to proceed as folder name is existing but its not a directory")
            return
    else:
        os.mkdir(FolderName)
        print("Directory for the log file gets created successfully..")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")     
    FileName = os.path.join(FolderName, "Marvellous_%s.log" % timestamp)
    
    fobj = open(FileName, "w")
    print(f"Log file gets successfully created with name {FileName}")

    fobj.write(Border + "\n")
    fobj.write("---- Marvellous Platform Survillence System ----\n")
    fobj.write("Log file gets created at : " + timestamp + "\n")
    fobj.write(Border + "\n\n")
    fobj.write("-------------------------- System Report -----------------------------\n")

    # CPU Information
    fobj.write("number of active CPU cores : %s\n" % psutil.cpu_count())
    fobj.write("CPU Usage : %s %%\n" % psutil.cpu_percent(interval=0.1))
    fobj.write(Border + "\n")

    # RAM Information
    memory = psutil.virtual_memory()
    fobj.write("RAM Usage : %s %%\n" % memory.percent)
    fobj.write("Total RAM Available : %s\n" % memory.total)
    fobj.write(Border + "\n")

    # Network Usage
    netobj = psutil.net_io_counters()
    fobj.write("Network Usage Report\n")
    fobj.write("Sent : %.2f MB\n" % (netobj.bytes_sent / (1024 * 1024)))
    fobj.write("Received : %.2f MB\n" % (netobj.bytes_recv / (1024 * 1024)))
    fobj.write(Border + "\n")

    # Process Log
    Data = ProcessScan()
    for info in Data:
        fobj.write("pid : %s\n" % info.get("pid"))
        fobj.write("name : %s\n" % info.get("name"))
        fobj.write("username : %s\n" % info.get("username"))
        fobj.write("status : %s\n" % info.get("status"))
        fobj.write("CPU Usage : %.4f\n" % info.get("cpu_percent", 0.0))
        fobj.write("RAM Usage : %.2f\n" % info.get("memory_percent", 0.0))
        fobj.write(Border + "\n")

    fobj.write(Border + "\n")
    fobj.write("------------------------ End of Log File -----------------------\n")
    fobj.write(Border + "\n")
    fobj.close()

    # Trigger optional email routine after file is completely closed out
    if ReceiverEmail:
        SendLogMail(FileName, ReceiverEmail)


def main():
    Border = "-" * 50
    print(Border)
    print("---- Marvellous Platform Survillence System ----")
    print(Border)

    # Help (--h) and Usage (--u) flags check
    if len(sys.argv) == 2:
        flag = sys.argv[1].lower()
        if flag == "--h":
            print("This automation script is use to perform")
            print("1 : It fetch the information of running processes")
            print("2 : It fetches the information about primary storage RAM")
            print("3 : It fetches the information about secondary storage as HDD")
            print("4 : It fetches the information about the microprocessor")
            print("5 : It gets auto scheduled periodically")
            print("6 : It maintains all records into log file")
            print("7 : It sends the log files through mail periodically")
        elif flag == "--u":
            print("Use the automation script as : ")
            print(f"Python {sys.argv[0]} Time_Interval FolderName Receiver_Email")
            print("Time_Interval  : Time in minutes for periodic execution")
            print("Folder_Name    : Name of folder for the log file creation")
            print("Receiver_Email : Email address to receive log files")
        else:
            print("Unable to proceed as there is no matching argument")
            print("Please use --h or --u flag for getting more details..")
        
    # Project Code execution handling 3 inputs: interval, directory, email ID
    elif len(sys.argv) == 4:
        print("Scheduler Started Successfully..")
        print("Press Ctrl+C to abort the automation script..")
        
        time_interval = int(sys.argv[1])
        folder_name = sys.argv[2]
        receiver_email = sys.argv[3]

        # Initial launch call
        PlatformSurvillence(folder_name, receiver_email)
     
        # Register scheduled looping configurations
        schedule.every(time_interval).minutes.do(PlatformSurvillence, folder_name, receiver_email)
        
        try:
            while True:
                schedule.run_pending()
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nMonitoring stopped by user.")
    
    else:
        print("Invalid number of arguments..")
        print("Unable to proceed as arguments are not matching")
        print("Please use --h or --u flag for getting more details..")

    print(Border)
    print("---- Thank you for using our automation system ---- ")
    print(Border)

if __name__ == "__main__":
    main()
