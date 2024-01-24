'''
Example of Inheritance
TV class
TVClass - Base class or parent class
Child classes:
LedTV class
PlasmaTV class
'''


#def - keyword to create function
'''__init__ also called as constructor,
it will be automatically called when object or instance of class is created.
Here plasma_tv= plasma() is an instance which makes use of values and methods
present inside constructor of plasma.
'''
#self - refers created instance of a class and uses its values as well
#Volume and Channel set to default value in parent class constructor and can be accessed across child classes
#f - used for formatting string
class TV:
    def __init__(self, brand, channel=1, volume=50):
        self.brand = brand
        self.channel = channel
        self.volume = volume

    def increase_volume(self):
            self.volume = self.volume + 10
            print(f"{self.brand} TV: Volume increased to {self.volume}")

    def decrease_volume(self):
            self.volume = self.volume - 10
            print(f"{self.brand} TV: Volume decreased to {self.volume}")

'''
super().__init__(brand) --with the help of super() we can initialize brand properties
that are present in base class and can use it for our child class
'''

class Plasma(TV):
    def __init__(self, brand, thickness, lifespan, display):
        super().__init__(brand)
        self.thickness = thickness
        self.lifespan = lifespan
        self.display = display

class LED(TV):
    def __init__(self, brand, thickness, lifespan, display):
        super().__init__(brand)
        self.thickness = thickness
        self.lifespan = lifespan
        self.display = display

#Creating instance of child plasma class and LED class by provided parameter name and its value
plasma_tv = Plasma(brand="Samsung", thickness="2 inches", lifespan="8 years", display="Full HD")
led_tv = LED(brand="Sony", thickness="1 inch", lifespan="10 years", display="4K")

print("Plasma TV Details:")
#f - used for formatting string
print(f"Brand: {plasma_tv.brand}")
print(f"Thickness: {plasma_tv.thickness}")
print(f"Lifespan: {plasma_tv.lifespan}")
print(f"Display: {plasma_tv.display}")
print(f"Default Volume of TV:{plasma_tv.volume}")
# Accessing parent class methods using dot(.) key -- instance.method()
#Here method decrease.volume() of parent class is directly inherited in child class
plasma_tv.decrease_volume()

print("\nLED TV Details:")
#f - used for formatting string
print(f"Brand: {led_tv.brand}")
print(f"Thickness: {led_tv.thickness}")
print(f"Lifespan: {led_tv.lifespan}")
print(f"Display: {led_tv.display}")
print(f"Default Volume of TV:{led_tv.volume}")
# Accessing parent class methods using dot(.) key -- instance.method()
#Here method increase.volume() of parent class is directly inherited in child class
plasma_tv.increase_volume()