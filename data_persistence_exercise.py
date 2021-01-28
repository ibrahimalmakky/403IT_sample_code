
list_of_nums = []
while True:
    user_inp = input("Please enter a number to be added to the file. To finish press f")
    if user_inp == "f":
        break
    try:
        num = int(user_inp)
        list_of_nums.append(num)
    except:
        print("Invalid input, please make sure to enter a number.")
print(list_of_nums)

my_file = open("numbers.txt", "w")
for num in list_of_nums:
    my_file.write(str(num))
    my_file.write("\n")
my_file.close()
