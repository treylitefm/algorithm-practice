from random import random
from time import time

start = time()

nums = []

for i in range(100): 
    nums.append(int(random()*100000))

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                (arr[j+1],arr[j]) = arr[j],arr[j+1]
    return arr

print bubble_sort(nums)
print 'Executed in ',time()-start,'seconds'
