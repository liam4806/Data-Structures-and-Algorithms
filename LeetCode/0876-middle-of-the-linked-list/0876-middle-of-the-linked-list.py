# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l1=head
        count=0
        l2=head
        x=0
        while l1:
            l1=l1.next
            count+=1
        count=count//2+1
        
        while x!=count-1:
            l2=l2.next
            x+=1
        return l2
