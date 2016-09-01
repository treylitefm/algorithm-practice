from random import random
from time import time

start = time()

nums = []

for i in range(10000): 
    nums.append(int(random()*10000))

def selection_sort(arr):
    count = 0
    for i in range(len(arr)):
        index_min = i
        index_max = i
        for j in range(i, len(arr)):
            count += 2
            if arr[j] < arr[index_min]:
                index_min = j
            elif arr[j] > arr[index_max]:
                index_max = j
        (arr[index_min],arr[index_max]) = (arr[index_max],arr[index_min])
    print count,'times'
    return arr

#print 'Before',nums
#print 'After',selection_sort(nums)
selection_sort(nums)
print 'Executed in ',time()-start,'seconds'
