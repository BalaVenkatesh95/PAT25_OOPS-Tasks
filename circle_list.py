'''
Create a class with constructor that take arguments
(Using Area of circle as example here)
'''

#import - helps to bring specific function or variable to current script
import math
#def - keyword to create function
'''__init__ also called as constructor,
it will be automatically called when object or instance of class is created.
Here circle_instance = Circle(10) is an instance which makes use of values and methods  
present inside constructor.
'''
#self - refers created instance of a class(here circle_calculation is instance) and uses values

class Circle:
    def __init__(self, radius):
        self.radius = radius
#instance methods that can be accessed
#Using for loop to iterate list
    def calculate_area(self):
        return [math.pi * r**2 for r in self.radius]

# Creating an instance and accessing methods
radius_list = [10, 501, 22, 37, 100, 999, 87, 351]
circle_calculation = Circle(radius_list)
# Accessing class methods using dot(.) key -- instance.method()
area_calculation = circle_calculation.calculate_area()
print("Area of Circle:", area_calculation)