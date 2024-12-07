#assign pnr, admit, assign department, assign courses..
#list of all pnr be kept to track
#pass the data only once when creating the object
#name, surname, phonenumber, city, pincode

import random

li = []
class Student:
    def __init__(self, data):
        self.name = data[0]
        self.surname = data[1]
        self.phonenum = data[2]
        self.city = data[3]
        self.year = data[4]
        self.caste = data[5]
        self.result = self.generate_pnr()
        self.pnr = str(data[4]) + data[5] + str(self.result)
        data.append(self.pnr)
        li.append(self.pnr)
        self.admit(data)
            

    def generate_pnr(self):
        start = pow(10, 5)
        end = pow(10,6) - 1
        pnr = random.randint(start, end)
        if pnr not in li:
            return pnr
        else:
            self.generate_pnr()

    def admit(self, data):
        print(f"For {data[0]} the addmission is confirmed!!")
        print(f"Details: {data}")
        self.assign_depart()
    
    def assign_depart(self):
        print("1.CSE \n2.ENTC \n3.Mech \n4.Civil \n")
        ch = int(input("Choose your departmen: \n"))
        if ch == 1:
            print("Your department is CSE \n")
        elif ch == 2:
            print("Your department is ENTC \n")
        elif ch == 3:
            print("Your department is Mech. \n")
        elif ch==4:
            print("Your department is Civil \n")
        self.assign_courses()
        

    def assign_courses(self):
        print("1.Maths \n2.Physics \n3.Chemistry \n")
        ch = int(input("Choose your course: \n"))
        if ch==1:
            print("Your subject is Maths\n")
        elif ch == 2:
            print("Your subject is Physics\n")
        elif ch==3:
            print("Your subject is Chemistry \n")



print("You can enter upto 2 students details: \n")
totalStud=2
stud_dict = {}
for i in range(1,totalStud+1):
    name=input("Enter the name: \n")
    surname=input("Enter your surname: \n")
    phonenumber=int(input("Enter your phone No.: \n"))
    city=input("Enter your city: \n")
    year=int(input("Enter the year of addmission: \n"))
    caste = input("Enter your caste: \n")
    stud_dict.setdefault(i, [name, surname, phonenumber, city, year, caste])

obj1 = Student(stud_dict[1])
obj2 = Student(stud_dict[2])
print(f"List of generated pnr: {li}")
