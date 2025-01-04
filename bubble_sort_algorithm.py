"""
Bubble Sort is an algorithm that sorts an array from the lowest value to the highest value
How it works:

Go through the array, one value at a time.
For each value, compare the value with the next value.
If the value is higher than the next one, swap the values so that the highest value comes last.
Go through the array as many times as there are values in the array.
"""

# Initialize the array to be sorted
my_array = [35, 23, 6, 60, 20, 80]

# Define the bubble sort function
def bubble_sort(arr):
    print("Bubble Sort")
    # Get the length of the array
    n = len(arr)
    # Loop over each element in the array except the last one
    for i in range(n-1):
        print(f"i: {i}")
        # Loop over the array from the start to the n-i-1 element
        # n-i-1 ensures we don't compare the last sorted elements
        for j in range(n-i-1):
            print(f"n-i-1: {n-i-1}")
            # If the current element is greater than the next element
            if arr[j] > arr[j+1]:
                # Swap the elements
                arr[j], arr[j+1] = arr[j+1], arr[j]

                # print the array after each iteration for visualization
                print(arr)

# Call the bubble sort function and print the sorted array
bubble_sort(my_array)
print("Sorted array:", my_array)

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

my_array = [20, 23, 6, 35, 60, 80]

# improved_bubble_sort(my_array)
