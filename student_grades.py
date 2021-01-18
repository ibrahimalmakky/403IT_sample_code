# Get grade input from user and case it into an integer
grade = input("What is your grade on the assignment?")
grade = int(grade)

if grade >= 40 and grade <= 100:
    print("Congratulations! You have passed the assignment.")
elif grade < 40 and grade >= 0:
    print("Sorry about that, but you have failed your assignment.")
else:
    print("You have enetered an invalid grade.")
