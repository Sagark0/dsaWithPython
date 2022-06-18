a=[2,3,1,6,8,4]
k=3

def partition(a,start,end):
    left=start-1
    pivot=end
    for i in range(start,end+1):
        if(a[i]<=a[pivot]):
            left+=1
            a[i],a[left]=a[left],a[i]
    return left

def kSmallest(a,start,end,k):
    if(k>0 and k<=end-start+1):
        pivot=partition(a,start,end)
        if(pivot-start==k-1):
            return a[pivot]
        elif(pivot-start>k-1):
            return kSmallest(a,start,pivot-1,k)
        else:
            return kSmallest(a,pivot+1,end,k-pivot+start-1)
    return

print(kSmallest(a,0,len(a)-1,k))
