class Graph:
    def __init__(self,n):
        self.arr=[]
        self.incomingEdge=[]
        for _ in range(n):
            edges=[]
            self.arr.append(edges)
            self.incomingEdge.append(0)
    def addEdge(self,u,v):
        self.arr[u].append(v)
        self.incomingEdge[v]+=1
    def noOfIncomingEdge(self,u):
        return self.incomingEdge[u]
    def getNeigh(self,u):
        return self.arr[u]
    
n=5
graph=Graph(n)
graph.addEdge(1,0)
graph.addEdge(2,1)
graph.addEdge(2,0)
graph.addEdge(0,3)
graph.addEdge(3,4)


def dfs(source,visited,st):
    if(visited[source]=='W'):
        visited[source]='G'
        # print(source)
        for neigh in graph.getNeigh(source):
            if(visited[neigh]=='W'):
                dfs(neigh,visited,st)
        visited[source]='B'
        st.append(source)
    elif(visited[source]=='G'):
        print("Cycle Found")

def topologicalSort(n):
    visited={}
    for i in range(n):
        visited[i]='W'
    st=[]
    for i in range(n):
        if(visited[i]=='W' and not graph.noOfIncomingEdge(i)):
            dfs(i,visited,st)
    while(len(st)>0):
        print(st.pop())

topologicalSort(n)
