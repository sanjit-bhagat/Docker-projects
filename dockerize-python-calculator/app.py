#!/usr/bin/env python3

class calculator:

    def __init__(self):
        pass

    def Addition(self):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        add = num1 + num2
        print(f"the Addition of two number: {add}")

    def Substraction(self):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        sub = num1 - num2
        print(f"the Substraction of two number: {sub}") 

    def Multiplication(self):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        mul = num1 * num2
        print(f"the Multiplication of two number: {mul}") 

    def Division(self):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if num2 == 0:
            print("Number does not divide by zero")
        else:
            div = num1 / num2
            print(f"the Division of two number: {div}") 

    def Modulus(self):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if num2 == 0:
            print("Cannot perform modulus with zero")
        else:
            mod = num1 % num2
            print(f"Modulus: {mod}")

    def Power(self):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        pow_val = num1 ** num2
        print(f"Power: {pow_val}")

    def Exit(self):
        print("Thanks for using...")


obj = calculator()

while True:

    print("=========================")
    print(" CALCULATOR APP ")
    print("=========================")
    print("1. ADDITION")
    print("2. SUBSTRACTION")
    print("3. MULTIPLICATION")
    print("4. DIVISION")
    print("5. MODULUS")
    print("6. POWER")
    print("7. EXIT")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        obj.Addition()

    elif choice == "2":
        obj.Substraction()

    elif choice == "3":
        obj.Multiplication()

    elif choice == "4":
        obj.Division()

    elif choice == "5":
        obj.Modulus()

    elif choice == "6":
        obj.Power()

    elif choice == "7":
        obj.Exit()
        break

    else:
        print("Invalid Choice, Try Again!")
