matrix=[
    [2,4,7,1],
    [2,2,6,7],
    [4,3,10,5],
    [100,2,5,3]
]
def func(matrix,dp,x,y,value):
    if(x==len(matrix)-1 and y==len(matrix[0])-1):
        return value+matrix[x][y]
    elif(x==len(matrix)-1):
        if((x,y) not in dp):
            dp[(x,y)]=func(matrix,dp,x,y+1,value+matrix[x][y])
        return dp[(x,y)]
    elif(y==len(matrix[0])-1):
        if((x,y) not in dp):
            dp[(x,y)]=func(matrix,dp,x+1,y,value+matrix[x][y])
        return dp[(x,y)]
    else:
        if((x,y) not in dp):
            dp[(x,y)]=max(func(matrix,dp,x+1,y,value+matrix[x][y]),func(matrix,dp,x,y+1,value+matrix[x][y]))
        return dp[(x,y)]

print(func(matrix,{},0,0,0))