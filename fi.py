a = 0
b = 1
nos = []
for i in range(20):
    nos.append(a)
    print(a, end=" ")
    a, b = b, a + b

print(nos)