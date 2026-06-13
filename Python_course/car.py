class Car:
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    
    def get_descriptive_name(self):
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def updated_odometer(self, milage):
        if milage>=self.odometer_reading:
            self.odometer_reading=milage
        else:
            print("You can not roll back on odometer !")

    def increment_odometer(self, miles):
        self.odometer_reading +=miles



class Battery:
    def __init__(self, battery_size=40):
        self.battery_size=battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}--kwh battery.")

    def get_range(self):
        if self.battery_size==40:
            range=250
        else:
            range=225
        
        print(f"This car can go about {range} miles on a full charge.")
    

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery=Battery()

    # def describe_battery(self):
    #     print(f"This car has a {self.battery_size}--Kwh battery.")

    # def fill_gas_tank(self):
    #     print("This car doesn't have a gas tank !")


my_leaf=ElectricCar("Nissan","Leaf", 2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()
my_leaf.fill_gas_tank()
