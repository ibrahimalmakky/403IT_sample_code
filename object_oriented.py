class Student:

    __test_private = 0

    # Constructor method
    # Here we are initialising the values for each new instance of the class
    def __init__(self, first_name, surename, age):
        # Remember to add modules and grades
        self.first_name = first_name
        self.surename = surename
        self.age = age
        self.modules = []
        self.grades = []

    def over_21(self):
        if self.age >= 21:
            print("The student is 21 or over")
        else:
            print("The student in under 21")

    def enrol_on_module(self, module_name):
        self.modules.append(module_name)
        self.grades.append(0)

    def add_grade(self, module, module_grade):
        module_index = self.modules.index(module)
        self.grades[module_index] = module_grade

    def check_if_pass(self, module_name):
        module_index = self.modules.index(module_name)
        grade = self.grades[module_index]
        if grade >= 40:
            print(self.first_name+" has passed the module " + module_name)
        else:
            print(self.first_name+" has failed the module "+ module_name)


student1 = Student("Herbert", "Moore", 25)
student2 = Student("Weronika", "Litwin", 20)

student1.enrol_on_module("403IT")
student2.enrol_on_module("404IT")

student1.add_grade("403IT", 20)
student2.add_grade("404IT", 85)

student1.check_if_pass("403IT")
student2.check_if_pass("404IT")
