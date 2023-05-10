
a=[1,2,3,1,4,5,2,3,1,6]
k=2
# res=[3,3,4,5,5,5,1,6]
from collections import deque
def func(a,k):
    q=deque()
    for i in range(k-1):
        if(len(q)!=0 and a[i]>a[q[-1]]):
            q.popleft()
        q.append(i)
    for i in range(k,len(a)):
        while(len(q)!=0 and a[i]>a[q[-1]]):
            q.pop()
        q.append(i)
        print(a[q[0]])

func(a,k)