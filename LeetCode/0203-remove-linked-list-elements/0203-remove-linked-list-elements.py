# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        l1=head
        l2=ListNode(0)
        l2.next=l1
        l1=l2
        if l1 == None:
            return l1  
        while l1:
            while l1.next and l1.next.val == val:
                l1.next=l1.next.next
            l1=l1.next
        return l2.next
        

