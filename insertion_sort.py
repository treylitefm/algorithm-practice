from random import random
from time import time

start = time()

nums = [int(random()*10000) for i in range(100)] 

def insertion_sort(arr):
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            (arr[j-1],arr[j]) = (arr[j],arr[j-1])
            j -= 1
    return arr

print 'Before',nums
print 'After',insertion_sort(nums)
print 'Executed in',time()-start,'seconds!'
