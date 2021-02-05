from sorting import gen_rand_ord_list
from sorting import selection_sort
import time
import random

# Measure the time it takes the search function to execute
def time_search(search_func, my_list, num):
    tic = time.perf_counter()
    search_func(num, my_list)
    toc = time.perf_counter()
    return toc-tic

# Write some code to find a certain number in this list
# Input: the list and the number we are searching for
# Output: the index for the number we are searching for
def linear_search_first(num, my_list):
    for i in range(len(my_list)):
        if num == my_list[i]:
            return i
    return None

# Another linear search
# Input: A list of numbers to search within
# Output: the indexes for all the instances of the a certain number x
# Consider using recursion for this problem to get higher grades on the assignment
def linear_search_all(num, my_list):
    inds = []
    ind = linear_search_first(num, my_list)
    if ind is not None:
        inds.append(linear_search_first(num, my_list))
    else:
        return inds
    while True:
        ind = linear_search_first(num, my_list[inds[-1]+1:])
        if ind is not None:
            inds.append(ind+inds[-1]+1)
        else:
            break
    return inds

# Binary search function to find an occurance of a certain number
# Implemening Binary Search in a recursive way for your assignment will
# gain you higher grades
def binarySearch(num, sorted_list):
    start = 0
    end = len(sorted_list)-1

    while start <= end:
        mid = (start + end) // 2
        if (num > sorted_list[mid]):
            start = mid + 1
        elif (num < sorted_list[mid]):
            end = mid - 1
        else:
            return mid
    return None


def test_search_algorithms():
    lengths = [100, 500, 1000, 5000, 10000, 15000, 20000, 50000, 100000, 500000, 1000000, 5000000]
    times = {'LinearSearchFirstInstance':[], 'LinearSearch':[], 'BinarySearch':[]}
    for length in lengths:
        sorted_list = gen_rand_ord_list(length)
        rand_num = random.randrange(0, length)
        times['LinearSearchFirstInstance'].append(time_search(linear_search_first, sorted_list, rand_num))
        times['LinearSearch'].append(time_search(linear_search_all, sorted_list, rand_num))
        times['BinarySearch'].append(time_search(binarySearch, sorted_list, rand_num))
        print(times)
    return times

test_search_algorithms()
