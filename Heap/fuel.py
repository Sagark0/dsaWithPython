import heapq
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
target = 100
startFuel = 50
stations =[[10,20],[20,60],[50,30],[80,20]]
def minFuelStop(stations,startFuel,target):
    a=[]
    b=MaxHeap(a)
    currFuel=startFuel
    refill=0
    prev=0
    for station in stations:
        print("Reached station "+str(station[0]))
        currFuel=currFuel-station[0]+prev
        prev=station[0]
        print(currFuel)
        MaxHeap.push(b,station[1])
        if(currFuel>=target-station[0]):
            return refill
        if(currFuel<=0):
            if(b.size()==0):
                return -1
            while(currFuel<=0 and b.size()!=0):
                fuel=b.pop()
                print("Refuelling "+str(fuel))
                currFuel+=fuel
                refill+=1
    if(currFuel<target-stations[-1][0]):
        if(b.size()==0):
                return -1
        while(currFuel<=target-stations[-1][0] and b.size()!=0):
            fuel=b.pop()
            print("Refuelling "+str(fuel))
            currFuel+=fuel
            refill+=1

    return refill

print(minFuelStop(stations,startFuel,target))