nums=[4,3,34,5,10,2]
target=7

def func(nums,dp,n,target):
    if(target==0):
        return True
    elif(n==0):
        return False
    else:
        if((n,target) not in dp):           
            inc=func(nums,dp,n-1,target-nums[n-1])
            exc=func(nums,dp,n-1,target)
            dp[(n,target)]=inc or exc

        return dp[(n,target)]
                

print(func(nums,{},len(nums),target))

# Recursion T.C = O(2^n) S.C = O(n)
# Memoization T.C = O(n * target) S.C = O(n * target) + O(N)