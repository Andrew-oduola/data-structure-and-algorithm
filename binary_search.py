def binary_search(list, target):
    first = 0
    last = len(list) - 1
    
    while first <= last:
        midpoint = (first + last)//2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 4

result = binary_search(list1, target)
print(result)

