'''
def binary_search(arr, target, start=None, n=None):
    if start is None:
        start = 0
    if n is None:
        n = len(arr)
    if n is 0:
        return False
    
    i = start + n/2

    if target is arr[i]:
        return i
    elif target > arr[i]:
        return binary_search(arr, target, i+1, start+(n-1)-i) #search right side
    else: #target < arr[i] by law of trichotomy
        return binary_search(arr, target, start, i-start) #search left side
'''

def binary_search(arr, target): #implemented without recursion
    first = 0
    last = len(arr)-1

    while True:
        if first > last:
            return False
        mid = (first+last)/2
        if arr[mid] is target:
            return mid
        elif arr[mid] > target:
            last = mid-1
        else:
            first = mid+1

def linear_search(arr, n):
    for i in arr:
        if arr[i] is n:
                return i
