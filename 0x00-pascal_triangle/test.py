#!/usr/bin/python3

arr = [6, 4, 5, 3, 7, 2, 1, 0.5, 115]
newarr = []
length = len(arr)

for i in range(len(arr)):
    for j in range(len(arr) - 1):
        if arr[j] < arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

for k in range(2, -1, -1):
    print(k)
    newarr.append(arr[k])
print(arr)
print(newarr)