from requests import head


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def addAtFront(self,data):
        node=Node(data)
        node.next=self.head
        self.head=node
    def printList(self):
        curr=self.head
        while(curr is not None):
            print(curr.data)
            curr=curr.next

def reverseAList(head):
    if head is None or head.next is None:
        return head
    rest=reverseAList(head.next)
    head.next.next=head
    head.next=None
    return rest

ll=LinkedList()
ll.addAtFront(1)
ll.addAtFront(2)
ll.addAtFront(3)
ll.addAtFront(4)
ll.addAtFront(5)
ll.printList()
reverseAList(ll.head)
ll.printList()