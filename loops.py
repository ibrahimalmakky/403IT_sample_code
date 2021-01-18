# Init
i = 0
# Termination condition
while i < 10:
    # The increment
    # Shortcut to i = i + 1
    i += 4
    if i == 5:
        continue
    print(i)
else:
    print("i is not greater than 10")
    
# For Loop
for i in range(0, 10, 4):
    print(i)
else:
    print("The for loop is now finished")

