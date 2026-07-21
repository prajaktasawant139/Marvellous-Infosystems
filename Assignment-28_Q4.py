def main():
    SourceFile = input("Enter source file name : ")
    DestinationFile = input("Enter destination file name : ")

    try:
        fobj1 = open(SourceFile, "r")
        print("Source file gets opened")

        Data = fobj1.read()

        fobj2 = open(DestinationFile, "w")
        fobj2.write(Data)

        print("Contents of", SourceFile, "copied into", DestinationFile)

        fobj1.close()
        fobj2.close()

    except FileNotFoundError:
        print("Source file is not present in current directory..")


if __name__ == "__main__":
    main()