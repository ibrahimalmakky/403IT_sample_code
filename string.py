my_string = "Hello World"

print(my_string[6:len(my_string)])

user_string = input("Please enter a string to reverse.")
# Extended slicing approach
print(user_string[::-1])
# For loop approach
reversed_string = ""
for char in range(len(user_string)-1, -1, -1):
    reversed_string += user_string[char]
print(reversed_string)