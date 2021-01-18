# Get the user input
name = input("Can you please enter your name?")
# Greet the user
print("Hello "+name)
print("Welcome to this two number addition program")
num1 = input("Please enter the value for your first number\n")
# Cast string input to integer
num1 = int(num1)
num2 = input("Please enter the value for your second number\n")
num2 = int(num2)
# Add the numbers together
my_sum = num1 + num2
print(my_sum)

# Comparison operators
# equal to ==
# Not equal !=
# Greater than >
# Less than <
# Greater than or equal to >=
# Less than or equal to <=
if my_sum >= 0:
    print("Sum is a positive number")
else:
    print("Sum is a negative number")
