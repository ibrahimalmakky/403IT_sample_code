my_list = [6, 4, 9, 2, 5, 3, 1]
another_list = [3, 2, 1]
# my_ordered_list = [smallest_number, ..., largest_number ]

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

print(selectionSort(my_list))
print(selectionSort(another_list))

# Write code to sort a list of numbers using bubble sort