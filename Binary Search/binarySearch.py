a=[10,20,25,30,40,45,60,80]
k=80
def search(a,k,start,end):
    if(start>end):
        return "Element not Found"
    mid=(start+end)//2
    if(a[mid]==k):
        return mid
    elif(a[mid]>k):
        return search(a,k,start,mid-1)
    else:
        return search(a,k,mid+1,end)

print(search(a,k,0,len(a)-1))