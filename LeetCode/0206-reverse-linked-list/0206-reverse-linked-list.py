# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        l1=head
        newhead=ListNode()
        while l1:
            newhead=l1.next
            l1.next=prev
            prev=l1
            l1=newhead

        return prev



