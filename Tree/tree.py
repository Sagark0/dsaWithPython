class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
# root=Node(1)
# root.left=Node(2)
# root.right=Node(3)
# root.left.left=Node(4)
# root.left.right=Node(5)
# root.left.right.left=Node(6)
# root.left.right.right=Node(7)
# root.right.left=Node(8)
root = Node(10)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(7)
root.left.right = Node(8)
root.right.right = Node(15)
root.right.left = Node(12)
root.right.right.left = Node(14)  

def preOrder(root):
    if(root is not None):
        print(root.val)
        preOrder(root.left)
        preOrder(root.right)
def postOrder(root):
    if(root is not None):
        postOrder(root.left)
        postOrder(root.right)
        print(root.val)

def inOrder(root):
    if(root is not None):
        inOrder(root.left)
        print(root.val)
        inOrder(root.right)

def height(root):
    if(root is None):
        return 0
    else:
        left=height(root.left)
        right=height(root.right)
        return max(left,right)+1
print(height(root))
def level(root,parent):
    if(root is not None):
        currLevel=parent+1
        print("Level of "+ str(root.val)+" is "+ str(currLevel))
        level(root.left,currLevel)
        level(root.right,currLevel)
# print(level(root,0))
def leftView(root,level,maxLevel):
    if root is None:
        return
    if(level>maxLevel[0]):
        print(root.val)
        maxLevel[0]=level
    leftView(root.left,level+1,maxLevel)
    leftView(root.right,level+1,maxLevel)

# maxLevel=[0]
# leftView(root,1,maxLevel)