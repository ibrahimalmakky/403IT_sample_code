G=input("What  grade did you get for your assignment?\n")
G = int(G)
if G >= 70 and G <= 100:
    print("You have passed the assignment with first class grade.")
elif G <70 and G >=60:
    print("You have passed the assignment with 2-1 grade.")
elif G <60 and G >=50:
    print("You have passed the assignment with 2-2 grade.")
elif G <50 and G >=40:
    print("You have passed the assignment")
elif G <40 and G >= 0:
     print("You have failed the assignment.")
else:
    print("You have entered an invalid grade.")
