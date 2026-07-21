import sys

def main():
    try:
        FileName1 = sys.argv[1]
        FileName2 = sys.argv[2]

        fobj1 = open(FileName1, "r")
        fobj2 = open(FileName2, "r")

        print("Both files get opened")

        Data1 = fobj1.read()
        Data2 = fobj2.read()

        if Data1 == Data2:
            print("Success")
        else:
            print("Failure")

        fobj1.close()
        fobj2.close()

    except FileNotFoundError:
        print("File is not present in current directory..")

    except IndexError:
        print("Please provide two file names through command line.")


if __name__ == "__main__":
    main()