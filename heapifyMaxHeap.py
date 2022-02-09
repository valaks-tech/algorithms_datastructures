# Heap implementation in python
"""
Heap is a binary tree. 2 types: Max Heap and Min Heap
Implementation of MaxHeap is below

Heapify ==>

build_heapify(A):
 for (i = (len(a)-1)/2 -1 )   to 0):
     build_heapify(A,i)

If heapsize = N:
   range of leave nodes = [N/2] to [N-1]
   range of internal nodes = 0 to [N/2]-1

Since you call build_heapify O(n) times, building the entire heap is O(n log n)

"""
class MaxHeap:
    def __init__(self,items=[]):
        super().__init__()
        self.heap = [0]
        for i in items:
            self.heap.append(i)
            self.__bubbleUp(len(self.heap) - 1)
    
    def push(self,data):
        self.heap.append(data)
        self.__bubbleUp(len(self.heap) - 1)
    
    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False
    
    def pop(self):
        # 3 possibilities
        if (len(self.heap)) > 2 : # remember we have a null and its 1-indexed
            # swap the first element(root) with last element
            self.__swap(1,len(self.heap) - 1)
            # pop the root
            max = self.heap.pop()
            # bubbledown
            self.__bubbleDown(1)
        elif len(self.heap) == 2:  # only root exits
            max = self.heap.pop()
        else: # no elements exist in heap
            max = False
        
        return max

    def __swap(self,i,j):
        self.heap[i], self.heap[j] = self.heap[j],self.heap[i]
    
    def __bubbleUp(self,index):
        parent = index // 2
        #2 possibilities
        # max element may be alreadt the top
        if index <= 1:
            return   # do nothing
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index,parent)
            self.__bubbleUp(parent)

    def __bubbleDown(self,index):
        left = index * 2  # remember its 1-indexed, not 0 indexed
        right = index * 2  + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index,largest)
            self.__bubbleDown(largest)
        
m = MaxHeap([9, 3, 51])
m.push(10)
m.push(56)
#m.pop()
#print(str(m.heap[0:len(m.heap)]))
print(str(m.pop()))
print(str(m.pop()))
print(str(m.pop()))
print(str(m.pop()))
print(str(m.pop()))
