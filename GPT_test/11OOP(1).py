# 1️⃣ Create a Student class with class variables and instance variables, create two objects, and show how changing a class variable affects both.

class Students:
    uni = "VTU"
    course = "AIML"
    def __init__(self, name, gpa):
        self.name = name 
        self.cgpa = gpa

s1 = Students("Sony", 8.3)
s2 = Students("Preetham", 8.6)
print(f"Name: {s1.name}\nUniversity: {s1.uni}\nCourse: {s1.course}\nCGPA: {s1.cgpa}", f"Name: {s2.name}\nUniversity: {s2.uni}\nCourse: {s2.course}\nCGPA: {s2.cgpa}", sep = "\n\n")

# 2️⃣ Create a Student class with constructor and a method that returns Pass/Fail based on marks, then test it with two objects.
class Students:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def res(self, marks):
        if(marks >= 40):
            return "pass"
        else:
            return "fail"

s1 = Students("Sony", 32)
s2 = Students("Sangeeta", 78)
print(f'Name: {s1.name}\nresult: {s1.res(s1.marks)}\n\nName:{s2.name}\nReult: {s2.res(s2.marks)}')


# 3️⃣ Create a class whose constructor prints a message and explain (in comment) why it prints once per object created.
class demo:
    def __init__(self):
        print("object created") # gets printed everytime an obj created

o1 = demo()
o2 = demo()
o3 = demo()
o1 = demo() # Now also the message executes cause the object here is recreated (may be)

# again → old object reference is lost, a new object is created, so constructor runs again