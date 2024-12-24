# Recursive Binary Search

def recursive_binary_search(array, target):
    if len(array) == 0:
        return False
    else:
        midpoint = len(array) // 2

        if array[midpoint] == target:
            return True
        elif array[midpoint] < target:
            return recursive_binary_search(array[midpoint+1:], target)
        else:
            return recursive_binary_search(array[:midpoint], target)
        
my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(recursive_binary_search(my_array, 11))