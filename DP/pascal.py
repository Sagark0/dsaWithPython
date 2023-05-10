def solve(numRows: int, output: list[list[int]]) -> list[int]:
    if(numRows == 1):
        output.append([1])
        return [1]
    elif(numRows == 2 ):
        output.append([1,1])
        return [1,1]
    else:
        prevList = solve(numRows-1, output)
        currList += prevList[0]
        for i in range(prevList-1):
            currList += prevList[i] + prevList[i+1]
        currList += prevList[-1]
        print(currList)
        output.append(currList)
        return currList
        output = []
        solve( numRows, output )
        return output