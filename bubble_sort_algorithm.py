"""
Bubble Sort is an algorithm that sorts an array from the lowest value to the highest value
"""

my_array = [35, 23, 6, 60, 20, 80]

def bubble_sort(arr):
    print("Bubble Sort")
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1): # n-i-1 not neglact the last element that was sorted in the previous iteration
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

                # print the array after each iteration for visualization
                print(arr)


def improved_bubble_sort(arr):
    print("Improved Bubble Sort")
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                # print the array after each iteration for visualization
                print(arr)
        # if no two elements were swapped by inner loop, then the array is sorted
        if not swapped:
            break

bubble_sort(my_array)

my_array = [20, 23, 6, 35, 60, 80]

improved_bubble_sort(my_array)
