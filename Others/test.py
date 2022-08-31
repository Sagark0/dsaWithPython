#User function Template for python3
class Graph:
    def __init__(self,n):
        self.arr=[]
        for i in range(n):
            Edge=[]
            self.arr.append(Edge)
    def addEdge(self,u,v):
        self.arr[u].append(v)
        self.arr[v].append(u)
    def getNeighs(self,u):
        return self.arr[u]
def dfs(graph,node,visited,color,q,ans):
    if(node not in visited and color[node] in q):
        visited[node]=True
        print("visiting node:",node,"color:",color[node])
        ans.add(color[node])
        for neigh in graph.getNeighs(node):
            if(neigh not in visited and color[neigh] in q):
                dfs(graph,neigh,visited,color,q,ans)
    

def solve(N,col, Edge, query):
    graph=Graph(N)
    for edge in Edge:
        graph.addEdge(edge[0],edge[1])
    res=[]
    for q in query:
        # print(1)
        visited={}
        ans=set()
        dfs(graph,0,visited,col,q,ans)
        flag=0
        for c in q:
            if c not in ans:
                flag=1
                break
        if(flag==0):
            res.append('YES')
        else:
            res.append('NO')
    return res
        

N = 6
col = "abdebc"
Edge = [{0, 1}, {0, 2}, {1, 3}, {1, 4},
            {1, 2}, {2, 4}, {4,5}]
query = {"abc", "aec", "azc"}
print(solve(N,col,Edge,query))