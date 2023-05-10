

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def addAtFront(self,data):
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode
    def printNode(self,head):
        curr=head
        while(curr!=None):
            print(curr.data)
            curr=curr.next

ll=LinkedList()
# ll.addAtFront(5)
# ll.addAtFront(4)
# ll.addAtFront(3)
# ll.addAtFront(2)
# ll.addAtFront(1)
# ll.head.next.next.next.next=ll.head.next
def detectCycle(head):
    if(head is None or head.next is None):
        return False
    fastPointer=head.next
    slowPointer=head
    while(fastPointer is not None and fastPointer.next is not None):
        if(fastPointer.data==slowPointer.data):
            return True
        fastPointer=fastPointer.next.next
        slowPointer=slowPointer.next
    return False

print(detectCycle(ll.head))
