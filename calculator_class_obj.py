'''import the math library'''
import math

'''here the calculator is class'''


class Calculator:

    def __init__(self):
        pass

    def add(self, num1, num2):
        return num1 + num2

    def sub(self, num1, num2):
        return num1 - num2

    def mul(self, num1, num2):
        return num1 * num2

    def div(self, num1, num2):
        try:
            return num1 / num2
        except ZeroDivisionError as e:
            return e


display = Calculator()


def main():
    user_input = int(input("1.addition\n2.subtraction\n3.multiplication\n4.division\nEnter the user operation: "))
    num1 = int(input("enter first number:"))
    num2 = int(input("enter second number:"))
    if user_input == 1:
        print(display.add(num1, num2))
    elif user_input == 2:
        print(display.sub(num1, num2))
    elif user_input == 3:
        print(display.mul(num1, num2))
    elif user_input == 4:
        print(display.div(num1, num2))
    else:
        quit()


if __name__ == "__main__":
    main()
