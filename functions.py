def mult_by_3(x):
    result = x * 3
    return result

# A function to check whether a student has passed or failed an assignment
def check_pass(grade):
    if grade >= 40 and grade <= 100:
        print("Pass")
    elif grade < 40 and grade >= 0:
        print("Fail")
    else:
        print("Invalid grade")

# Write a function to check whether a number is odd or even
def odd_or_even(x):
    if x % 2 != 0:
        print(str(x)+ " is odd")
    else:
        print(str(x)+ " is even")

odd_or_even(4)
odd_or_even(12435425243)