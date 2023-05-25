# find next greater element in the stack


a=[7,5,3,2,6,8,10]
# a=[5,4,4,4,5,6,-1]
def func(nums2):
    n=len(nums2)
    res=[-1]*n
    st=[]
    for i in range(n):
        while(len(st)>0 and nums2[i] > nums2[st[-1]]):
            top = st.pop()
            res[top] = nums2[i]
        st.append(i)
        # print(st)
    return res

print(func(a))

# Stack will store elements in increasing order (top -> down)