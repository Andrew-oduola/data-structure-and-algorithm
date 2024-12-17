my_array = [64, 34, 25, 5, 22, 11, 90, 12]

def selection_sort(my_array):
    n = len(my_array)
    for i in range(n-1):
        min_index = 1
        for j in range(i+1, n):
            if my_array[j] < my_array[min_index]:
                min_index = j
        min_value = my_array.pop(min_index)
        my_array.insert(i, min_value)
        # print array for visualization
        print(f'After pass {i+1}:', my_array)


"""Shifting of the elements index when an element is deleted and inserted 
takes time and can be a problem when working with large datasets
so instead we can swap it, it won't change anythig as the least element 
will be brought forward and the other side is not yet sorted"""


def improved_seleccton_sort(my_array):
    n = len(my_array)
    for i in range(n):
        min_index = 1
        for j in range(i+1, n):
            if my_array[j] < my_array[min_index]:
                min_index = j
        my_array[i], my_array[min_index] = my_array[min_index], my_array[i]
            

selection_sort(my_array)