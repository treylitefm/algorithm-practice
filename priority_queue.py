from random import random

def heapify(arr, n):
    i = n
    while True:
        if i > 0 and arr[i] > arr[(i-1)/2]: #if node is greater than parent
            parent = (i-1)/2
            (arr[parent],arr[i]) = (arr[i],arr[parent]) #swap
            i = parent
        else:
            break

nums = []

for i in range(15):
    nums.append(int(random()*100))

print nums

for i in range(1,len(nums)):
    heapify(nums, i) 
print nums

def printTree(arr, i, level, tree=None):
    if len(arr) <= i:
        return 
    if len(tree) <= level:
        tree.append([])
    tree[level].append(arr[i])
    printTree(nums, 2*i+1, level+1, tree)
    printTree(nums, 2*i+2, level+1, tree)

tree = []
printTree(nums, 0, 0, tree);

for row,level in zip(tree,range(len(tree))):
    print level,row
