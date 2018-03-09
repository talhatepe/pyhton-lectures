import random

arr = [None] * 100
tmp = [None] * 99

for i in range(1, 100):
    arr[i] = i
tmp += arr
arr[0] = random.randint(1, 99)
random.shuffle(arr)
print(arr)

for i in arr:
    d = tmp[i-1]
    if d == None:
        tmp[i-1] = 1
    else:
        print("Duplicate Num: ", i)
