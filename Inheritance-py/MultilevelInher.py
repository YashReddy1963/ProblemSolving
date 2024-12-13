# Create a Vehicle class with an attribute make and a method 
# display_make(). Derive a Car class that adds an attribute 
# model and a method display_model(). Finally, derive an 
# ElectricCar class that adds an attribute battery_capacity 
# and a method display_car_details() to show all details

class Vehicle:
    def __init__(self, make):
        self.make = make
    def display_make(self):
        print(f"Make: {self.make}")

class Car(Vehicle):
    def __init__(self, make, model):
        super().__init__(make)
        self.model = model
    def display_model(self):
        self.display_make()
        print(f"Model: {self.model}")

class ElectricCar(Car):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)
        self.battery_capacity = battery_capacity
    def display_car_details(self):
        self.display_model()
        print(f"Batter Capacity: {self.battery_capacity} kWh")

car = ElectricCar("Tesla", "Model S", 100)
car.display_car_details()