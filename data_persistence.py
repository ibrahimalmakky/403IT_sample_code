# We want to use the functions that we have declared in the recursion.py file
import recursion


# Writing data to a file
my_file = open("test.txt", "w")
my_file.write("This is some file content. Hello 403IT :D")
my_file.close()

my_file = open("test.txt", "r")
my_string = my_file.read()
print(my_string)

# Write a limited part of Fibonacci sequence into a file called "Fibonacci.txt"
fib_list = recursion.fibonacci(0,1,100)
print(fib_list)
my_file = open("Fibonacci.txt", "w")
for num in fib_list:
    my_file.write(str(num))
    my_file.write("\n")
my_file.close()
