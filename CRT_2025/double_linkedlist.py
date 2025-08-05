
#Double linked List

class Node:
    def __init__(self,val):
        self.prev=None
        self.data=val
        self.next=None
def doubleLinkedList(arr):
    head= None
    for val in arr:
        if(head ==None):
            head =Node(val)
            temp=head
        else:
            newNode=Node(val)
            temp.next=newNode
            newNode.prev=temp
            temp=temp.next
    return head.data
arr=list(map(int,input().split()))
print(doubleLinkedList(arr))
