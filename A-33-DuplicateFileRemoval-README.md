# Duplicate File Removal Automation Using Python

## Project Information

**Project Name:** Duplicate File Removal Automation

**Language:** Python

**IDE:** Visual Studio Code 

**Operating System:** Windows 11pro

**Author:** Prajakta Tulshiram Sawant

---

# Introduction

Duplicate files occupy unnecessary storage space and make file management difficult. This project automates the process of identifying and removing duplicate files from a specified directory. It uses the MD5 checksum algorithm to compare file contents instead of file names, ensuring accurate duplicate detection.

---

# Problem Statement

Develop a Python automation script that periodically scans a directory, detects duplicate files using MD5 checksum, removes duplicate copies while keeping one original file, generates a log file containing the execution details, and emails the generated log file to a specified recipient.

---

# Objectives

- Automate duplicate file removal.
- Reduce storage usage.
- Improve file management.
- Generate execution logs.
- Send log through email.
- Execute periodically.

---

# Features

- Recursive directory scanning
- Duplicate detection using MD5 checksum
- Automatic duplicate file deletion
- Timestamp-based log generation
- Email notification with log attachment
- Periodic execution using Scheduler
- Help (--h) and Usage (--u) support
- Exception handling

---

# Modules Used

| Module | Purpose |
|---------|---------|
| os | File and directory operations |
| sys | Command-line arguments |
| hashlib | Generate MD5 checksum |
| time | Date and time handling |
| schedule | Periodic task scheduling |
| smtplib | Sending emails |
| email.message | Email attachment support |

---

# Software Requirements

- Python 3.14.5
- Visual Studio Code / PyCharm
- Windows Operating System

---

# Hardware Requirements

- Processor : Intel(R) Core(TM) i5-10210U CPU @ 1.60GHz (2.11 GHz)
- RAM : 16.0 GB 
- Hard Disk : 5171 GB of 477 GB used

---

# Installation

Install Python.

Install schedule module.

```bash
pip install schedule
```

---

# Folder Structure

```
DuplicateFileRemoval.py

README.md

Marvellous/
      Marvellous_Mon_Aug_06_10_30_10_2026.log
```

---

# Command to Execute

```bash
python DuplicateFileRemoval.py <DirectoryPath> <TimeInterval> <Email>
```

Example

```bash
python DuplicateFileRemoval.py D:\Demo 5 abc@gmail.com
```

---

# Algorithm

1. Accept directory path, time interval and email address.
2. Validate the input arguments.
3. Traverse the directory recursively.
4. Calculate MD5 checksum for every file.
5. Store checksum in a dictionary.
6. Compare checksum values.
7. If duplicate exists, delete duplicate copy.
8. Generate log file.
9. Send log file through email.
10. Repeat after specified time interval.

---

# Working

- Reads command-line arguments.
- Traverses all folders recursively.
- Calculates MD5 checksum.
- Detects duplicate files.
- Deletes duplicate files.
- Generates log file.
- Sends log through Gmail.
- Runs periodically.

---

# Output

Console

```
--------------------------------------------------
Duplicate File Removal Automation
--------------------------------------------------

Directory : D:\Demo

Total Files : 50

Duplicate Files : 8

Deleted Files : 8

Mail Sent Successfully
```

---

# Sample Log File

```
--------------------------------------------------

Duplicate File Removal Automation

--------------------------------------------------

Scan Time : Thu Aug 06 10:30:15 2026

Directory : D:\Demo

Total Files Scanned : 50

Duplicate Files Found : 8

Duplicate Files Deleted : 8

Deleted Files

D:\Demo\Test\File1.pdf

D:\Demo\Images\Copy.jpg

--------------------------------------------------
```

---

# Advantages

- Saves storage space.
- Eliminates duplicate files.
- Fully automatic.
- Generates execution logs.
- Email notification.
- Easy to use.
- Reduces manual work.

---

# Limitations

- Uses Gmail SMTP configuration.
- Requires Internet connection for email.
- Permanently deletes duplicate files.

---

# Future Scope

- GUI using Tkinter.
- SHA-256 checksum support.
- Backup before deletion.
- Database log storage.
- PDF report generation.
- Cloud storage support.

---

# Conclusion

This project successfully automates the task of identifying and removing duplicate files from a specified directory. It minimizes storage wastage, generates execution reports, and sends log files through email. The automation can run periodically without user intervention, making file management efficient and reliable.

---

# Author

**Prajakta Tulshiram Sawant**

Master of Computer Science

Python Automation Project

Marvellous Infosystems