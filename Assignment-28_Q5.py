def main():
    FileName = input("Enter file name : ")
    Word = input("Enter word to search : ")

    try:
        fobj = open(FileName, "r")
        print("File gets opened")

        Data = fobj.read()

        if Word in Data:
            print(Word, "is present in", FileName)
        else:
            print(Word, "is not present in", FileName)

        fobj.close()

    except FileNotFoundError:
        print("File is not present in current directory..")


if __name__ == "__main__":
    main()