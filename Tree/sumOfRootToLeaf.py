import tree
Node=tree.Node
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.left.right.left=Node(6)
root.left.right.right=Node(7)
root.right.left=Node(8)


def getSum(root,sum):
    if(root is not None):
        temp=sum+root.val
        if(root.left is None and root.right is None):
            print(temp)
        getSum(root.left,temp)
        getSum(root.right,temp)
    
getSum(root,0)