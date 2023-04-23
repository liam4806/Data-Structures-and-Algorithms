# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l1=head
        start=ListNode()
        start.next=l1
        l1=start
        l3=l1
        while l1:
            if l1.next==None or l1.next.next == None:
                break
            l=l1.next.val
            if l1.next.next.val == l:
                l2=l1
                l1=l1.next
                l2.next=None
                while l1.val == l:
                    if l1.next==None:
                        l1=None
                        break
                    l1=l1.next
                l2.next=l1
                l1=l2
            else:
                l1=l1.next
                    
        return l3.next





                
                

            
        