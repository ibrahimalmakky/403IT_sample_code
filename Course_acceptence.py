# Get the input for the IELTS certificate
A = input("Do you have an IELTS certificate?")
if A == "yes" or A == "Yes":
    A = True
else:
    A = False
B = input("Do you have a TOFEL certificate?")
if B == "yes" or A == "Yes":
    B = True
else:
    B = False
C = input("What is your Maths grade?")
C = int(C)
if C >= 80:
    C = True
else:
    C = False
D = input("What is your IT grade?")
D = int(D)
if D >= 80:
    D = True
else:
    D = False

Y = (A or B) and (C and D)
if Y:
    print("You have been accepted on the course.")
else:
    print("You have not been accepted on the course.")
