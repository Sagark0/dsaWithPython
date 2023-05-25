class Node:
    def __init__(self,val):
        self.val=val
        self.right=None
        self.left=None
    
root=Node(1)
root.left=Node(2)
root.left.left=Node(3)
root.left.right=Node(4)
root.left.left.left=Node(5)
root.left.left.right=Node(6)
root.left.left.right.right=Node(7)
root.left.left.right.right.right=Node(8)
root.left.left.right.right.right.right=Node(9)

def height(root):
    if(root is not None):
        left=height(root.left)
        right=height(root.right)
        return max(left,right)+1
    else:
        return 0
def diameter(root):
    if (root is not None):
        left=height(root.left)
        right=height(root.right)
        leftDia=diameter(root.left)
        rightDia=diameter(root.right)
        dia=left+right+1
        return max(dia,leftDia,rightDia)
    else:
        return 0
print(diameter(root))

# T.C O(n^2) S.C O(n)

# T.C O(n) is also possible. How?