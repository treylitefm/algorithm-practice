def binary_search(arr, target, start=None, n=None):
    #import ipdb; ipdb.set_trace()
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

def linear_search(arr, n):
    for i in arr:
        if arr[i] is n:
            return i
