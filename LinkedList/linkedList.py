from requests import delete, head


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def addAtFront(self,data):
        node=Node(data)
        node.next   =self.head
        self.head=node
    def printList(self):
        curr=self.head
        while(curr is not None):
            print(curr.data)
            curr=curr.next
    def deleteFromFront(self):
        if(self.head==None):
            print("Nothing to Delete")
        else:
            self.head=self.head.next


LL=LinkedList()
LL.addAtFront(1)
LL.addAtFront(2)
LL.addAtFront(3)
LL.addAtFront(4)
LL.printList()
LL.deleteFromFront()
LL.printList()        


        