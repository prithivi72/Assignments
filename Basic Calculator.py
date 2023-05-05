def addition(value_1,value_2):
    sum=value_1+value_2
    print(sum)
def subtraction(value_1,value_2):
    Difference=value_1+value_2
    print(Difference)
def multiply(value_1,value_2):
    Multiply=value_1+value_2
    print(multiply)
def division(value_1,value_2):
    divide=value_1+value_2
    print(divide)
    print("Calculator")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiply")
    print("4.Division")
value_1=int(input("Enter the number  :"))
User_input=int(input("Enter the operation done by the user  :"))
value_2=int(input("Enter the number  :"))
if User_input==1:
    value_3=value_1+value_2
    print(value_3)
elif User_input==2:
    value_3=value_1-value_2
    print(value_3)
elif User_input==3:
    value_3=value_1*value_2
    print(value_3)
elif User_input==4:
    value_3=value_1/value_2
    print(value_3)
else:
    print("Enter the valid input")
