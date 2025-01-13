# FIBONACCI

arr = []

x = 1
y = 0
z = 0

for i in range(0, 100):
    z = x + y
    x = y
    y = z
    arr.append(y)

print(arr)