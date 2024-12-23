def binary_search(list, target):
    first = 0 # Set the first to the first element
    last = len(list) - 1 # Set the last to the last element
    
    while first <= last: # Continue looping if first variable <= last variable
        midpoint = (first + last)//2  # Get the middle index of the current search interval

        if list[midpoint] == target: # If the target variable is the middle element
            return midpoint # return the index
        elif list[midpoint] < target: # If the middle element is less than the target
            first = midpoint + 1 # Move the starting index to the right of the midpoint, this mean the target can't be in the left part of the array
        else:
            last = midpoint - 1 # Else the middle element is greater than the target so the target will be in the left part of the array, so we set the last index to the index before the midpoint

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 4

result = binary_search(list1, target)
print(result)

