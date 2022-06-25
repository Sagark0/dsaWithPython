a=[1,3,5,20,100]
m=3


def check(a,m,mid):
    cp=a[0]
    for i in range(1,len(a)):
        if((a[i]-cp)>=mid):
            m-=1
            cp=a[i]
    return not bool(m-1)
        
def func(a,m):
    start=a[0]
    end=a[-1]
    ans=-1
    while(start<=end):
        mid=(start+end)//2
        if(check(a,m,mid)):
            ans=mid
            start=mid+1
        else:
            end=mid-1
    return ans

print(func(a,m))

