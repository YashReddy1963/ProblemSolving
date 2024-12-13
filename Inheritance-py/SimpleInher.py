#Create a Person class with attributes like name and age, 
# and a method display_details() to print them. Derive a 
# Student class from Person that adds an attribute grade 
# and a method display_student_details() to print all details 
# including the grade

class Person: 
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
    def display_student_details(self):
        std.display_details()
        print(f"Grade: {self.grade}")

std = Student("Yash", 19, 89)
std.display_student_details()