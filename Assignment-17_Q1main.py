# Q1. Create an module named as Arithmetic which contains 4 functions as Add() for addition, Sub() for subtraction, Mult() for multiplication and Div() for division. All functions accepts two parameters as number and perform the operation. Write on python program which call all the functions from Arithmetic module by accepting the parameters from user.

import Assignment17Q1ArithmaticModule

def main():

    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    print("Addition is :", Assignment17Q1ArithmaticModule.Addition(No1, No2))
    print("Substraction is :", Assignment17Q1ArithmaticModule.Substraction(No1, No2))
    print("Multiplication is :", Assignment17Q1ArithmaticModule.Multiplication(No1, No2))
    print("Division is :", Assignment17Q1ArithmaticModule.Division(No1, No2))

if __name__ == "__main__":
    main()








