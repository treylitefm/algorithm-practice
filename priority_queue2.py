from random import random

class PriorityQueue(object): #implemented using min-heap; all nodes are greater than or equal to children
    arr = None

    def __init__(self, arr):
        self.arr = arr
        for i in range(1, len(self.arr)):
            self.__heapify_up(self.arr, i)

    def __heapify_up(self, arr, n): #take element at end of list with length n and heapify it upwards until greater than parent
        i = n
        while True:
            if i > 0 and arr[i] < arr[(i-1)/2]: #if node is less than parent
                parent = (i-1)/2
                (arr[parent],arr[i]) = (arr[i],arr[parent]) #swap
                i = parent
            else:
                break

    def __heapify_down(self, arr, n):
        i = 0
        while True:
            if 2*i+1 < n:
                left = 2*i+1
                right = 2*i+2
                if arr[i] < min(arr[left],arr[right]):
                    break
                else:
                    if arr[left] <= arr[right]:
                        (arr[i],arr[left]) = (arr[left],arr[i]) #swap parent with left child
                        i = left
                    else:
                        (arr[i],arr[right]) = (arr[right],arr[i]) #swap parent with right child
                        i = right
            else:
                break

    def __treeify(self, arr, i, level, tree):
        if len(arr) <= i:
            return 
        if len(tree) <= level:
            tree.append([])
        tree[level].append(arr[i])
        self.__treeify(arr, 2*i+1, level+1, tree)
        self.__treeify(arr, 2*i+2, level+1, tree)

    def get_tree(self):
        tree = []
        self.__treeify(self.arr, 0, 0, tree);
        return tree

    def get_array(self):
        return self.arr

    def print_tree(self):
        tree = self.get_tree()
        for row,level in zip(tree,range(len(tree))):
            print level,row

    def push(self, n):
        self.arr.append(n)
        self.__heapify_up(self.arr, len(self.arr)-1)

    def pop(self):
        val = self.arr[0]
        (self.arr[-1],self.arr[0]) = (self.arr[0],self.arr[-1])
        self.arr = self.arr[:-1]
        self.__heapify_down(self.arr, len(self.arr))
        return val

    def heapsort(self):
        arr = self.arr
        for i in range(len(arr)-1, 0, -1):
            (arr[i],arr[0]) = (arr[0],arr[i])
            self.__heapify_down(arr, i-1)
        return arr

    def heapify(self):
        for i in range(1, len(self.arr)):
            self.__heapify_up(self.arr, i)
        return self.arr

'''
nums = []

for i in range(15):
    nums.append(int(random()*100))

nums.append(100)
print nums

pq = PriorityQueue(nums)

pq.push(25)
pq.push(205)

print pq.get_array()
print pq.heapsort()
print pq.heapify()

print pq.get_array()
pq.print_tree()

print 'popped:',pq.pop()

print pq.get_array()
pq.print_tree()
'''
