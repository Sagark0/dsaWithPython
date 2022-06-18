#implementing Merge Sort
arr=[8,7,6,5,4,3,2,1]
arr2=[9,3,23,5,2,56,3,1,5,6,7]
def merge(a,start,mid,end):
    i=start
    j=mid+1
    c=[]
    while(i<=mid and j<=end):
        if(a[i]<a[j]):
           c.append(a[i])
           i+=1
        else:
            c.append(a[j])
            j+=1
    while(i<=mid):
        c.append(a[i])
        i+=1
    while(j<=end):
        c.append(a[j])
        j+=1

    for index in range(len(c)):
        a[start+index]=c[index]
       
        


def mergeSort(a, start, end):
    if(start<end):
        mid=(start+end)//2
        mergeSort(a,start,mid)
        mergeSort(a,mid+1,end)
        merge(a,start,mid,end)
    return a

print(mergeSort(arr2,0,len(arr2)-1))

# time complexity is O(n log(n))
# space complexity is O(n)