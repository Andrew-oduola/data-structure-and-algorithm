def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    leftArr = arr[:mid]
    rightArr = arr[mid:]

    sortedLeft = mergeSort(leftArr)
    sortedRight = mergeSort(rightArr)

    return merge(sortedLeft, sortedRight)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

unsortedArr = [3, 7, 6, 5, 4, 3, 2, 1]
sortedArr = mergeSort(unsortedArr)

print(sortedArr)

