import random

arr = [None] * 100
for i in range(1, 100):
    arr[i] = i

arr[0] = random.randint(1, 99)
random.shuffle(arr)
print(arr)

x = 0
for i in range(0, 100):
    x = x + i

total = 0
for i in range(len(arr)):
    total += arr[i]
print("Duplicate Num: ", total - x)
