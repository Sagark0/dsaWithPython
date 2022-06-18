# find next greater element in the stack


a=[7,5,3,2,6,8,10]
# a=[5,4,4,4,5,6,-1]
def func(a):
    n=len(a)
    res=[-1]*n
    st=[]
    for i in range(n):
        if(len(st)==0 or a[st[len(st)-1]]>=a[i]):
            st.append(i)
        else:
            while(len(st)>0 and a[st[len(st)-1]]<a[i]):
                res[st[len(st)-1]]=i
                st.pop()
            st.append(i)
        print(st)
    return res

print(func(a))