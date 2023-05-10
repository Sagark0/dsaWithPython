a=[2,10,6,8,4,3,5]
# In partition function we choose a pivot and place to correct position
# elements smaller than pivot will be on left side of pivot
# elements larger than pivot will be on right side of pivot
def partition(a,start,end):
    left=start-1
    pivot=end
    for i in range(start,end+1):
        if(a[i]<=a[pivot]):
            left+=1
            a[left],a[i]=a[i],a[left]
    return left

def quickSort(a,start,end):
    if(start<end):
        pivotPosition=partition(a,start,end)
        quickSort(a,start,pivotPosition-1)
        quickSort(a,pivotPosition+1,end)
    return a

print(quickSort(a,0,len(a)-1))

# Average Complexity O(nlogn), Worst O(n^2)