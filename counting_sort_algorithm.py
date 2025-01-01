myArray = [ 2, 3, 0, 2, 3, 2]

def counting_sort_algorithm(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
   
    while len(arr) > 0:
        num = arr.pop(0)
        count[num] += 1

    for i in range(len(count)):
        while count[i] > 0:
            arr.append(i)
            count[i] -= 1

    return arr


print(counting_sort_algorithm(myArray))

