import re

# user_inp = input("Please enter a list of number separated by commas.")
# split_inp = user_inp.split(",")
# list_of_nums = []
# for inp_num in split_inp:
#     try:
#         inp_num = int(inp_num)
#         list_of_nums.append(inp_num)
#     except:
#         print("Invalid input: "+inp_num)
# print(list_of_nums)

my_string = "Hello, my name is Ibrahim. It is a pleasure to meet you. I live in Coventry and it is always rainy here. However, I love this city very much."
test = re.search("it.*Coventry$", my_string)
print(test)

# Search for the first (4-letter) word that starts with an "l" and ends with an "e"
my_word = re.findall("l.{2}e", my_string)
print(my_word)

# Write code to find a phone number in a string (Polish mobile phone number)
test_string = "Hello, my phone number is 613 123 546. Please call me when you're free. I am usually free around 12:00pm"
phone_num = re.findall("[0-9]{9}|[0-9]{3} [0-9]{3} [0-9]{3}", test_string)
print(phone_num)
