#!/usr/bin/python3

arr = [4, 3, 5, 2]
s = set()
newlist = []

for i in range(4):
    for j in range(4):
        newlist.append((arr[i], arr[j]))

print(newlist)
        
 
