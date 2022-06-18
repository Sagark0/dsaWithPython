class Stack:
    def __init__(self):
        self.st=[]
    def push(self,el):
        self.st.append(el)
    def pop(self):
        return self.st.pop()
    def top(self):
        return self.st[len(self.st)-1]
    def printStack(self):
        print(self.st)
    def length(self):
        return len(self.st)

st=Stack()
st.push(2)
st.push(8)
st.push(1)
st.push(6)
st.push(9)

def g(st,k):
    if(st.length()==0 or st.top()>=k):
        st.push(k)
    else:
        pop=st.pop()
        g(st,k)
        st.push(pop)


def f(st):
    if(st.length()>0):
        top=st.pop()
        f(st)
        g(st,top)

st.printStack()
f(st)
st.printStack()
