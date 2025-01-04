# Initialize the array to be sorted
my_array = [4, 34, 25, 12, 22, 11, 80, 5]

# Get the length of the array
n = len(my_array)

# Loop over each element in the array starting from the second element
for i in range(1, n):
    # Set the index where the current value will be inserted
    insert_index = i
    # Remove the current element from the array and store it in current_value
    current_value = my_array.pop(i)
    
    # Loop backwards through the sorted portion of the array
    for j in range(i-1, -1, -1):
        # If the current element in the sorted portion is greater than current_value
        if my_array[j] > current_value:
            # Update the insert_index to the current position
            insert_index = j
    
    # Insert the current_value at the correct position in the sorted portion
    my_array.insert(insert_index, current_value)

# Print the sorted array
print("Sorted array:", my_array)