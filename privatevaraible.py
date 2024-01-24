'''
Create proper member variable inside class and use them
when necessary.
For Example,create a private variable named pi=3.141
'''

'''__init__ also called as constructor,
it will be automatically called when object or instance of class is created.
Here circle_instance = Circle(10) is an instance which makes use of values and methods  
present inside constructor.
'''
#def - keyword to create function
#__pi - to declare variable as private, double underscore should be prefixed
#self - refers created instance of a class(here circle_calculation is instance) and uses values
class Circle:
    def __init__(self, radius):
        self.__pi = 3.141
        self.radius = radius

    def calculate_area(self):
        return self.__pi * self.radius**2
#if __name__ == '__main__': interpreter jumps directly into this line and executes based on provided
if __name__ == '__main__':
# Creating an instance and accessing methods
 circle_calculation = Circle(10)
# Accessing class methods using dot(.) key -- instance.method()
 area = circle_calculation.calculate_area()
 print("Given Radius of circle:", circle_calculation.radius)
 print("Area of Circle:", area)