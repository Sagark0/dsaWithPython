# Find and return the kth smallest element from array
a=[10,60,30,80,50]
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
        pivot=partition(a,start,end)   # Placing Pivot at correct position
        if(pivot-start==k-1):          # If Pivot is at the position K-1 -> return the position
            return a[pivot]
        elif(pivot-start>k-1):         # If Pivot is at greater position than k-1 -> return left portion
            return kSmallest(a,start,pivot-1,k)
        else:                          # If Pivot is at lesser position than k-1 -> return right portion
            return kSmallest(a,pivot+1,end,k-pivot+start-1)
    return

print(kSmallest(a,0,len(a)-1,k))
