def main():
    FileName = input("Enter file name : ")

    try:
        fobj = open(FileName, "r")
        print("File gets opened")

        Count = 0

        for line in fobj:
            Count = Count + 1

        print("Total number of lines in", FileName, "are :", Count)

        fobj.close()

    except FileNotFoundError:
        print("File is not present in current directory..")


if __name__ == "__main__":
    main()
