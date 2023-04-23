# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l1=head
        ll=list()
        tot=0
        flag=0
        while l1.next:           
            if l1!=0:
                flag=1
            if flag==1 and l1.next.val==0:
                tot=tot+l1.val
                ll.append(tot)
                tot=0
            else:
                tot=tot+l1.val
            l1=l1.next
        return arr(ll)
def arr(l):
    head=None
    for i in l:
        node=ListNode(i)
        if head is None:
            head=node
            l1=head
        else:
            l1.next=node
            l1=node
    return head

