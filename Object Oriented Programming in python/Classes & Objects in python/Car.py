# Car class should have the following attributes & methods
#
# Attributes:
#   color, max_speed, acceleration, tyre_friction
#


# Implement the Car class appropriately
class Car:
    def __init__(self, color, max_speed, acceleration, tyre_friction):
        self.color=color
        self.max_speed=max_speed
        self.acceleration=acceleration
        self.tyre_friction=tyre_friction
# You need not change any code below.
# Do not call this function anywhere. It will automatically be called internally during tests.
def default_test():
    car = Car(color="Red", max_speed=250, acceleration=10, tyre_friction=3)
    print(car.color)
    print(car.max_speed)
    print(car.acceleration)
    print(car.tyre_friction)

'''
Question: Car
In this coding question, you are given an incomplete Car class. Your task is to implement the Car class with the described attributes and methods. The attributes are color, max_speed, acceleration, and tyre_friction.

Approach
To solve this problem, we will follow these steps:

Understand the Car class and its attributes.
Define the Car class.
Implement the __init__ method to initialize the attributes.
Step-by-Step Explanation
Step 1: Understand the Car class

Before we start coding, let's understand the Car class and its attributes:

color: The color of the car.
max_speed: The maximum speed the car can reach.
acceleration: The rate at which the car can increase its speed.
tyre_friction: The friction between the car's tires and the road.
Step 2: Define the Car class

Now that we understand the Car class and its attributes, let's define the class in Python:

PYTHON
Step 3: Implement the init method

Inside the Car class, we need to implement the __init__ method to initialize the attributes. The __init__ method is a special method in Python classes that is called when an object is created.

PYTHON
In the __init__ method, we take the values of color, max_speed, acceleration, and tyre_friction as arguments and assign them to the corresponding attributes using self.

'''