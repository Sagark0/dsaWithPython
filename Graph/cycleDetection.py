class Graph:
    def __init__(self,n):
        self.arr=[]
        for _ in range(n):
            edge=[]
            self.arr.append(edge)
    def addEdge(self,u,v):
        self.arr[u].append(v)
        # self.arr[v].append(u)
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
graph.addEdge(4,2)


def cycleDetection(source,color):
    if(source not in color):
        color[source]='G'
        print(source)
        for neigh in graph.getNeigh(source):
            cycleDetection(neigh,color)
        color[source]='B'
    elif(color[source]=='G'):
        print("Cycle Detected!")
    # print(color)
cycleDetection(0,color={})