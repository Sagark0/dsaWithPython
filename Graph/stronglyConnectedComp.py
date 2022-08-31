# Strongly Connected Components are group of those components in which we can reach from every single node to every other node


class Graph:
    def __init__(self,n):
        self.arr=[]
        self.arr2=[]
        for _ in range(n):
            edges=[]
            edges2=[]
            self.arr.append(edges)
            self.arr2.append(edges2)
    def addEdge(self,u,v):
        self.arr[u].append(v)
        self.arr2[v].append(u)
    def getNeigh(self,arr,u):
        if(arr=='arr1'):
            return self.arr[u]
        elif(arr=='arr2'):
            return self.arr2[u]
        else:
            return []
n=5
graph=Graph(n)
graph.addEdge(1,0)
graph.addEdge(2,1)
graph.addEdge(0,2)
graph.addEdge(0,3)
graph.addEdge(3,4)


def dfs(source,arr,visited,st,printNode):
    if source not in visited:
        visited[source]=True
        if printNode:
            print(source)
        for neigh in graph.getNeigh(arr,source):
            if neigh not in visited:
                dfs(neigh,arr,visited,st,printNode)
        st.append(source)
def firstdfs():
    visited={}
    st=[]
    for i in range(n):
        if i not in visited:
            dfs(i,'arr1',visited,st,False)
    return st
    
def ssc():

    st=firstdfs()
    visited={}
    st2=[]
    while(len(st)>0):
        top=st.pop()
        if top not in visited:
            print("----------")
            dfs(top,'arr2',visited,st2,True)


ssc()
