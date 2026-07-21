def main():
    FileName = input("Enter file name : ")
    Word = input("Enter string to search : ")

    try:
        fobj = open(FileName, "r")
        print("File gets opened")

        Data = fobj.read()

        Count = Data.count(Word)

        print("Frequency of", Word, "is :", Count)

        fobj.close()

    except FileNotFoundError:
        print("File is not present in current directory..")


if __name__ == "__main__":
    main()