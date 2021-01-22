class Course:

    def __init__(self, name):
        self.course_name = name
        self.modules = {}
    
    def add_module(self, module_code, module_name):
        self.modules[module_code] = module_name

class Library:

    def __init__(self, name):
        self.name = name
        self.books = {}

    def add_book(self, location, title, genre, author, year):
        book_details = {}
        book_details["title"] = title
        book_details["genre"] = genre
        book_details["author"] = author
        book_details["year"] = year
        self.books[location] = book_details

    # Returns the location of the book if the book is in the library else it
    # return None
    def find_book(self, title):
        # Iterate through the key, value pairs in the books dictionary
        for location, book in self.books.items():
            # Check if the book title is equal to the searched title
            if book["title"] ==  title:
                # Return the location of the book
                return location
        return None

my_library = Library("Coventry")
my_library.add_book("SE987", "Software Engineering", "Software", "Ian Sommerville", 2015)
print(my_library.find_book("Software Engineering"))
print(my_library.find_book("Design for Usability"))


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

