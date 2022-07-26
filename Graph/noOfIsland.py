from collections import deque


arr=[['L','W','W','W','L'],
    ['W','W','L','W','W'],
    ['L','L','L','W','W'],
    ['W','W','W','W','W']]

neighs=[[-1,0],[0,-1],[1,0],[0,1]]

def bfs(grid,x,y,visited):
    visited[(x,y)]=True
    q=deque()
    q.append((x,y))
    while(len(q)>0):
        top=q.popleft()
        x=top[0]
        y=top[1]
        for neigh in neighs:
            newX=neigh[0]+x
            newY=neigh[1]+y
            if(newX>=0 and newY>=0 and newX<len(grid) and newY<len(grid[0])):
                if((newX,newY) not in visited and grid[newX][newY]=='L'):
                    q.append((newX,newY))
                    visited[(newX,newY)]=True
def noOfIsland(grid):
    count=0
    visited = {}
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if((x,y) not in visited and grid[x][y]=='L'):
                count+=1
                bfs(grid,x,y,visited)
    return count

print(noOfIsland(arr))

