
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        frnode=head
        senode=head
        for i in range(n):
            if senode.next is None:
                try:
                    if senode.next.next is None:
                        return 
                except:
                    frnode=frnode.next
                    return frnode
            senode=senode.next
        while senode.next:
            if senode.next is None:
                break
            frnode=frnode.next
            senode=senode.next
        frnode.next=frnode.next.next

        return head