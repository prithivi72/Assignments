"""import the math  library"""
import math


def display_shape(user_in):
    """ user_input is used to get the value from the user"""
    if user_in == 1:
        print(" Selected Shape is CIRCLE :")
        print('''
        1.Area
        2.Perimeter
        3.Both Area and Perimeter
        ''')
        choice = int(input("Enter the choice: "))
        if choice == 1:
            radius = float(input("Enter the radius  of the circle :"))
            print("Area of the circle :", radius * radius * 3.14)
        elif choice == 2:
            radius = float(input("Enter the radius  of the circle :"))
            print("Perimeter of the circle :", (2 * radius * 3.14))
        elif choice == 3:
            radius = float(input("Enter the radius  of the circle :"))
            print("Area of the circle :", radius * radius * 3.14)
            print("Perimeter of the circle :", (2 * radius * 3.14))
        else:
            print('Enter the valid choice')
    elif user_in == 2:
        print(" Selected Shape is RECTANGLE :")
        print('''
                   1.Area
                   2.Perimeter
                   3.Volume
                   4.Value of Area,Perimeter and Volume
                   ''')
        choice = int(input("Enter the choice: "))
        if choice == 1:
            length = float(input("Enter the length  of the rectangle :"))
            width = float(input("Enter the width  of the rectangle :"))
            print("Area of the Rectangle :", (length * width))
        elif choice == 2:
            length = float(input("Enter the length  of the rectangle :"))
            width = float(input("Enter the width  of the rectangle :"))
            print("Perimeter of the Rectangle :", (2 * (length * width)))
        elif choice == 3:
            length = float(input("Enter the length of the Rectangle :"))
            width = float(input("Enter the width of the Rectangle :"))
            height = float(input("Enter the height of the Rectangle :"))
            print("Volume of the square :", (length * width * height))
        elif choice == 4:
            length = float(input("Enter the length  of the rectangle :"))
            width = float(input("Enter the width  of the rectangle :"))
            print("Area of the Rectangle :", (length * width))
            print("Perimeter of the Rectangle :", (2 * (length * width)))
            length = float(input("Enter the length of the Rectangle :"))
            width = float(input("Enter the width of the Rectangle :"))
            height = float(input("Enter the height of the Rectangle :"))
            print("Volume of the square :", (length * width * height))
        else:
            print("Enter the valid choice:")

    elif user_in == 3:
        print(" Selected Shape is Square :")
        print('''
                              1.Area
                              2.Perimeter
                              3.Volume
                              4.Value of Area,Perimeter and Volume
                              ''')
        choice = int(input("Enter the choice: "))
        if choice == 1:
            side = float(input("Enter the dimension of the square :"))
            print("Area of the square :", (side * side))
        elif choice == 2:
            side = float(input("Enter the dimension of the square :"))
            print("Perimeter of the square :", (4 * side))
        elif choice == 3:
            length = float(input("Enter the length of the Square :"))
            width = float(input("Enter the width of the Square :"))
            height = float(input("Enter the height of the square :"))
            print("Volume of the square :", (length * width * height))
        elif choice == 4:
            side = float(input("Enter the dimension of the square :"))
            print("Area of the square :", (side * side))
            print("Perimeter of the square :", (4 * side))
            length = float(input("Enter the length of the Square :"))
            width = float(input("Enter the width of the Square :"))
            height = float(input("Enter the height of the square :"))
            print("Volume of the square :", (length * width * height))
        else:
            print("Enter the valid choice:")
    elif user_in == 4:
        print("The selected shape is  TRIANGLE :")
        print('''
                                          1.Area
                                          2.Perimeter
                                          3.Volume
                                          4.Value pf Area,Perimeter,Volume
                                          ''')
        choice = int(input("Enter the choice: "))
        if choice == 1:
            breath = float(input("Enter the breath of the triangle :"))
            length = float(input("Enter the length of the triangle :"))
            print("Area of the Triangle :", (1 / 2 * (length * breath)))
        elif choice == 2:
            side_1 = float(input("Enter the side 1 of the Triangle :"))
            side_2 = float(input("Enter the side 2 of the Triangle :"))
            base = float(input("Enter the base of the Triangle :"))
            print("Perimeter of the Triangle :", (side_1 + side_2 + base))
        elif choice == 3:
            base_area = float(input("Enter the base area of the triangle :"))
            height = float(input("Enter the height of the triangle :"))
            print("Volume of the triangle:", (base_area * height))
        elif choice == 4:
            breath = float(input("Enter the breath of the triangle :"))
            length = float(input("Enter the length of the triangle :"))
            print("Area of the Triangle :", (1 / 2 * (length * breath)))
            side_1 = float(input("Enter the side 1 of the Triangle :"))
            side_2 = float(input("Enter the side 2 of the Triangle :"))
            base = float(input("Enter the base of the Triangle :"))
            print("Perimeter of the Triangle :", (side_1 + side_2 + base))
            base_area = float(input("Enter the base area of the triangle :"))
            height = float(input("Enter the height of the triangle :"))
            print("Volume of the triangle:", (base_area * height))
        else:
            print("Enter the valid choice")
   


class DifferentShapes:
    """display_shape using as function.self is used to call the class inside the function"""

    print("1.circle\
          2.Rectangle\
          3.Square\
          4.Triangle")


user_input = float(input("Enter the shape :"))
access = DifferentShapes()
display_shape(user_input)
