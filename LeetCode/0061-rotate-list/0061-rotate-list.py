# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count=0
        lc=1
        l=head
        if l is None:
            return head
        if l.next is None:
            return head
        while l.next:
            l=l.next
            lc=lc+1
        l.next=head
        ll=head
        k=k%lc
        for _ in range(lc-k-1):
            ll=ll.next
        llast=ll.next
        ll.next = None
        
        return llast