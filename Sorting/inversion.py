# count number of inversions

a=[2,5,1,6,3,8]
count=0
def merge(a,start,mid,end):
    global count
    i=start
    j=mid+1
    c=[]
    while(i<=mid and j<=end):
        if(a[i]<=a[j]):
            c.append(a[i])
            i+=1
        else:
            c.append(a[j])
            j+=1
            count+=(mid-i+1)
    while(i<=mid):
        c.append(a[i])
        i+=1
    while(j<=end):
        c.append(a[j])
        j+=1
    for index in range(len(c)):
        a[start+index]=c[index]

def mergeSort(a,start,end):
    if(start<end):
        mid=(start+end)//2
        mergeSort(a,start,mid)
        mergeSort(a,mid+1,end)
        merge(a,start,mid,end)
mergeSort(a,0,len(a)-1)
print(count)