'''import the math  library'''
import math
class DifferentShapes():
    '''display_shape using as function.self is used to call the class inside the function'''
    def display_shape(self, user_input):
        ''' user_input is used to get the value from the user'''
        if user_input==1:
            radius=float(input("Enter the radius :"))
            print("Area  :",radius*radius*3.14)
            print("Perimeter :" ,(2*radius*3.14))
        elif user_input==2:
            length=float(input("Enter the length  :"))
            width=float(input("Enter the width   :"))
            print("Area  :",(length*width))
            print("Perimeter  :",(2*(length*width)))
            length=float(input("Enter the length  :"))
            width=float(input("Enter the width :"))
            height=float(input("Enter the height  :"))
            print("Volume :",(length*width*height))
        elif user_input==3:
            side=float(input("Enter the dimension  :"))
            print("Area  :",(side*side))
            print("Perimeter  :",(4*side))
            length=float(input("Enter the length  :"))
            width=float(input("Enter the width  :"))
            height=float(input("Enter the height  :"))
            print("Volume  :",(length*width*height))
        elif user_input==4:
            breath=float(input("Enter the breath :"))
            length=float(input("Enter the length :"))
            print("Area of the Triangle :",(1/2*(length*breath)))
            side_1=float(input("Enter the side 1  :"))
            side_2=float(input("Enter the side 2  :"))
            base=float(input("Enter the base  :"))
            print("Perimeter  :",(side_1+side_2+base))
            base_area=float(input("Enter the base  :"))
            height=float(input("Enter the  :"))
            print("Volume :",(base_area*height))
        else:
            print("Enter the Valid input")
print("1.circle\
      2.Rectangle\
      3.Square\
      4.Triangle")
user_in=float(input("Enter the shape :"))
access=DifferentShapes()
access.display_shape(user_in)