#5. Car and ElectricCar class hierarchy

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        return f"{self.year} {self.make} {self.model}"


class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        # Call the constructor of the parent class
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def description(self):
        # Override the parent method
        return f"{super().description()} with a {self.battery_size} kWh battery"

    def battery_details(self):
        return (f"Battery: {self.battery_size} kWh. "
                "Features: approximately 400 km range and 8-hour home charging time.")


# Create an ElectricCar object
my_car = ElectricCar("Tesla", "Model 3", 2024, 75)

print(my_car.description())
print(my_car.battery_details())

#example

#2024 Tesla Model 3 with a 75 kWh battery
#Battery: 75 kWh. Features: approximately 400 km range and 8-hour home charging time.

#Explanation:
#- Car is the base class with make, model, and year.
#- ElectricCar(Car) means that ElectricCar inherits from Car.
#- super().__init__() reuses the constructor from the Car class.
#- ElectricCar adds the battery_size attribute.
#- The description() method is overridden to include battery information.
#- battery_details() provides electric-vehicle-specific information such as range and charging time.