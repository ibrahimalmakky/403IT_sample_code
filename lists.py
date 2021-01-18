# Lists
numbers = [1, 2, 6, 8, 0]
words = ["Hello", "There", "It", "is", "nice", "to", "meet", "you"]
nums_and_strings = [1, 5, "Hello", 7]

i = 0
while i < len(numbers):
    print("numbers["+str(i)+ "]:" + str(numbers[i]))
    i += 1  
else:
    print("The numbers array is now over")

# Print the words list elements from end to start
i = len(words)-1
while i >= 0:
    print(words[i])
    i -= 1
else:
    print("While loop for array has ended")

# For loop to iterate through the elements of an list
for word in words:
    print(word)
else:
    print("For loop has ended")

# Sum up the numbers in an list
num_arr_sum = 0
for num in numbers:
    num_arr_sum += num

print(num_arr_sum)

my_sentence = ""
for word in words:
    my_sentence = my_sentence + " " + word

print(my_sentence)
