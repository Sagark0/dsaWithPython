# Find kth smallest element in the sorted array
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
            # print("Mid:",mid)
            if(row[mid]>k):
                end=mid-1
                upperBound=mid
            else:
                start=mid+1
        count+=upperBound
        # print("upper BOund",upperBound)
    # print("Count",count)
    return count
def func(a,k):
    n=len(a)
    start=a[0][0]
    end=a[n-1][n-1]
    ans=-1
    while(start<=end):
        mid=(start+end)//2
        # print("Start:",start,"End:",end,"Mid",mid)
        count=checkSmaller(a,mid)
        if(count>=k):
            end=mid-1
            ans=mid
        else:
            start=mid+1
    return ans


print("ans:",func(a,k))




# The overall time complexity of the algorithm is O(n log w), where n is the number of rows in the matrix and w is the range of values in the matrix. This is because the checkSmaller function performs binary search on each row of the matrix, which takes O(log w) time, and is called once for each value of mid in the func function, which performs binary search on the range of values in the matrix, also taking O(log w) time.

# The space complexity of the algorithm is O(1), since only constant amount of extra space is used to store variables for the binary search and counting.