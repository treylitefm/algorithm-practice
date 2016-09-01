from random import random
from time import time

start = time()

nums = []

for i in range(100): 
    nums.append(int(random()*100000))

def selection_sort(arr):
    for i in range(len(arr)):
        index_min = i
        for j in range(i, len(arr)):
            if arr[j] < arr[index_min]:
                index_min = j
        (arr[index_min],arr[i]) = (arr[i],arr[index_min])
    return arr

print 'Before',nums
print 'After',selection_sort(nums)
print 'Executed in ',time()-start,'seconds'
