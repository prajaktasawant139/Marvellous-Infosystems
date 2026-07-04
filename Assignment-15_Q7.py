# Q7. Write a lambda function using filter() which accepts a list of strings and returns a list of strings having length greater than 5.

CheckLength = lambda Str : len(Str) > 5

def main():
    Data = ["apple", "banana", "grapes", "kiwi", "pineapple", "mango"]
    print("Input Data is : ", Data)

    FData = list(filter(CheckLength, Data))
    print("Strings with length > 5 are : ", FData)

if __name__ == "__main__":
    main()