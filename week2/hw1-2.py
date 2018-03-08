import random

arr = [None] * 100
for i in range(1, 100):
    arr[i] = i
    arr2 = i

arr[0] = random.randint(1, 99)
print(arr)

random.shuffle(arr)

randoms = [x for n, x in enumerate(arr) if x in arr[:n]]
print ("Duplicate Num: ", randoms)