'''Calculate the area of a circle'''

#prompt the user to enter the radius



def calculate_circle_area(radius):
    from math import pi
    area = pi * radius **2
    return area

try:
    radius = float(input("Enter the radius of the circle "))
    area = calculate_circle_area(radius)
    print ( f"The area of the circle is {area}")
except:
    print("please enter a valid number for the radius")

