
#Circular single linked list

class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
def circularSinglelinkedList(arr):
    head= None
    for val in arr:
        if(head ==None):
            head =Node(val)
            temp=head
        else:
            temp.next=Node(val)
            temp=temp.next
    temp.next=head
arr=list(map(int,input().split()))
print(circularSinglelinkedList(arr))
