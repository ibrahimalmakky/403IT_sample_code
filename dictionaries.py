class Course:

    def __init__(self, name):
        self.course_name = name
        self.modules = {}
    
    def add_module(self, module_code, module_name):
        self.modules[module_code] = module_name

my_list = ["Hello", "403IT", "Mike"]

my_dict = {"greeting": "Hello", "module": "403IT", "name": "mike"}
my_other_dict = {1: "test1", 7:"test2"}

# Looping through a dictionary
for key, value in my_dict.items():
    print(key, value)

# print(my_dict.values())

# Adding a key-value pair to an existing dictionary
words = {"greetings":["Hello", "Welcome", "Good morning", "Good afternoon"], 
         "names": ["Herbert", "Weronika", "Kasia"]}
words["test"] = ["new", "array"]

# Using a dictionary in a class
course = Course("Cyber Security")
course.add_module("403IT", "Problem Solving and Programming")
course.add_module("400IT", "Network Fundementals")
print(course.modules)

