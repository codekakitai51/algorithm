# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)

        return self.merge(left, right)
    
    def merge(self, list1, list2):
        dummyHead = ListNode(0)
        prev = dummyHead
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next

        prev.next = list1 if list1 else list2
        return dummyHead.next

    
    def getMid(self, head):
        midPrev = None
        slow, fast = head, head
        while fast and fast.next:
            midPrev = slow
            slow = slow.next
            fast = fast.next.next
        
        midPrev.next = None
        return slow
