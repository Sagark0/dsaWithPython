from collections import deque
from operator import ne
class Graph:
    def __init__(self,n):
        self.adj=[]
        for i in range(n):
            edges=[]    
            self.adj.append(edges)
    def addEdge(self,u,v):
        self.adj[u].append(v)
        self.adj[v].append(u)
    def getNeigh(self,u):
        return self.adj[u]

n=5
graph=Graph(5)
graph.addEdge(0,1)
graph.addEdge(0,2)
graph.addEdge(2,3)
# graph.addEdge(3,4)
graph.addEdge(0,4)
print(graph.getNeigh(1))
def bfs(source):
    q=deque()
    visited={}
    q.append(source)
    for i in range(n):
        visited[i]=False
    visited[source]=True
    while(len(q)>0):
        element=q.popleft()
        print(element)
        for neigh in graph.getNeigh(element):
            if(visited[neigh]==False):
                q.append(neigh)
                visited[neigh]=True

bfs(0)

