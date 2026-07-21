def main():
    FileName = input("Enter file name : ")

    try:
        fobj = open(FileName, "r")
        print(FileName, "exists in current directory.")

        fobj.close()

    except FileNotFoundError:
        print(FileName, "does not exist in current directory.")


if __name__ == "__main__":
    main()