trinagle_tuple = (5, 4, 9)
trinagle_list = [5, 4, 9]
trinagle_list[0] = 8

# Get the length of a tuple
print(len(trinagle_tuple))

test_tuple = ("Hello", 5, 4.7)
print(type(test_tuple))

for i in test_tuple:
    print(i)

# Join tuples
print(test_tuple+trinagle_tuple)
print(test_tuple*2)

# Convert tuple to a list
print(list(trinagle_tuple))