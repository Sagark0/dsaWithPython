s='ababa' 
def solution(s,dp,i,j):
    if(i>len(s) or j<0):
        return 0
    else:
        if(s[i]==s[j]):
            return solution(s,dp,i+1,j-1)+1
        else:
            if((i,j) in dp):
                return dp[(i,j)]
            a=solution(s,dp,i+1,j)
            b=solution(s,dp,i,j-1)
            dp[(i,j)]=max(a,b)
            return dp[(i,j)]

print(solution(s,{},0,len(s)-1))
