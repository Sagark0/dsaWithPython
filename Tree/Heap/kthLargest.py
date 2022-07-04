import heapq
a=[5,7,3,1,9,4,10]
k=2
class MaxHeap:
    def __init__(self,arr):
        self.arr=[]
        for i in arr:
            heapq.heappush(self.arr,-i)    
    def push(self,x):
        heapq.heappush(self.arr,-x)
    def pop(self):
        return -heapq.heappop(self.arr)
    def top(self):
        return -self.arr[0]
    def size(self):
        return len(self.arr)

def klargest(a,k): #kth largest using min heap
    b=[]
    for i in range(k):
        heapq.heappush(b,a[i])
    for i in range(k,len(a)):
        if(b[0]<a[i]):
            heapq.heappop(b)
            heapq.heappush(b,a[i])
    return b[0]

def klargest2(a,k): #kth largest using maxheap ||  Less Efficient
    b=[]
    heap=MaxHeap(a)
    for i in range(k-1):
        heap.pop()
    print(heap.pop())

    
klargest2(a,k)