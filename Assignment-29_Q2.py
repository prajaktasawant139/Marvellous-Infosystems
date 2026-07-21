def main():
    FileName = input("Enter file name : ")

    try:
        fobj = open(FileName, "r")
        print("File gets opened")

        Data = fobj.read()

        print("Contents of", FileName, "are :")
        print(Data)

        fobj.close()

    except FileNotFoundError:
        print("File is not present in current directory..")


if __name__ == "__main__":
    main()