
a=[1,3,-1,-3,5,3,6,7]
k=3
# res=[3,3,4,5,5,5,1,6]
from collections import deque
def func(a,k):
    q=deque()
    for i in range(k-1):
        if(len(q)!=0 and a[i]>a[q[-1]]):
            q.pop()
        q.append(i)
    for i in range(k-1,len(a)):
        if( len(q)!=0 and q[0] == i-k):
            q.popleft()
        while(len(q)!=0 and a[i]>a[q[-1]]):
            q.pop()
        q.append(i)
        print(a[q[0]])
func(a,k)