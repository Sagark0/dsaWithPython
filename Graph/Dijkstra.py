import heapq
from turtle import distance


class Graph:
    def __init__(self,n):
        self.arr=[]
        for _ in range(n):
            edge=[]
            self.arr.append(edge)
    def addEdge(self,u,v,weight):
        self.arr[u].append((v,weight))
    def getNeighs(self,u):
        return self.arr[u]
n=6
graph=Graph(n)
graph.addEdge(0,1,1)
graph.addEdge(0,3,4)
graph.addEdge(1,3,1)
graph.addEdge(1,2,2)
graph.addEdge(3,4,6)
graph.addEdge(2,4,0)
graph.addEdge(2,5,7)
graph.addEdge(4,5,1) # (u,v,weight)

a=[]
def shortestPath(source):
    dist={}
    for i in range(n):
        dist[i]=99999
    dist[source]=0
    heapq.heappush(a,(0,source))
    while(len(a)>0):
        currentDistance, currentNode=heapq.heappop(a)
        print(dist)
        for neigh in graph.getNeighs(currentNode):      # neigh(destination, weight)
            newDistance=currentDistance+neigh[1]
            if(dist[neigh[0]]>newDistance):
                dist[neigh[0]]=newDistance
                heapq.heappush(a,(dist[neigh[0]],neigh[0]))

    return dist

print(shortestPath(0))