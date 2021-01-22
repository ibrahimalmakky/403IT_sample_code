my_list = [x for x in range(0, 100)]

chars_list = [letter for letter in "Hello"]

odd_numbers = [x for x in range(0, 100) if x%2 != 0]

print(odd_numbers)

# In-line loop to generate a list of numbers in fibonacci sequence
series = []
series.append(1)
series.append(1)
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...]
[series.append(series[x-1]+series[x-2]) for x in range(2, 10)]
print(series)

# Nested Loops in one line
mult_table = [x*y for x in range(1,10) for y in range(1,10)]

print(mult_table)

# Create a list of numbers with in-line loop that counts down from 100 to 0

