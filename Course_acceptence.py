# Get the input for the IELTS certificate
def get_IELTS():
    # EOFError (Sorted)
    try:
        A = input("Do you have an IELTS certificate?")
    except:
        print("Please do not enter the end of line to your input.")
        get_IELTS()
    # Possible logical error if the user enters a value other than yes and Yes
    A = A.lower()
    if A == "yes":
        A = True
    elif A == "no":
        A = False
    else:
        print("Undefined input. Please make sure that you answer with yes or no.")
        get_IELTS()
    return A

A = get_IELTS()
# EOFError
B = input("Do you have a TOFEL certificate?")
# Possible logical error if the user enters a value other than yes and Yes
if B == "yes" or A == "Yes":
    B = True
else:
    B = False

# Create a function to get a valid input for the Maths grade from the user

# EOFError
C = input("What is your Maths grade?")
# Possible conversion error when user inputs non numerical value
try:
    C = int(C)
except:
    print("Please make sure that you enter a numerical value.")
    exit()
# Possible logical error here when the user enters grades beyond the 0->100 range
if C >= 80:
    C = True
else:
    C = False
# EOFError
D = input("What is your IT grade?")
# Possible conversion error when user inputs non numerical value
D = int(D)
# Possible logical error here when the user enters grades beyond the 0->100 range
if D >= 80:
    D = True
else:
    D = False

Y = (A or B) and (C and D)
if Y:
    print("You have been accepted on the course.")
else:
    print("You have not been accepted on the course.")
