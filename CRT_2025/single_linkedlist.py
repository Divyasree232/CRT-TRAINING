
# single linked list

class Node:
    def __init__(self,val):# To create node constructor is required and constructor is used for instance of variables
        self.data=val
        self.next=None
def linkedList(arr):
    head= None
    for val in arr:
        if(head ==None):
            head =Node(val)#node(val) means address
            temp=head
        else:
            temp.next=Node(val)
            temp=temp.next
    return head.data
arr=list(map(int,input().split()))
print(linkedList(arr))
