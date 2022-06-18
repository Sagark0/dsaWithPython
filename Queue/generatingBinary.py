# generate Binary Pattern
from collections import deque

def generate(k):
    q=deque(['0','1'])
    cnt=0
    while(cnt<k):
        el=q.popleft()
        print(el)
        q.append(el+'0')
        q.append(el+'1')
        cnt+=1
generate(10)

