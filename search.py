from sorting import gen_rand_list

my_list = gen_rand_list(100)

# [3, 4, 1, 6, 3, 1]
# I would like to find all the occurences of x=1

# Write some code to find a certain number in this list
# Input: the list and the number we are searching for
# Output: the index for the number we are searching for
def find_num(num, my_list):
    for i in range(len(my_list)):
        if num == my_list[i]:
            return i
    return None

# Another linear search
# Input: A list of numbers to search within
# Output: the indexes for all the instances of the a certain number x
def find_nums(num, my_list):
    inds = []
    ind = find_num(num, my_list)
    if ind is not None:
        inds.append(find_num(num, my_list))
    else:
        return inds
    while True:
        ind = find_num(num, my_list[inds[-1]+1:])
        if ind is not None:
            inds.append(ind+inds[-1]+1)
        else:
            break
    return inds

# Consider using recursion for this problem to get higher grades on the assignment

print(my_list)
print(find_num(5, my_list))
print(find_nums(7, my_list))
# Assess the performance of the linear search function with an increasing number of elements in the list
