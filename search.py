from sorting import gen_rand_list

my_list = gen_rand_list(100)

# Write some code to find a certain number in this list
# Input: the list and the number we are searching for
# Output: the index for the number we are searching for
def find_num(num, my_list):
    for i in range(len(my_list)):
        if num == my_list[i]:
            return i
    return None

print(my_list)
print(find_num(5, my_list))
