a=[[2,3,4,9],[3,5,5,10],[4,7,7,17],[8,10,12,19]]
k=4

def checkSmaller(a,k):
    count=0
    for row in a:
        upperBound=0
        start=0
        end=len(row)-1 
        while(start<=end):
            mid=(start+end)//2
            if(row[mid]>k):
                end=mid-1
                upperBound=mid
            else:
                start=mid+1
        count+=upperBound
    return count
def func(a,k):
    n=len(a)
    start=a[0][0]
    end=a[n-1][n-1]
    ans=-1
    while(start<=end):
        mid=(start+end)//2
        count=checkSmaller(a,mid)
        if(count>=k):
            end=mid-1
            ans=mid
        else:
            start=mid+1
    return ans

print(func(a,k))