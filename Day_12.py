'''OOP Excercise'''
# OOP Exercise 1: Create a Class with instance attributes
# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes
class Vehicle:
    '''
    Vehicle class
    '''
    def __init__(self,max_speed,mileage) -> None:
        self.max_speed = max_speed
        self.mileage = mileage

    def __str__(self) -> str:
        return f'Max Speed: {self.max_speed} m/s, Mileage: {self.mileage} km'   
    def __repr__(self) -> str:
        return "vehicle()"

obj = Vehicle(2,4)
print(repr(obj))

# --------------------------------------------------------
# Exercise 2: Create a Vehicle class without any variables and methods
class Vehicle:
    '''
    Vehicle class
    '''
    pass
# --------------------------------------------------------
# Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class Vehicle:
    '''
    Vehicle class
    '''
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class Bus(Vehicle):
    '''
    Bus class
    '''
    def __str__(self) -> str:
        return f"Vehicle Name: {self.name} Volvo Speed: {self.max_speed} Mileage: {self.mileage}"

obj =Bus("PIA",123,44)
print(obj)

# --------------------------------------------------------
# Exercise 4: Class Inheritance
class Vehicle:
    '''
    Vehicle class
    '''
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        '''seating capacity'''
        return f"The seating capacity of a {self.name} is {capacity} passengers"
class Bus(Vehicle):
    '''
    Bus class
    '''
    def seating_capacity(self, capacity=50):
        '''Bus seating_capacity function'''
        return super().seating_capacity(capacity=50)
school_bus = Bus("Bus", 180, 12)

print(school_bus.seating_capacity())
# --------------------------------------------------------
