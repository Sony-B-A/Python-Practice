# Q1 — Class vs Instance Attribute (Thinking test)
class student:
    college = "abc"
    def __init__(self, name, cgpa, clg):
        self.name = name
        self.gpa = cgpa
        self.college = clg

o1 = student("a", 8.9, "xyz")
o2 = student("b", 9, "xyz")
print(student.college)
print(o1.college)
print(o2.college)

# Q2 — Constructor & Object Creation
# 👉 How many times is the message printed and why?
class counter:
    def __init__(self):
        print("constructor created")
o1 = counter()
o2 = counter()
o3 = counter()
o1 = counter() # I didn't get this perticular topic
# Every time a new object created the constructor runs
"""
Q3 — Instance Method vs Class Method
Create a class Laptop with:
class attribute storage_type
instance attributes ram, price
instance method show_details()
class method change_storage_type()
👉 Call the class method using:
class name
object name
Print results and observe what changes."""

class laptop:
    storage_type = "SSD"
    def __init__(self, ram, price):
        self.price = price
        self.ram = ram
    def show_details(self):
        print(f"Laptop details\nPrice: {self.price}\nStorage type: {self.storage_type}\nRAM: {self.ram}")
    @classmethod
    def change_storage_type(cls):
        cls.storage_type = "HDD"
    

obj = laptop("512GB", 53_000)
obj.show_details()
"""
Laptop details
Price: 53000
Storage type: SSD
RAM: 512GB
"""
laptop.change_storage_type()
obj.show_details()
"""
Laptop details
Price: 53000
Storage type: HDD
RAM: 512GB
"""

obj.change_storage_type()
obj.show_details()

class shop:
    @staticmethod
    def calc_discount(price, discount):
        discounted_price = price - (price * discount / 100)
        print(f"Dicounted price = {discounted_price}")

obj = shop()
obj.calc_discount(200, 10)
shop.calc_discount(14000, 10)
# Self is not needed bcz static method doesn,t belong to class or object
# but it's logic is belong to the behavior of class
# it doesn't take any class or instance attributes 


# 👉 Explain why everything in Python is an object (1–2 lines).
# I don't know answer for this

"""Q7 — Mix It All (Mini challenge)
Create a class Employee with:
class attribute company
constructor → name, salary
instance method → returns yearly salary
class method → change company name
static method → check if salary > 50,000
👉 Create 2 objects and test all methods."""

class Employee:
    company = "xyz"
    def __init__(self, name, sal):
        self.name = name
        self.salary = sal
    def yearly_salary(self):
        return self.salary * 12
    @classmethod
    def change_company(cls):
        company = "abc"
        print("Changed company name")

    @staticmethod
    def check(salary):
        if(salary > 50000):
            return True
        else:
            return False


o1 = Employee("Sony", 58000)
o2 = Employee("Sangeeta", 30000)
print(f"Yearly Salary of {o1.name}: {o1.yearly_salary()}")
o1.change_company()
print(o1.company)
print(f"Is salary greater than 50,000; {o1.check(o1.salary)}")

print(f"Yearly Salary of {o2.name}: {o2.yearly_salary()}")
o2.change_company()
print(o2.company)
print(Employee.company)
print(f"Is salary greater than 50,000; {o2.check(o2.salary)}")
print(o2.company)