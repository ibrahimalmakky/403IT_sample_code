import random
import time

# Randomly generate a list of numbers with repetition
def gen_rand_list(length):
    rand_list = []
    for _ in range(length):
        rand_list.append(random.randrange(0,length))
    return rand_list

# Randomly generate a list of ordered numbers
def gen_rand_ord_list(length):
    rand_list = []
    i = 0
    while len(rand_list) < length:
        flip = random.randrange(0,2)
        if flip == 0:
            pass
        else:
            rand_list.append(i)
        i+=1
    return rand_list

# Measure the time it takes a function to process a list
def time_alg(sort_func, my_list):
    tic = time.perf_counter()
    sort_func(my_list.copy())
    toc = time.perf_counter()
    return toc-tic

# Selection Sort
# Computation Complexity (Big-O notation)
# O(n**2)
def selection_sort(my_list):
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
# Computational Complexity: O(n**2)
def bubble_sort(my_list):
    for _ in range(len(my_list)):
        x = 0
        while x < len(my_list)-1:
            if my_list[x] > my_list[x+1]:
                my_list[x], my_list[x+1] = my_list[x+1], my_list[x]
            x += 1
    return my_list


# Bubble Sort (Weronika)
# Computational Complexity: O(n**2)
def bubble_sort_w(my_list):
    n = len(my_list)
    for i in range(n-1):
        for j in range(n-i-1):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    return my_list


# Merge Sort
# Computational Complexity: O(n*log(n))
def merge_sort(my_list):
    if len(my_list) > 1:
        mid = len(my_list) // 2
        L = my_list[:mid].copy()
        R = my_list[mid:].copy()
        merge_sort(L)
        merge_sort(R)
        
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                my_list[k] = L[i]
                i+=1
            else: 
                my_list[k] = R[j]
                j+=1
            k += 1
        
        while i < len(L) and k < len(my_list):
            my_list[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R) and k < len(my_list):
            my_list[k] = R[j]
            j+=1
            k+=1

    else:
        return my_list


# Pass a list and return the largest index of a specified list of indices
# Example:
# [3, 5, 7, 2]
# [0, 1, 2]
# 2
def largest_ind(alist, inds):
    largest_ind = inds[0]
    for i in range(1, len(inds)):
        if alist[largest_ind] < alist[inds[i]]:
            largest_ind = inds[i]
    return largest_ind

# swap two elements of a list
def swap(alist, ind1, ind2):
    alist[ind1], alist[ind2] = alist[ind2], alist[ind1]

# Build max heap
def max_heap(my_list):
    # print(my_list)
    first_non_leaf_node = int(len(my_list)/2-1)
    for i in range(first_non_leaf_node, -1, -1):
        left_child = 2*i+1
        right_child = 2*i+2
        root = my_list[i]
        
        if right_child < len(my_list):
            print(str(my_list[i])+": "+str(my_list[left_child])+", "+str(my_list[right_child]))
            largest_num = largest_ind(my_list, [i, left_child, right_child])
        elif left_child < len(my_list):
            print(str(my_list[i])+": "+str(my_list[left_child]))
            largest_num = largest_ind(my_list, [i, left_child])
            # print(my_list[largest_num])
        else:
            largest_num = i

        if largest_num != i:
                swap(my_list, i, largest_num)
                # Something can be done here to make things more effecient
                max_heap(my_list)
        # print(my_list)

# Heap Sort
def heap_sort(my_list):
    
    sorted_list = []
    n = len(my_list)
    max_heap(my_list)

    while len(sorted_list) < n:
        swap(my_list, 0, -1)
        sorted_list.append(my_list[-1])
        del my_list[-1]
        max_heap(my_list)

    return sorted_list

def test_sorting():
    lengths = [10, 100, 500, 1000, 5000, 10000, 15000, 20000]
    times = {'selectionSort':[], 'bubbleSort':[], 'bubbleSortW':[], 'mergeSort':[]}
    for length in lengths:
        current_list = gen_rand_list(length)
        times['selectionSort'].append(time_alg(selection_sort, current_list))
        times['bubbleSort'].append(time_alg(bubble_sort, current_list))
        times['bubbleSortW'].append(time_alg(bubble_sort_w, current_list))
        times['mergeSort'].append(time_alg(merge_sort, current_list))
        print(times)

# test_sorting()
# print(gen_rand_ord_list(100))
# my_list = gen_rand_list(10)
# merge_sort(my_list)
# print(my_list)
# heap_sort([1,12,9,5,6,10])