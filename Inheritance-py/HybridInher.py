# Create a Device class with an attribute device_name. 
# Create a Laptop class and a Tablet class that inherit 
# from Device, adding their respective unique attributes 
# (ram for Laptop and battery_life for Tablet). Create a 
# HybridDevice class that inherits from both Laptop and 
# Tablet to represent a hybrid laptop-tablet device. 
# Implement methods to display details of the hybrid device

class Device:
    def __init__(self, device_name):
        self.device_name = device_name
    
class Laptop(Device):
    def __init__(self, ram):
        self.ram = ram

class Tablet(Device):
    def __init__(self, device_name, battery_life):
        super().__init__(device_name)
        self.battery_life = battery_life
    
class HybridDevice(Laptop, Tablet):
    def __init__(self, device_name, ram, battery_life):
        Laptop.__init__(self,ram)
        Tablet.__init__(self,device_name, battery_life)
    def info(self):
        print(f"Device Name: {self.device_name}")
        print(f"RAM: {self.ram}GB")
        print(f"Battery Life: {self.battery_life} hours")

obj = HybridDevice("Surface Pro",16,10)
obj.info()