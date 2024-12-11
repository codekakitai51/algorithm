# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:  
# both O(n) but this is bit faster
        # Edge case: return None if there is only one node.
        if head.next == None:
            return None
        
        # Initialize two pointers, 'slow' and 'fast'.
        slow, fast = head, head.next.next
        
        # Let 'fast' move forward by 2 nodes, 'slow' move forward by 1 node each step.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # When 'fast' reaches the end, remove the next node of 'slow' and return 'head'.
        slow.next = slow.next.next
        
        # The job is done, return 'head'.
        return head

# ---------        
        # # count
        # n = 0
        # cur = head
        # while cur:
        #     cur = cur.next
        #     n += 1

        # if n == 1:
        #     return None

        # # move to target
        # prev = ListNode(0, head)
        # head = prev.next
        # cur = head

        # targetIdx = n // 2
        # for _ in range(targetIdx):
        #     prev = cur
        #     cur = cur.next
        
        # # remove
        # prev.next = cur.next
        # cur.next = None
    
        # return head