def main():
    FileName = input("Enter file name : ")

    try:
        fobj = open(FileName, "r")
        print("File gets opened")

        Data = fobj.read()

        Words = Data.split()

        Count = len(Words)

        print("Total number of words in", FileName, "are :", Count)

        fobj.close()

    except FileNotFoundError:
        print("File is not present in current directory..")


if __name__ == "__main__":
    main()