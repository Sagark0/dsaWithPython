import tree
Node=tree.Node
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(9)
root.left.right.left=Node(6)
root.left.right.right=Node(7)
root.right.left=Node(8)

def specialNode(root,maximum):
    if(root is not None):
        if(root.left is None and root.right is None):
            if(root.val>maximum):
                print("Node:"+str(root.val)+"is a Special Node")
            else:
                print("Node:"+str(root.val)+"is not a Special Node")
        specialNode(root.left,max(maximum,root.val))    
        specialNode(root.right,max(maximum,root.val))    
specialNode(root,-99)
