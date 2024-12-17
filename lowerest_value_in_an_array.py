myarray = [3, 5, 7, 3, 6, 8, 1, 4, 8, 9]

lowest_value = myarray[0]
for i in myarray:
    if i < lowest_value:
        lowest_value = i

print(lowest_value)