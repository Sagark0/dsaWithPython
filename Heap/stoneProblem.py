import heapq

from urllib3 import Retry
# a=[2,5,7,6,3,1]
a=[9,5,4]

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

heap=MaxHeap(a)
while(heap.size()>=2):
    first=heap.pop()
    second=heap.pop()
    res=abs(first-second)
    if(res):
        heap.push(res)
if(not heap.size()):
    print('everthing is destroyed')
else:
    print('last stone is '+ str(heap.top()))

