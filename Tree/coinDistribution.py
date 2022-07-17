import tree
Node=tree.Node
root=Node(1)
b=Node(0)
c=Node(0)
d=Node(3)
e=Node(1)

root.left=b
root.right=c
b.left=d
b.right=e


count=0

def coin(root):
    global count
    if(root is not None):
        left=coin(root.left)
        right=coin(root.right)
        req=root.val-1+left+right
        count+=abs(left)+abs(right)
        return req
    else:
        return 0
def netReqCoin(root):
    global count
    if(root is not None):
        left=coin(root.left)
        right=coin(root.right)
        req=root.val-1+left+right
        count+=abs(left)+abs(right)
        return req
    else:
        return 0
netRequirement=coin(root)
print(netRequirement)
if(not netRequirement):
    print(count)
else:
    print('cant be balanced')

