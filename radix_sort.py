def radix_sort(my_array: list):
    max_val = max(my_array)
    radix_array = [[], [], [], [], [], [], [], [], [], []]
    exp = 1

    while max_val // exp > 0:

        while len(my_array) > 0:
            val = my_array.pop()
            radix_index = (val // exp) % 10
            radix_array[radix_index].append(val)

        for bucket in radix_array:
            while len(bucket) > 0:
                val = bucket.pop()
                my_array.append(val)


        exp *= 10
    return my_array

my_array = [23, 56, 32, 63, 89, 43, 34]
print(radix_sort(my_array))