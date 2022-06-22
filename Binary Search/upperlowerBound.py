from matplotlib.pyplot import legend


a=[10,20,60,60,60,60,70,100,130]
k=60
def lowerBound(a,k,start,end,ans):
    if(start>end):
        return ans
    mid=(start+end)//2
    if(a[mid]>=k):
        return lowerBound(a,k,start,mid-1,ans=mid)
    else:
        return lowerBound(a,k,mid+1,end,ans)
    
def upperBound(a,k,start,end,ans):
    if(start>end):
        return ans
    mid=(start+end)//2
    if(a[mid]<=k):
        return upperBound(a,k,mid+1,end,ans)
    else:
        return upperBound(a,k,start,mid-1,ans=mid)
print(lowerBound(a,k,0,len(a)-1,-1))
print(upperBound(a,k,0,len(a)-1,-1))