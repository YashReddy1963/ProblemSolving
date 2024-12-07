import random

li = []
class Employee:
    def __init__(self, data):
        self.name = data[0]
        self.age = data[1]
        self.designation = data[2]
        self.year = data[3]
        self.id = self.generate_empid()
        self.emp_id = str(data[3]) + str(self.id)
        data.append(self.emp_id)
        li.append(self.emp_id)
        self.admit(data)
            

    def generate_empid(self):
        start = pow(10, 5)
        end = pow(10,6) - 1
        pnr = random.randint(start, end)
        if pnr not in li:
            return pnr
        else:
            self.generate_pnr()

    def admit(self, data):
        print(f"Data of {data[0]} is saved!!")
        print(f"Details: {data}")
        self.assign_project()
    
    def assign_project(self):
        print("1.ProjectAlpha \n2.ProjectBeta \n")
        ch = int(input("Choose your Project: \n"))
        if ch == 1:
            print("Your Project is ProjectAlpha \n")
        elif ch == 2:
            print("Your Project is ProjectBeta \n")



print("You can enter data upto 2 employees only: \n")
totalEmp=2
emp_dict = {}
for i in range(1,totalEmp+1):
    name=input("Enter the name: \n")
    age=int(input("Enter the age: \n"))
    designation=input("Enter your designation: \n")
    year=int(input("Enter the year of joining: \n"))
    emp_dict.setdefault(i, [name, age, designation, year,])

obj1 = Employee(emp_dict[1])
obj2 = Employee(emp_dict[2])
print(f"List of generated emp_id: {li}")