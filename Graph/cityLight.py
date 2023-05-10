from collections import deque
arr=[
    ['F','F','F','F'],
    ['F','C','F','C'],
    ['F','C','C','C'],
    ['F','F','F','F']
]
def bfs(grid,x,y,visited,distance,maxm):
    neighs=[[-1,0],[0,-1],[1,0],[0,1]]
    visited[(x,y)]=True
    distance[(x,y)]=0
    q=deque()
    q.append((x,y))
    while(len(q)>0):
        top=q.popleft()
        x=top[0]
        y=top[1]
        for neigh in neighs:
            newX=x+neigh[0]
            newY=y+neigh[1]
            if(newX>=0 and newY>=0 and newX<len(grid) and newY<len(grid[0])):
                if(grid[newX][newY]=='C' and (newX,newY) not in visited):
                    q.append((newX,newY))
                    visited[(newX,newY)]=True
                    distance[(newX,newY)]=distance[top]+1
                    maxm=max(maxm,distance[(newX,newY)])
    return maxm
def cityLight(grid,x,y):
    visited={}
    distance={}
    m=len(grid)
    n=len(grid[0])
    for i in range(m):
        for j in range(n):
            distance[(i,j)]=9999999
    maxm=0
    maxm=bfs(grid,x,y,visited,distance,maxm)
    return maxm

print(cityLight(arr,1,1))
