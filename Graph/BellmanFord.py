class Graph:
    def __init__(self,n):
        self.arr=[]
        for _ in range(n):
            edge=[]
            self.arr.append(edge)
    def addEdge(self,u,v,w):
        self.arr[u].append((v,w))
    def getNeigh(self,u):
        return self.arr[u]
    
n=4
graph=Graph(n)
graph.addEdge(0,1,7)
graph.addEdge(0,2,5)
graph.addEdge(1,2,2)
graph.addEdge(2,3,12)
graph.addEdge(1,3,4)

def bellmanFord(graph,source):
    dist={}
    for i in range(n):
        dist[i]=99999
    dist[source]=0
    flag=False
    for V in range(n):
        for u in range(n):
            for (v,w) in graph.getNeigh(u):   
                if(dist[v]>dist[u]+w):
                    if(V<n-1):
                        dist[v]=dist[u]+w
                    else:
                        flag=True
    if(flag):
        print("Infinit Loop Initiated")
    else:
        print(dist)

bellmanFord(graph,0)
                

