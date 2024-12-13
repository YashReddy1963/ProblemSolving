# Create a Base class that has a method message() which prints 
# "This is the base class". Create a Derived class that 
# overrides this method to print "This is the derived class". 
# Demonstrate calling the message() method from both the Base 
# and Derived classes, and also explicitly call the parent 
# class's message() method from the overridden method

class Base:
    def message(self):
        print("This is a base class")

class Derived(Base):
    def message(self):
        super().message()
        print("This is derived class")

obj1 = Base()
print("Calling using Base class object:")
obj1.message()

obj2 = Derived()
print("Calling using derived class object:")
obj2.message()