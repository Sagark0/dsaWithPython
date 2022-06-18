# st=[1,2,3,4,5]
class Stack:
    def __init__(self):
        self.st=[]
    def push(self,data):
        self.st.append(data)
    def pop(self):
        return self.st.pop()
    def top(self):
        return self.st[len(self.st)-1]
    def printStack(self):
        print(self.st)
    def length(self):
        return len(self.st)

def g(st,pop):
    if(st.length()==0):
        st.push(pop)
    else:
        temp=st.pop()
        g(st,pop)
        st.push(temp)
def reverse(st):
    if(st.length()>0):
        pop=st.pop()
        reverse(st)
        g(st,pop)

st=Stack()
st.push(1)
st.push(2)
st.push(3)
st.push(4)
st.push(5)
st.printStack()
reverse(st)
st.printStack()