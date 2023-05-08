'''import the math  library'''
import math
class DifferentShapes():
    '''display_shape using as function.self is used to call the class inside the function'''
    def display_shape(self, user_input):
        ''' user_input is used to get the value from the user'''
        if user_input==1:
            print(" Selected Shape is CIRCLE :")
            radius=float(input("Enter the radius  of the circle :"))
            print("Area of the circle :",radius*radius*3.14)
            print("Perimeter of the circle :",(2*radius*3.14))
        elif user_input==2:
            print("The selected shape is RECTANGLE : ")
            length=float(input("Enter the length  of the rectangle :"))
            width=float(input("Enter the width  of the rectangle :"))
            print("Area of the Rectangle :",(length*width))
            print("Perimeter of the Rectangle :",(2*(length*width)))
            length=float(input("Enter the length of the Rectangle :"))
            width=float(input("Enter the width of the Rectangle :"))
            height=float(input("Enter the height of the Rectangle :"))
            print("Volume of the square :",(length*width*height))
        elif user_input==3:
            print("The Selected shape is SQUARE :")
            side=float(input("Enter the dimension of the square :"))
            print("Area of the square :",(side*side))
            print("Perimeter of the square :",(4*side))
            length=float(input("Enter the length of the Square :"))
            width=float(input("Enter the width of the Square :"))
            height=float(input("Enter the height of the square :"))
            print("Volume of the square :",(length*width*height))
        elif user_input==4:
            print("The selected shape is  TRIANGLE :")
            breath=float(input("Enter the breath of the triangle :"))
            length=float(input("Enter the length of the triangle :"))
            print("Area of the Triangle :",(1/2*(length*breath)))
            side_1=float(input("Enter the side 1 of the Triangle :"))
            side_2=float(input("Enter the side 2 of the Triangle :"))
            base=float(input("Enter the base of the Triangle :"))
            print("Perimeter of the Triangle :",(side_1+side_2+base))
            base_area=float(input("Enter the base area of the triangle :"))
            height=float(input("Enter the height of the triangle :"))
            print("Volume of the triangle:",(base_area*height))
        elif user_input==5:
            print("The Selected shape is  HEXAGON :")
            side=float(input("Enter the dimension of the hexagon :"))
            print("Area of the Hexagon :",(3*math.sqrt(3)) / (2) * side * side)
            print("Perimeter of the Hexagon :",(6*side))
        elif user_input==6:
            print("The Selected Shape is  PENTAGON :")
            side=float(input("Enter the dimension of the Pentagon :"))
            print("Perimeter of the Pentagon :",(5*side))
        elif user_input==7:
            print("The selected shape is RHOMBUS :")
            diagonal_1=float(input("Enter the dimension 1 of Rhombus :"))
            diagonal_2=float(input("Enter the dimension 2 of Rhombus :"))
            print("Area of the Rhombus :",(diagonal_1*diagonal_2)/2)
            diagonal_3=float(input("Enter the dimesion of the Rhombus :"))
            print("Perimeter of the Rhombus :",(4*diagonal_3))
        else:
            print("Enter the Valid input")
print("1.circle\
      2.Rectangle\
      3.Square\
      4.Triangle\
      5.Hexagon\
      6.Pentagon\
      7.Rhombus")
user_in=float(input("Enter the shape :"))
access=DifferentShapes()
access.display_shape(user_in)
