#assign pnr, admit, assign department, assign courses..
#list of all pnr be kept to track
#pass the data only once when creating the object
#name, surname, phonenumber, city, pincode

import random

li = []
class Student:
    def __init__(self, data, n):

        for i in range(1,n+1):
            self.name = data[i][0]
            self.surname = data[i][1]
            self.phonenum = data[i][2]
            self.city = data[i][3]
            self.year = data[i][4]
            self.caste = data[i][5]
            self.result = self.generate_pnr()
            self.pnr = str(data[i][4]) + data[i][5] + str(self.result)
            data.setdefault(i,[]).append(self.pnr)
            li.append(self.pnr)
            self.admit(data, i)
            

    def generate_pnr(self):
        start = pow(10, 5)
        end = pow(10,6) - 1
        pnr = random.randint(start, end)
        if pnr not in li:
            return pnr
        else:
            self.generate_pnr()

    def admit(self, data, i):
        print(f"For {data[i][0]} the addmission is confirmed!!")
        for j in range(0,7):
            print(data[i][j])
        self.assign_depart(data, i)
    
    def assign_depart(self, data, i):
        print("1.CSE \n2.ENTC \n3.Mech \n4.Civil \n")
        ch = int(input("Choose your departmen: \n"))
        if ch == 1:
            print("Your department is CSE \n")
            data.setdefault(i,[]).append("CSE")
        elif ch == 2:
            print("Your department is ENTC \n")
            data.setdefault(i,[]).append("ENTC")
        elif ch == 3:
            print("Your department is Mech. \n")
            data.setdefault(i,[]).append("Mech")
        elif ch==4:
            print("Your department is Civil \n")
            data.setdefault(i,[]).append("Civil")
        self.assign_courses(data, i)
        

    def assign_courses(self, data, i):
        print("1.Maths \n2.Physics \n3.Chemistry \n")
        ch = int(input("Choose your course: \n"))
        if ch==1:
            print("Your subject is Maths\n")
            data.setdefault(i,[]).append("Maths")
        elif ch == 2:
            print("Your subject is Physics\n")
            data.setdefault(i,[]).append("Physics")
        elif ch==3:
            print("Your subject is Chemistry \n")
            data.setdefault(i,[]).append("Chemistry")



num = int(input("Enter number of students: \n"))
stud_dict = {}
for i in range(1,num+1):
    name=input("Enter the name: \n")
    surname=input("Enter your surname: \n")
    phonenumber=int(input("Enter your phone No.: \n"))
    city=input("Enter your city: \n")
    year=int(input("Enter the year of addmission: \n"))
    caste = input("Enter your caste: \n")
    stud_dict.setdefault(i, [name, surname, phonenumber, city, year, caste])

obj = Student(stud_dict, num)
print(f"List of generated pnr: {li}")
