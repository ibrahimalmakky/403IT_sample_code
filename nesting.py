# Nesting conditional statements
# password = input("Please enter your password")
password = "test"
if len(password) > 8:
    print("The length of the password is acceptable")
else:
    if len(password) < 1:
        print("You have not entered a password")
    else:
        print("Your password length is not acceptable")

# Nesting Loops
greetings = ["Hello ", "Welcome ", "Good morning "]
names = ["Weronika", "Herbert", "Kasia"]
i = 0
while i < len(names):
    for greeting in greetings:
        # print(greeting + names[i])
        pass
    i += 1

# Write code (using nested loops) to output the multiplication tables for numbers between 2 and 9
# Outer loop to go through the numbers for which multiplication tables are to be generated
for i in range(2, 10): # 8 different numbers (n)
    # print("--------------------")
    # Inner loop to go through numbers between 1 and 10
    for j in range(1, 10): # 9 different numbers (m)
        # print(str(i)+" x "+str(j)+"= "+str(i*j))
        pass


# Nested lists (a list of lists) for the modules of the Cyber Security Course
modules = [["400IT", "401IT", "403IT", "402IT"],
           ["500IT", "501IT", "503IT", "502IT"],
           ["600IT", "601IT", "603IT", "602IT"]]
for year_modules in modules:
    # print("Year 1:")
    for year_module in year_modules:
        # print(year_module)
        pass
    # print("----------------------")


# Store multiplication tables in a multi-dimensional list
mult_tables = []
for i in range(2, 10): 
    mult_table = []
    for j in range(1, 10): 
        mult_table.append(i*j)
    mult_tables.append(mult_table)
print(mult_tables)
