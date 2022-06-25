
class Node:
    def __init__(self,val):
        self.val=val
        self.right=None
        self.left=None

rootA=Node(1)
rootA.left=Node(2)
rootA.right=Node(3)
rootA.left.left=Node(4)
rootA.left.right=Node(5)
rootA.left.right.left=Node(6)
rootA.left.right.right=Node(7)
rootA.right.left=Node(8)

rootB=Node(1)
rootB.left=Node(2)
rootB.right=Node(3)
rootB.left.left=Node(4)
rootB.left.right=Node(5)
rootB.left.right.left=Node(6)
rootB.left.right.right=Node(7)
rootB.right.left=Node(8)
rootB.right.left.left=Node(9)

def checkSame(rootA,rootB):
    if(rootA is not None and rootB is None):
        return False
    elif(rootA is None and rootB is not None):
        return False
    elif(rootA is not None and rootB is not None):
        if(rootA.val!=rootB.val):
            return False
        left=checkSame(rootA.left,rootB.left)
        right=checkSame(rootA.right,rootB.right)
        return left and right
    else:
        return True

print(checkSame(rootA,rootB))
