import sys

def main():
    try:
        SourceFile = sys.argv[1]

        fobj1 = open(SourceFile, "r")
        print("Source file gets opened")

        Data = fobj1.read()

        fobj2 = open("Demo1.txt", "w")
        fobj2.write(Data)

        print("Contents of", SourceFile, "copied into Demo1.txt")

        fobj1.close()
        fobj2.close()

    except FileNotFoundError:
        print("Source file is not present in current directory..")

    except IndexError:
        print("Please provide file name through command line.")


if __name__ == "__main__":
    main()