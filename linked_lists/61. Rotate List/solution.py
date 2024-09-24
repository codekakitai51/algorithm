# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        n = 1
        cur = head

        while cur.next:
            cur = cur.next
            n += 1
        # close the linked list into the ring
        cur.next = head

        newTail = head
        for _ in range(n - k % n - 1):
            newTail = newTail.next
        newHead = newTail.next

        # break the ring
        newTail.next = None

        return newHead


