
class Graph:
    def __init__(self,n):
        self.arr=[]
        for i in range(n):
            edges=[]
            self.arr.append(edges)
    def addEdge(self,u,v):
        self.arr[u].append(v)
        self.arr[v].append(u)
    def getNeigh(self,u):
        return self.arr[u]

graph=Graph(8)
graph.addEdge(0,1)
graph.addEdge(0,2)
graph.addEdge(1,5)
graph.addEdge(5,6)
graph.addEdge(6,7)
graph.addEdge(2,3)
graph.addEdge(2,4)
visited={}
def dfs(source,visited):
    if(source not in visited):
        visited[source]=True
        print(source)  
        for neigh in graph.getNeigh(source):
            # if(neigh not in visited):
                dfs(neigh,visited)

dfs(0,visited)