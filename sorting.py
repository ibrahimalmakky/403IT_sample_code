import random
import time

# Randomly generate a list of numbers with repetition
def gen_rand_list(length):
    rand_list = []
    for _ in range(length):
        rand_list.append(random.randrange(0,length))
    return rand_list

# Measure the time it takes a function to process a list
def time_alg(sort_func, my_list):
    tic = time.perf_counter()
    sort_func(my_list.copy())
    toc = time.perf_counter()
    return toc-tic

# Selection Sort
def selectionSort(my_list):
    my_ordered_list = []
    while len(my_list) != 0:
        smallest_num_index = 0
        for i in range(0, len(my_list)):
            if (my_list[i] < my_list[smallest_num_index]):
                smallest_num_index = i
        my_ordered_list.append(my_list[smallest_num_index])
        del my_list[smallest_num_index]
    return my_ordered_list

# Bubble Sort (Herbert and Kasia)
def bubbleSort(my_list):
    for _ in range(len(my_list)):
        x = 0
        while x < len(my_list)-1:
            if my_list[x] > my_list[x+1]:
                my_list[x], my_list[x+1] = my_list[x+1], my_list[x]
            x += 1
    return my_list

# Bubble Sort (Weronika)
def bubbleSortW(my_list):
    n = len(my_list)
    for i in range(n-1):
        for j in range(n-i-1):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    return my_list


def test_sorting():
    lengths = [10, 100, 500, 1000, 5000, 10000, 15000, 20000]
    times = {'selectionSort':[], 'bubbleSort':[], 'bubbleSortW':[]}
    for length in lengths:
        current_list = gen_rand_list(length)
        times['selectionSort'].append(time_alg(selectionSort, current_list))
        times['bubbleSort'].append(time_alg(bubbleSort, current_list))
        times['bubbleSortW'].append(time_alg(bubbleSortW, current_list))
        print(times)

# test_sorting()
