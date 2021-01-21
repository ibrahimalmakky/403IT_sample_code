
numbers = []

while True:
    inp = input("Please enter the next number of the sequence. To finish enter y \n")
    if inp == "y" and len(numbers) >= 3:
        break
    elif inp == "y" and len(numbers) < 3:
        print("Please enter at least three numbers in the sequence")
    else:
        numbers.append(int(inp))

fibonacci = True
for i in range(2, len(numbers)):
    if numbers[i] == numbers[i-1] + numbers[i-2]:
        pass
    else:
        fibonacci = False
        break

if fibonacci:
    print(numbers, " is a Fibonacci sequence.")
else:
    print(numbers, " is not a Fibonacci sequence.")


