class Triangle:

    def __init__(self):
        self.user_input()
    
    def calc_area(self):
        return ((self.b * self.h)/2)
    
    def calc_per(self):
        return (self.a + self.b + self.c)

    def user_input(self):
        self.a = int(input("Please enter the length for side a \n"))
        self.c = int(input("Please enter the length for side c \n"))
        self.b = int(input("Please enter the length for the base side \n"))
        self.h = int(input("Please enter the height of the triangle \n"))
        self.area = self.calc_area()
        self.per = self.calc_per()
    
my_traingle = Triangle()
print(my_traingle.area)
print(my_traingle.per)