def recursive_binary_search(list1, target):
    """This function work just like the binary search 
    but with recursion. It starts by checking if the list is empty. If it is, it returns False.
    If the list isn't empty, it finds the midpoint of the list and compares it to the target.
    If they're equal, it returns True. If the midpoint is less than the target, it recursively calls itself on the right(or left) half of the list.
    """
    if len(list1) == 0: # Check if the list is empty
        return False
    else:
        midpoint = (len(list1))//2 # Get the midpoint of the list

        if list1[midpoint] == target: # Check if the midpoint is equal to the target
            return True
        else:
            if list1[midpoint] < target: # if the midpoint is less than the target
                return recursive_binary_search(list1[midpoint+1:], target) # Recursive binary search on the right side of the list
            else:
                return recursive_binary_search(list1[:midpoint], target) # Recursive binary search on the left side of the list
            
def verify(result):
    print("Target found: ", result)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = recursive_binary_search(numbers, 12)
verify(result)

result = recursive_binary_search(numbers, 6)
verify(result)