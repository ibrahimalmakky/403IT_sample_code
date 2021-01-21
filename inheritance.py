# Parent Class (Also called Super class)
class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def over_18(self):
        if self.age >= 18:
            print("The student is 18 or over")
        else:
            print("The student in under 18")

# Child class
class Student(Person):
    
    def __init__(self, first_name, last_name, age, course):
        super().__init__(first_name, last_name, age)
        self.course = course
        self.modules = {}

    def add_module(self, module_code, module_name):
        self.modules[module_code] = module_name

# Creating an instance of the parent class
mike = Person("Mike", "Anderson", 50)

# Creating an instance of the child class
student = Student("Ibrahim", "Smith", 56, "Cyber Security")
print(student.course)
print(student.first_name)
student.add_module("403IT", "Problem Solving and Programming")
# Use functions from the parent class (CODE REUSABILTIY RIGHT HERE :))
student.over_18()