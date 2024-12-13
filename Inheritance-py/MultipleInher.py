#Create a Teacher class with an attribute subject and a 
# method display_subject(). Create another class Mentor 
# with an attribute experience (years) and a method 
# display_experience(). Derive a TeachingAssistant 
# class from both Teacher and Mentor. Implement a 
# method in TeachingAssistant to display all the 
# details together
class Teacher:
    def __init__(self, subject):
        self.subject = subject
    def display_subject(self):
        print(f"Subject: {self.subject}")

class Mentor:
    def __init__(self, experience):
        self.experience = experience
    def display_experience(self):
        print(f"Experience: {self.experience} years")
        
class TeachingAssistant(Teacher, Mentor):
    def __init__(self, subject, experience, role):
        Teacher.__init__(self, subject)
        Mentor.__init__(self, experience)
        self.role = role
    def work(self):
        self.display_subject()
        self.display_experience()
        print(f"Role: {self.role}")

obj = TeachingAssistant("Mathematic", 3, "Teaching Assistant")
obj.work()