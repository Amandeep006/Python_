"""Creating and using a class"""
#creating the dog class 
# class Dog:
#     def __init__(self, name, age): #
#         self.name = name # self is a convention used to refer to the instance of the class. It is used to access the attributes and methods of the class.
#         self.age = age

#     def sit(self):  # It is the Instance methods
#         print(f"{self.name} is now sitting")

#     def roll_over(self):
#         print(f"{self.name} rolled over !")

# """Making an instance from a class """
# my_dog= Dog("Tommy",3) # Create an instance of the dog class. The name of the instance is my_dog. The name of the class is Dog. and my_dog is object of the class dog.
# print(f"MY dog's name is {my_dog.name}") # my_dog.name is used to access the name attribute of the my_dog instance. The name attribute is defined in the __init__ method of the Dog class.
# print(f"My dog is {my_dog.age} years old. ")

# """Calling a methods from a class"""
# my_dog.sit()
# my_dog.roll_over()

# """Creating multiple instances of a class"""
# your_dog=Dog("Luccy",5)
# print(f"\n Your dog's names is {your_dog.name}.")
# print(f"Your dog is {your_dog.age} years old.")
# your_dog.sit()
# your_dog.roll_over()

# class Car:
#     def __init__ (self, make="audi", model="A4", year=2024):
#         self.make=make
#         self.model=model
#         self.year=year
#         self.odometer_reading=0

#     def get_descriptive_name(self):
#         long_name= (f"{self.make} {self.model} {self.year}")
#         return long_name.title()
    
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it.")
    
#     def update_odometer(self, mileage):
#         self.odometer_reading=mileage
#         # """Set the odometer reading to the  given value.
#         # Reject the change if it attempts to troll the odometer back."""

#         # if mileage>= self.odometer_reading:
#         #     self.odometer_reading=mileage
#         # else:
#         #     print("You can't roll back an odometer !")

#     def increment_odometer(self, miles):
#         self.odometer_reading +=miles



# my_new_car = Car('audi', 'a4', 2024) # It is the instance of the Car class.
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()

# """Modifying Attribute Values"""
# # we can change the attributes values directly through an instances.

# """1. Modifying an attribute's value directly"""
# my_new_car.odometer_reading=23
# my_new_car.read_odometer()

# """2. Modifying an attribute's value through a method"""
# my_new_car.update_odometer(23)
# my_new_car.read_odometer()

"""3. Incrementing an attribute's Value Through a method"""
# my_used_car=Car("subaru","outback",2019)
# print(my_used_car.get_descriptive_name())

# my_used_car.update_odometer(23500)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()

"""Inheritance """

"""It it the parent class """
# class Car:
#     def __init__(self, make, model, year):
#         self.make=make
#         self.model=model
#         self.year=year
#         self.odometer_reading=0
    
#     def get_descriptive_name(self):
#         long_name=f"{self.year} {self.make} {self.model}"
#         return long_name.title()
    
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it.")

#     def updated_odometer(self, milage):
#         if milage>=self.odometer_reading:
#             self.odometer_reading=milage
#         else:
#             print("You can not roll back on odometer !")

#     def increment_odometer(self, miles):
#         self.odometer_reading +=miles
    

# """It is the chld class """
# class ElectricCar(Car):
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#         self.battery_size=40

#     def describe_battery(self):
#         print(f"This car has a {self.battery_size}--Kwh battery.")

#     def fill_gas_tank(self):
#         print("This car doesn't have a gas tank !")


# my_leaf=ElectricCar("Nissan","Leaf", 2024)
# print(my_leaf.get_descriptive_name())
# my_leaf.describe_battery()
# my_leaf.fill_gas_tank()

# """Instances as attributes """

# class Battery:
#     def __init__(self, battery_size=40):
#         self.battery_size=battery_size

#     def describe_battery(self):
#         print(f"This car has a {self.battery_size}--kwh battery.")

#     def get_range(self):
#         if self.battery_size==40:
#             range=250
#         else:
#             range=225
        
#         print(f"This car can go about {range} miles on a full charge.")

# class ElectricCar(Car):
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#         self.battery=Battery()

# my_leaf=ElectricCar("Nissan", "Leaf", 2024)
# print(my_leaf.get_descriptive_name())
# my_leaf.battery.describe_battery()
# my_leaf.battery.get_range()

"""Generate random numbers using the library of randint() """
from random import randint
print(randint(1,6))

"""Choice function"""
from random import choice
players=["charles", "Martina", "michael", "Florence"]
first_up=choice(players)
print(first_up)