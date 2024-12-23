# One of the fastest sorting algorithm

def partition(array, low, high):
    pivot = array[high]  # Choose the last element as the pivot
    i = low - 1  # Start with i just before the low index
    
    for j in range(low, high):  # Loop through the array from low to high-1
        if array[j] <= pivot:  # If the current element is less than or equal to the pivot
            i += 1  # Move the smaller element index forward
            array[i], array[j] = array[j], array[i]  # Swap the elements
    
    array[i+1], array[high] = array[high], array[i+1]  # Place the pivot in the correct position
    return i + 1  # Return the index of the pivot

def quick_sort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1  # Set high to the last index if not provided

    if low < high:  # Only sort if there are at least two elements
        pivot_index = partition(array, low, high)  # Get the pivot index
        quick_sort(array, low, pivot_index - 1)  # Recursively sort the left part
        quick_sort(array, pivot_index + 1, high)  # Recursively sort the right part

my_array = [64, 34, 25, 12, 22, 11, 90, 5]
quick_sort(my_array)
print("Sorted array:", my_array)